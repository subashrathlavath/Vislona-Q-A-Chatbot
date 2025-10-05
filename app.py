import streamlit as st
from faq_engine import TFIDF_Engine
from gemini_engine import Gemini_Engine

st.title("Vislona Chatbot")

@st.cache_resource
def load_engines():
    faq_engine = TFIDF_Engine()
    gemini_engine = Gemini_Engine()
    return faq_engine, gemini_engine

faq_engine, gemini_engine = load_engines()

user_query = st.text_input("Ask me anything about Vislona:")

if st.button("Ask"):
    if user_query:
        with st.spinner("Thinking..."):
            faq_response = faq_engine.get_response(user_query)
            if faq_response:
                st.write("**Answer:**", faq_response)
            else:
                gemini_response = gemini_engine.get_response(user_query)
                st.write("**Answer:**", gemini_response)
    else:
        st.warning("Please enter a question.")
