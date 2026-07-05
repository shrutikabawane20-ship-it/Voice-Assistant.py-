import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am your voice assistant")

