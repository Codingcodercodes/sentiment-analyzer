import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import time

# Customizing the app's title and description
st.title("Sentiment Analysis App with Multiple Language Support")
st.markdown("""
    ### Check the sentiment of any text in multiple languages!
    Enter a sentence below, and we'll tell you whether it's positive, negative, or neutral. 😊😠😐
    🌍 Supports multiple languages!
""")

# Input from the user
user_input = st.text_input("Enter a sentence:")

if user_input:
    # Detect the language of the user input
    blob = TextBlob(user_input)
    detected_language = blob.detect_language()

    # Translate to English if the detected language is not English
    if detected_language != 'en':
        with st.spinner(f'Translating from {detected_language} to English...'):
            translated_input = blob.translate(to='en')
            st.write(f"Original Text ({detected_language}): {user_input}")
            st.write(f"Translated to English: {translated_input}")
    else:
        translated_input = user_input
        st.write(f"Original Text (English): {user_input}")

    # Show a loading spinner while analyzing
    with st.spinner('Analyzing sentiment...'):
        time.sleep(2)  # Simulate some processing time
        
        # Perform sentiment analysis using TextBlob
        sentiment_blob = TextBlob(translated_input)
        sentiment = sentiment_blob.sentiment.polarity

    st.success("Analysis complete!")
    
    # Display Polarity Score with some styling
    st.markdown(f"**Polarity Score:** {sentiment:.2f}")
    
    # Sentiment Output with Emojis
    if sentiment > 0:
        st.success("The sentiment is **Positive** 😊")
    elif sentiment < 0:
        st.error("The sentiment is **Negative** 😠")
    else:
        st.info("The sentiment is **Neutral** 😐")

    # Adding a Progress Bar
    st.progress(100)  # Show full progress when analysis is done

    # Create and display a sentiment pie chart
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [sentiment if sentiment > 0 else 0, 
             -sentiment if sentiment < 0 else 0, 
             1 if sentiment == 0 else 0]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=["#32CD32", "#FF6347", "#D3D3D3"])
    ax.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
    
    st.pyplot(fig)

    # Add footer with GitHub and social media links
    st.markdown("""
        ---
        [Check out my GitHub Repository](https://github.com/Codingcodercodes/sentiment-analyzer)) | [LinkedIn](https://www.linkedin.com/in/p-charmi-reddy-b2aaa2294/)
    """)

# Add more fun features
# For example, include a text sentiment history feature
if 'history' not in st.session_state:
    st.session_state.history = []

# Save the sentiment history
if user_input:
    st.session_state.history.append(f"Sentiment of '{user_input}' is {'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral'}")
    
# Display sentiment history
if st.session_state.history:
    st.subheader("Sentiment History:")
    for history_item in st.session_state.history:
        st.write(history_item)
