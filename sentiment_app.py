import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import time

st.title("Sentiment Analysis App with Multiple Language Support")
st.markdown("""
    ### Check the sentiment of any text in multiple languages!
    Enter a sentence below, and we'll tell you whether it's positive, negative, or neutral. 😊😠😐
    🌍 Supports multiple languages!
""")


user_input = st.text_input("Enter a sentence:")

if user_input:
    
    blob = TextBlob(user_input)
    detected_language = blob.detect_language()

    
    if detected_language != 'en':
        with st.spinner(f'Translating from {detected_language} to English...'):
            translated_input = blob.translate(to='en')
            st.write(f"Original Text ({detected_language}): {user_input}")
            st.write(f"Translated to English: {translated_input}")
    else:
        translated_input = user_input
        st.write(f"Original Text (English): {user_input}")

    
    with st.spinner('Analyzing sentiment...'):
        time.sleep(2)  
        
        
        sentiment_blob = TextBlob(translated_input)
        sentiment = sentiment_blob.sentiment.polarity

    st.success("Analysis complete!")
    
    
    st.markdown(f"**Polarity Score:** {sentiment:.2f}")
    
 
    if sentiment > 0:
        st.success("The sentiment is **Positive** 😊")
    elif sentiment < 0:
        st.error("The sentiment is **Negative** 😠")
    else:
        st.info("The sentiment is **Neutral** 😐")

  
    st.progress(100)  

    
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [sentiment if sentiment > 0 else 0, 
             -sentiment if sentiment < 0 else 0, 
             1 if sentiment == 0 else 0]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#32CD32", "#FF6347", "#D3D3D3"])
    ax.axis('equal')  
    
    st.pyplot(fig)

    
    st.markdown("""
        ---
        [Check out my GitHub Repository](https://github.com/Codingcodercodes/sentiment-analyzer)) | [LinkedIn](https://www.linkedin.com/in/p-charmi-reddy-b2aaa2294/)
    """)


if 'history' not in st.session_state:
    st.session_state.history = []


if user_input:
    st.session_state.history.append(f"Sentiment of '{user_input}' is {'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'}")

if st.session_state.history:
    st.subheader("Sentiment History:")
    for history_item in st.session_state.history:
        st.write(history_item)
