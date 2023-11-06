# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        #speak("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open chat' in query:
            webbrowser.open("https://chat.openai.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   
        elif 'open lead code' in query:
            webbrowser.open("https://leetcode.com/studyplan/top-interview-150/")
        elif 'play funk music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=NDC3nRUTrMk&t=3s&ab_channel=PhonkCity")


        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=4tywp83zkmk")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open face recognition' in query:
            codePath = "C:\\Users\\DG\\OneDrive\\Desktop\\projects\\AI\\PYTHON_opencv\\facerecotion_and_boxed\\main.py"
            os.startfile(codePath)

        #C:\\Users\\DG\\OneDrive\\Desktop\\projects\\AI\\PYTHON_opencv\\facerecotion_and_boxed\\main.py
        
        else:
            print("try saying again")
            speak("sorry")