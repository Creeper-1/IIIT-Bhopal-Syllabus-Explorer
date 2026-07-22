import streamlit as st
from bs4 import BeautifulSoup
import requests
import re

def module_name(a,b):
    url = f"https://iiitbhopal.ac.in/Document/ss/CSE-{a}00{b}.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    modules = soup.find_all("div", class_="modules")

    for module in modules:
        title = module.find("div", class_="top-row")
        content = module.find("div", class_="row")

        if title and content:
            module_title = re.sub(r"\s+", " ", title.get_text(strip=True))
            module_content = re.sub(r"\s+", " ", content.get_text(" ", strip=True))

            with st.expander(module_title):
                for topic in module_content.split(","):
                    st.markdown(f"- {topic.strip()}")

password = st.text_input(label="Enter password",type="password")

if password == "HK@1122":
    sem = st.selectbox(label="Choose Semester" , options=(1,2))

    sub1 = ["EM-1" , "Phy" , "FOCP" , "FOEE" , "PC"]
    sub2 = ["EM-2" , "DM" , "DLD" , "DSA" , "OPP"]
    
    option = sub1 if sem == 1 else sub2

    select = st.selectbox(label="Choose subject" , options=option)
    index = option.index(select)
    module_name(sem,index+1)

    st.write("Download Paper Here")

    with open( f"Paper\{sem}_{index+1}_M.pdf" , "rb") as file_type:
        file_data_M = file_type.read()
    
    with open( f"Paper\{sem}_{index+1}_E.pdf" , "rb") as file_type:
        file_data_E = file_type.read()
    
    st.download_button(
        label="Mid-Exam" , data= file_data_M , file_name= f"{select}_mid.pdf" , mime="application/pdf"
    )

    st.download_button(
        label="End-Exam" , data= file_data_E , file_name= f"{select}_end.pdf" , mime="application/pdf"
    )

else:
    st.stop()



