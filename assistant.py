from datetime import datetime
from decimal import setcontext
from logging import exception
from multiprocessing import context
from unittest.mock import sentinel
from pip import main
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 
from plyer import notification
import time
from time import sleep, time
from pip import main
from plyer import notification
import schedule
import pywhatkit
import pyjokes
import random
import pyscreenshot
from selenium import webdriver



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How can i help you sir.")    

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('harshkaushik8810@gmail.com', '123@hkaushik')
    server.sendmail('harshkaushik8810@gmail.com', to, content)
    server.close()
def leave():
    ex=random.randint(1,5)
    if ex==1:
        speak("See You Later Alligator.")
    elif ex==2:
        speak("Be well, do good work, and keep in touch.")
    elif ex==3:
        speak("Its time to say goodbye.")
    elif ex==4:
        speak("Adios!")
    elif ex==5:
        speak("See you Sir!")

def startup():
    ex=random.randint(1,5)
    if ex==1:
        print("Trying saying set a reminder....")
    elif ex==2:
        print("Trying saying what is cleopata on wikipedia........")
    if ex==3:
        print("Trying saying set a reminder.......")
    if ex==4:
        print("Trying saying play some music on youtube........")
    if ex==5:
        print("Trying saying rock paper scissor.........")

def ss():
  image = pyscreenshot.grab()
  image.show()
  speak("Enter file name.")
  a=input("Enter file name")
  image.save(f"{a}.png")
  speak("File saved.")


if __name__=="__main__":
    speak("Hey its me your Virtual Assistant.")
    speak("May i ask your name please.")
    name=input("Enter your name")
    speak(F"Hello {name} welcome back.")
    wishme()
    startup()
    lol=1
    while lol==1:
        query=takeCommand().lower()


        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open chrome' in query:
            path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'open youtube' in query:
               webbrowser.open("youtube.com")
        elif 'open google' in query:
               webbrowser.open("google.com")
        elif 'open email' in query:
               webbrowser.open("email.com")
        elif 'open facebook' in query:
               webbrowser.open("facebook.com")
        elif 'open twiter' in query:
               webbrowser.open("twitter.com")
        elif 'open instagram' in query:
               webbrowser.open("instagram.com")
        elif 'music' in query:
            music_dir='D:\\music'
            song=os.listdir(music_dir)
            print(song)
            os.startfile(os.path.join(music_dir,song[0]))
        elif 'the time' in query:
            time=datetime.now().strftime("%I:%M:%p")
            print(time)
            speak(f"Current time is {time}")  
        elif 'open vs code' in query:
                path="B:\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
        elif 'send email' in query:
            try:
                to = input("enter email id whom you want to send mail") 
                speak("What should I type?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                #print(e)
                speak("something went wrong")    
        elif 'rock paper scissor' in query:
                from project1 import *
        elif 'who are you' in query:
            speak("I am a Virtual assistant created by sir Harsh Kaushik in VS code. with the help of Python language, and im a capable of doing many things icluding play music, play video, open application and still working on lots of process. ")
        elif'how are you' in query:
            speak("im fine. How are you sir")   
        elif'add' in query:
            from calculator import sum
            sum()
        elif'subtract' in query:
            from calculator import sub
            sub()
        elif'divide' in query:
            from calculator import div
            div()
        elif'multiply' in query:
            from calculator import mul
            mul()
        elif'factor' in query:
            from calculator import fact
            fact()
        elif'currency' in query:
            from convertor import convertor
            convertor()
        elif'remind' in query:
            speak("set your own reminder.")
            from noti import noti
            noti()       
        elif 'password' in query:
            speak("wait a moment please")
            from password import password
            password()
        elif "guess the number" in query:
            from project2 import game
        elif"my age" in query:
            from age import guessage  
            guessage() 

        elif 'on youtube' in query:
            speak(f"playing{query}")
            pywhatkit.playonyt(query)
        elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif ' make a joke on me' in query:
            speak("your whole life is a joke bro... ")
        elif 'single' in query:
            speak("No sorry,Im not like you broke and single as fuck, I got boyfriend. You looser.")
        elif'hurt me' in query:
            speak("All i said was facts buddy.you dont even have a girl friend. Get some bitches first")
        elif"roll a dice" in query:
            from dice import roll
            roll()
        elif"roll two dice" in query:
            from dice import roll2
            roll2()
        elif "into inch" in query:
            from unit import *
            inch()
        elif "into centimeter" in query:
            from unit import *
            cm()
        elif "into meter" in query:
            from unit import *
            meter()
        elif "into mile" in query:
            from unit import *
            mile()
        elif "into foot" in query:
            from unit import *
            foot()
        elif "into yard" in query:
            from unit import *
            yard()
        elif"shutdown pc" in query:
            os.system("shutdown /s")
        elif "file" in query:
            location=input("Enter Drive and file name (eg. D:\\file name)")
            print("Creating....... wait a moment")
            os.mkdir(location)
            speak(f"file created succesfully at {location}")
        elif "remove file" in query:
            location=input("Enter Drive and file name (eg. D:\\file name)")
            print("Removing....... wait a moment")
            os.rmdir(location)
            speak(f"file Removed succesfully from {location}.")
        elif "screenshot" in query:
            ss()
        elif 'bye' in query:
            leave()
            lol=lol-1
        