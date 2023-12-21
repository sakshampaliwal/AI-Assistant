import tkinter as tk
from tkinter import messagebox
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Alexa Two Point o Sir. Please tell me how may I help you")


def get_audio_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"


def take_command():
    query = get_audio_input().lower()
    return query


def execute_command(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    # Add other commands here based on your requirements


def on_click():
    query = take_command()
    if query == "None":
        messagebox.showinfo("Info", "Sorry, I didn't get that. Please try again.")
    else:
        execute_command(query)


def create_gui():
    root = tk.Tk()
    root.title("Voice Assistant")

    label = tk.Label(root, text="Click the button to start listening:")
    label.pack()

    button = tk.Button(root, text="Listen", command=on_click)
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    wishMe()
    create_gui()
