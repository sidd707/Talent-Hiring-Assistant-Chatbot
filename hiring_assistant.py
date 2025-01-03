
# Your Streamlit app code goes here
import google.generativeai as genai
import streamlit as st
from pyngrok import ngrok

# Google Gemini API key configuration
genai.configure(api_key="AIzaSyB7B4LHaqEMvACJXnqC4qe_hI-DS1yqGsk")  # Replace with your Google Gemini API Key

# Streamlit App
st.title("TalentScout Hiring Assistant Chatbot")
st.markdown("""
Welcome to the TalentScout Hiring Assistant Chatbot! This bot will help gather your information and ask relevant technical questions based on your declared tech stack.
""")

# Collect Candidate Information
with st.form("candidate_form"):
    st.header("Candidate Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.text_input("Years of Experience")
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (e.g., Python, Django, MySQL)")
    submitted = st.form_submit_button("Submit")

# Generate Technical Questions
if submitted:
    if name and email and phone and experience and position and location and tech_stack:
        st.success("Thank you for submitting your details! Generating questions...")
        
        # Prompt construction
        prompt = f"""
You are a recruitment assistant for a technology company. Based on the candidate's information, generate 3-5 technical questions for each technology they are proficient in.
Candidate Details:
Name: {name}
Tech Stack: {tech_stack}
"""
        
        try:
          # Use the correct method to generate content
          model = genai.GenerativeModel("gemini-1.5-flash")
          response = model.generate_content(prompt)
          questions = response.text
          st.subheader("Generated Technical Questions:")
          st.write(questions)
        except Exception as e:
            st.error("Error generating questions. Please try again.")
            st.write(e)
    else:
        st.warning("Please fill out all fields before submitting.")
# End Conversation
st.sidebar.header("Exit Chat")
end_chat = st.sidebar.button("End Conversation")
if end_chat: 
    st.write("Thank you for using the TalentScout Hiring Assistant Chatbot! Goodbye.")
