import streamlit as st
import re  # importing regex module

st.title("Password strength calculator")

def strength_calculator(password):

    # ____Initializing variables for score security measures and keywords ...
    score = 0
    security_measures = []
    key_words = ""

    # ____Recording uppercase, lowercase  and special characters along with password length
    length = len(password)
    uppercase_letters = re.findall("[A-Z]",password)
    number_chars = re.findall("[0-9]",password)
    lower_letters = re.findall("[a-z]",password)
    special_chars = re.findall(r"[!@#$%^&*()_\-+=\[\]{}<>?/.,~`:;|\\]",password)

    # ____Evaluating password with it's length
    if(length >=8):
        score+=1
    else: security_measures.append("Ensure that the password contains 8 characters or long")   

    # ____Evaluating passwords with uppercase characters
    if(len(uppercase_letters)>=1):
        score+=1
    else: security_measures.append("A strong password must have 1 or 2 uppercase characters")

    # ____Evaluating password with lowercase characters
    if(len(lower_letters)>=1):
        score +=1
    else: security_measures.append("Strong passwords must have atleast 1 lowercase character")

    # ___Eveluating passwords with special characters
    if(len(special_chars)>=2):
          score +=1
    else : security_measures.append("A strong password must contain atleast 2 special characters")
    
    # ___Eveluating passwords with special characters
    if(len(number_chars)>=2):
          score +=1
    else : security_measures.append("A strong password must contain atleast 2 numeric characters")

    # ____Generating keywords ...
    if(score == 5):
        key_words = "Strong password"
    elif(score <5 and score >3):
        key_words = "Moderate password"
    elif(score <3 and score > 1):
        key_words = "Very weak. Read security measures to fix this"
    else: key_words = "Vulnerable password . Zero strength and no security"

    return {
        "Score":score,
        "Security-measures":security_measures,
        "Keywords":key_words
    }

password = st.text_input("Enter your password")
calculated_result = strength_calculator(password)
calculated_score = calculated_result["Score"]
security_measures = calculated_result["Security-measures"]
key_words = calculated_result["Keywords"]

# ____Displaying outputs:
st.title("Results")
st.write("Score :", calculated_score)

if(len(security_measures) == 0) :
    st.write("No vulnurabilites found")
else :
    st.write("Security measures :")
    for str in security_measures :
        st.write(str)

st.write("Keywords : ", key_words)