import datetime
import os
import pyttsx3
import cv2
import random
import urllib.request
import json
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import time
import smtplib

import speech_recognition as sr

KEY_UP = pyautogui.keyUp("alt")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("I am jarvis, how can I help you?")


def news():
    main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=1dca249453464b7eb0b95f13e72f65bd"
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[1]} news is: {head[1]}")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('swatiatul5@gmail.com', 'newstartnew19')
    server.sendmail('swatiatul5@gmail.com', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 6
        audio = r.listen(source, timeout=6, phrase_time_limit=5)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("say that again please")
        return "none"
    return query



if __name__ == "__main__":
        wish()
        while True:
            query = takeCommand().lower()
            if "open notepad" in query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in query:
                os.system("start cmd")

            elif "open adobe reader" in query:
                apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\ProgramsAcrobat Reader DC"
                os.startfile(apath)

            elif "email " in query:
                try:
                    speak("What should I send?")
                    content = takeCommand().lower()
                    to = "bodkemihika@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    print("sorry I am not able to send")

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow("webcam", img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cap.destroyAllWindows()

            elif "play music" in query:
                music_dir = "C:\\Users\\Mihika Atul\\Desktop\\music"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "ip address" in query:
                ip = get("https://api.ipify.org").text
                speak(f"your ip address is {ip}")

            elif "wikipedia" in query:
                speak("Searching wikipedia..")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open google" in query:
                speak("what do I search?")
                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")
                webbrowser.open("www.google.com")
                speak("according to google")
                speak(results)
                print(results)

            elif "open stack overflow" in query:
                webbrowser.open("www.stackoverflow.com")

            elif "send message " in query:
                kit.sendwhatmsg("+917021888491", "I hate you", 5, 37)

            elif "play songs on youtube" in query:
                kit.playonyt("see you again")

            elif "set alarm" in query:
                nn = int(datetime.datetime.now().hour)
                if nn == 22:
                    music_dir = "C:\\Users\\Mihika Atul\\Desktop\\music"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))

            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down" in query:
                os.system("shutdown /s/t/5")

            elif "restart" in query:
                os.system("shutdown /r/t/5")

            elif "sleep" in query:
                os.system("rundll32.exe powproof.dll, SetSuspendState 0,1,0")

            elif "switch the window" in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)

            elif "news" in query:
                news()

            elif "where am I" in query:
                speak("wait, let me check")
                try:
                    # ipAdd = requests.get('https://api.ipify.org').text
                    # print(ipAdd)
                    # url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    # geo_requests = requests.get(url)
                    # city = geo_data["city"]
                    # country = geo_data["country"]
                    # speak(f"I am not sure but I think we are in,{city} city of {country}")
                    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
                        data = json.loads(url.read().decode())
                        country = data['country_name']
                        city = data['city']
                        speak('According to me we are in ' + city + ' city of ' + country + ' country')

                # try:
                #     with urllib.request.urlopen("https://geolocation.com/json") as url:
                #         data = json.loads(url.read().decode())
                #         country = data['country name']
                #         city = data['city']
                #         speak(f"I am not sure but I think we are in,{city} city of {country}")
                except Exception as e:
                    speak("Sorry, no netowrk")


            elif "no thanks" in query:
                kit.playonyt("Thank you, Bye")
                sys.exit()

            # time.sleep(25)
            # speak("Can I do anything else?")











