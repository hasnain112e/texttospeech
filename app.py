import streamlit as st
import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Streamlit UI
st.title("🎙️ AI Voice Generator with pyttsx3")
st.write("Enter text, and generate AI audio for free!")

# Input text
text = st.text_area("Enter text to convert to speech:", "Hello, this is AI voice generation!")

# Language selection (support for Hindi and English)
language = st.selectbox("Select language:", ["English", "Hindi"])

# Set voice based on selected language
if language == "English":
    voice_id = "com.apple.speech.synthesis.voice.Alex"  # English voice
elif language == "Hindi":
    voice_id = "com.apple.speech.synthesis.voice.Vaani"  # Hindi voice (MacOS)

# Generate Button
if st.button("Generate Audio"):
    if text:
        with st.spinner("Generating voice..."):
            # Set the voice for the engine
            engine.setProperty('voice', voice_id)

            # Save the audio to an MP3 file
            file_path = "output.mp3"
            engine.save_to_file(text, file_path)
            engine.runAndWait()

            # Display audio player
            st.audio(file_path, format="audio/mp3")
    else:
        st.warning("Please enter some text!")
