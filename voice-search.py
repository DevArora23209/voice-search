import pyttsx3
import speech_recognition as sr
from googlesearch import search
import webbrowser

def command():
    r = sr.Recognizer()
    x = 0  
    while True:
        with sr.Microphone() as source:
            print("Danta: Listening.....")
            audio = r.listen(source)
            try:    
                query = r.recognize_google(audio)
                print(f"master: {query}")
                return query
            except sr.UnknownValueError:
                print("Could not understand audio, try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
        
        x += 1
        if x == 1:
            break 

while True:
    query = command().lower() 
    if query: 
        for i in search(query, tld="com", num=1, stop=1, pause=2):
            print(f"Opening: {i}")
            webbrowser.open(i)
    else:
        print("No query was recognized.")
