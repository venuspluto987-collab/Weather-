import streamlit as st
import pandas as pd

st.set_page_config(page_title="College Chatbot", page_icon="🎓")

st.title("🎓 College Support Chatbot")

# Load CSV
df = pd.read_csv("college_chatbot_data.csv")

question = st.text_input("Ask your question:")

if question:
    found = False
    
    for i in range(len(df)):
        if question.lower() in df["question"][i].lower():
            st.success("🤖 Bot: " + df["answer"][i])
            found = True
            break
    
    if not found:
        st.error("🤖 Bot: Sorry, I don't understand. Ask about fees, admission, hostel, courses etc.")