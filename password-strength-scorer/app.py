from zxcvbn import zxcvbn
import streamlit as st

st.title("Password Strength Calculator")

password = st.text_input("Enter password")

if password:

    # ____Eveluation using function
    calculations = zxcvbn(password)

    # ___For debugging use this :
    #  st.write(calculations)

    # ____Evaluation  
    score = calculations["score"]
    guess_attempts = calculations["guesses"]

    # ___Display ramarks
    st.subheader("Remarks :")
    if(score == 1): 
         st.write("Vulnerable password . Zero strength and no security")
    elif(score == 2): 
         st.write("Very weak. Read security measures to fix this")
    if(score == 3): 
         st.write("Try improvements")
    if(score == 4): 
         st.write("Good !")

    # ____Displaing status :
    st.write(f"**Password Strength Score:** {score} / 4")
    st.write("🔢 **Guess Attempts Required:**", guess_attempts)
    st.write("⏳ **Crack Time (in seconds):** ", str(calculations["crack_times_seconds"]["offline_fast_hashing_1e10_per_second"]))

    
    if(calculations["feedback"]["warning"]):
        st.subheader("Warnings :")
        st.warning(calculations["feedback"]["warning"])

    if(calculations["feedback"]["suggestions"]):
        st.subheader("Suggestions and improvements:")
        for i in range(len(calculations["feedback"]["suggestions"])):
            st.write(f"- {calculations["feedback"]["suggestions"][i]}")
else:
    st.warning("⚠️ Please enter a password!")