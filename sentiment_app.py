import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analyzer")
user_input = st.text_input("Enter a sentence:")

if user_input:
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    st.write("Polarity Score:", sentiment)
    if sentiment > 0:
        st.success("Positive 😊")
    elif sentiment < 0:
        st.error("Negative 😠")
    else:
        st.info("Neutral 😐")
