import streamlit as st
import speech_recognition as sr

st.title("🎤 Speech to Text App")

st.write("Upload an audio file (WAV format) and get text output.")

audio_file = st.file_uploader("Upload Audio File", type=["wav"])

if audio_file is not None:
    recognizer = sr.Recognizer()

    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    audio = sr.AudioFile("temp.wav")

    with audio as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        st.success("Transcription:")
        st.write(text)
    except sr.UnknownValueError:
        st.error("Could not understand audio")
    except sr.RequestError:
        st.error("API error. Check internet connection.")
