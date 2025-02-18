import streamlit as st;  # importing main streamlit class  
import pandas as pd; # importing pandas for data analysis
import os;  # importing machine configurations
from io import BytesIO; # importing BytesIO module so that we can perform operations on bytes as well

# setting page title and page initial display centered or wide for long
st.set_page_config(page_title=" Stream lit 1st assignment app", layout="wide"); 

st.markdown("""
<style>
            .green-label { background-color:#63ebb9; color:white;}
            </style>
""",unsafe_allow_html=True)

#___Main sectoin in the page
st.title("Test Report analysis");

#___Content on that main page
st.write("Website test report analytics");

#___Allowing user to upload files Where:
# type accepts an array of file type allowed in this field
#accept_multiple_files=true  allow multiple uploads

uploaded_files = st.file_uploader("\nupload test report in cvs format only", type=["csv"], accept_multiple_files=True)

# If files exist then loop over them 
testStatus = None;

if(uploaded_files):
    i=0;
    for file in uploaded_files:
        i+=1
        print(file.name)
        file_extension = os.path.splitext(file.name)[1].lower();
        print(file_extension)

        # if file_ext == ".csv" :
        #     print("hello world");
        # elif file_ext != ".csv" :
        #         print("Hi world")
        if file_extension == ".csv" :
            df = pd.read_csv(file);
            testStatus = df["Status:"];
            print(testStatus.value_counts())
            
            if testStatus is not None :
                st.title(f"For Tests :");
                st.write(f"File name :", file.name)
                st.write(f"File extension :", file_extension)
                st.write(f"File size in MBs: ", file.size)
                st.write(f"Passed :", testStatus.value_counts().get("Passed"));
                st.write(f"Failed :", testStatus.value_counts().get("Failed"))
                st.write(f"Onhold :", testStatus.value_counts().get("Onhold"))