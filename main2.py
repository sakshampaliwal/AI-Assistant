import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import urllib.parse
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

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
            speak("What would you like to search on Google?")
            search_query = takeCommand()
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            speak(f"Searching Google for {search_query}")

            # Make a request to the Google search page
            google_page = requests.get(search_url)
            soup = BeautifulSoup(google_page.content, 'html.parser')

            # Find and extract the first search result
            search_results = soup.find_all('div', class_='tF2Cxc')
            if search_results:
                first_result = search_results[0].find('div', class_='BNeawe iBp4i AP7Wnd').text
                speak("Here is the first result from Google:")
                speak(first_result)
            else:
                speak("Sorry, I couldn't find any search results.")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            speak("What song would you like to play?")
            song_name = takeCommand()
            search_query = urllib.parse.quote(song_name)
            search_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(search_url)
            speak(f"Playing the first result for {song_name} on YouTube.")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyouremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
