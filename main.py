import pyttsx3
import speech_recognition as sr
import requests
import json
from typing import Dict, Any, Optional
from datetime import datetime
from datetime import  timedelta
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
from robot_interface import create_robot_interface
from dotenv import load_dotenv
import pyjokes
import pyautogui
from groq import Groq
import requests
from bs4 import BeautifulSoup
import psutil
import imdb
from GoogleNews import GoogleNews 
import pandas as pd
import time
load_dotenv()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold=180
        audio=r.listen(source,timeout=3,phrase_time_limit=5)
    try:
        print("Recogninzing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said {query}")

    except Exception as e:
        print("Say that again please...")
        return None
    return query
    
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

def user_name():
    speak("what should i call u ")
    name=takecommand()
    speak(f"Hello {name} welcome")

def wish():
    hour=int(datetime.now().hour)
    if (hour>0 and hour <12):
        speak("Good Morning")
    elif(hour >=12 and hour <18):
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am shara , i am your desktop assistant")

def cpu():
    usage=str(psutil.cpu_percent())
    speak(f"cpu is at {usage}")
    battery=psutil.sensors_battery()
    speak(f"cpu is at {battery}")

def movie():
    
    movie_db = imdb.IMDb()
    speak("Please tell me the movie name, sir.")
    mov_name = takecommand()


    speak(f"Searching for {mov_name}...")
    movies = movie_db.search_movie(mov_name)

    if not movies:
      speak("No movie found.")
    else:
        speak("I found these:")
        for movie in movies[:5]:  # Limit to the first 5 results for brevity
            title = movie.get("title", "Unknown Title")
            year = movie.get("year", "Unknown Year")
            speak(f"{title} - {year}")
        
      
            movie_id = movie.getID()
            detailed_movie = movie_db.get_movie(movie_id)
        
            rating = detailed_movie.get("rating", "No rating available")
            plot = detailed_movie.get("plot outline", "No summary available")
        
      
            speak(f"{title} was released in {year} and has an IMDb rating of {rating}.")
            speak(f"The summary of the movie is: {plot}")



def news():
    news_info=GoogleNews(period="1d")
    news_info.search("India")
    news_res=news_info.result()
    news_data=pd.DataFrame.from_dict(news_res)
    news_data_print=news_data.drop(columns=["img"])
    news_data_print.head()
    for i in news_res:
        # print(i["title"])
        speak(i["title"])

if __name__ == "__main__":
    create_robot_interface() 
    wish()
    
    while True:
        speak("Do you need any work to be done")
        
        query=takecommand().lower()

       
        if query is None:
            speak("I could not hear it properly . could you speak it again.")
            continue
        if query.strip()=="":
            speak("I could not hear it properly . could you speak it again.")
            continue
        elif "use ai" in query:
        

            os.environ["GROQ_API_KEY"] = "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"



            client = Groq()
            speak("what do you want to know")
            user_ques=takecommand().lower()

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                    "role": "user",
                    "content": user_ques,
                }
         ],
            model="llama3-8b-8192",
            stream=False,
            )

            user_ans=chat_completion.choices[0].message.content
            speak(user_ans)

        elif "ai" in query:
        

            os.environ["GROQ_API_KEY"] = "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"



            client = Groq()
            speak("what do you want to know")
            user_ques=takecommand().lower()

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                    "role": "user",
                    "content": user_ques,
                }
         ],
            model="llama3-8b-8192",
            stream=False,
            )

            user_ans=chat_completion.choices[0].message.content
            speak(user_ans)

        elif "dance" in query:
            file_path = 'D:/jarvis/dance.html'
            music_dir="C:\\Users\\Shara\\Music\\only music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

            speak("ok , sir we are executing your command")
            speak("hope you enjoy my dance")
         
            webbrowser.open(f'file://{file_path}')

        elif "artificial intelligence" in query:
        

            os.environ["GROQ_API_KEY"] = "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"



            client = Groq()
            speak("what do you want to know")
            user_ques=takecommand().lower()

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                    "role": "user",
                    "content": user_ques,
                }
         ],
            model="llama3-8b-8192",
            stream=False,
            )

            user_ans=chat_completion.choices[0].message.content
            speak(user_ans)

        elif "hello" in query:
            speak("Hello My friend , hope you are good . how can i help you")
        elif "i am fine" in query:
            speak("thats great, you are my everything sir ")


        elif "open notepad" in query:
            npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
        elif "command prompt" in query:
            os.system("start cmd")
        elif "camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(50)
                if k==28:
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir="C:\\Users\\Shara\\Music\\only music"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "ip address" in query:
            ip=get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")
        elif "google" in query:
            speak("opening google")
            speak("What do you want to know")
            ques=takecommand().lower()
            info=f"https://www.google.com/search?q={ques}"
            r=requests.get(info)
            data=BeautifulSoup(r.text,"html.parser")
            my_res=data.find("div", class_ = "BNeawe").text
            speak(f"{ques}  is {my_res}")
            
        elif "write a note" in query:
            speak("what should i write.")
            note=takecommand()
            file=open('shara.txt','w')
            file.write(note)
        
        elif "show notes" in query:
            file=open('shara.txt',r)
            speak(file.read())
            print(file.read())
            
        
            print(my_res)
      
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
        
        elif "send message" in query:
            
            send_time = datetime.now() + timedelta(minutes=2)

            kit.sendwhatmsg(
            "+919697738407",  
            "Hello",          
            send_time.hour,   
            send_time.minute  
            )


        elif "songs" in query:
            speak("Which song do you want to listen")
            song=takecommand().lower()
            speak("Ok executing your command")
            kit.playonyt(song)

            
        
        elif "time now" in query:
            timenow = datetime.now().strftime("%H:%M")
            speak(f"Time now is {timenow}")


        elif "cpu" in query:
            cpu()

        elif "movie" in query:
            movie()

        elif "news" in query:
            news()




        elif "joke" in query:
            speak(pyjokes.get_joke(language="en",category="neutral"))
        
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "alt tab" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")



        elif "screenshot"  in query:
            speak("please tell me the name of the file")
            fil_name=takecommand().lower()
            speak("Hold on the screen , i am taking the screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{fil_name}.png")
            speak("image captured and saved")

        elif "prt sc"  in query:
            speak("please tell me the name of the file")
            fil_name=takecommand().lower()
            speak("Hold on the screen , i am taking the screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{fil_name}.png")
            speak("image captured and saved")

        elif "print screen"  in query:
            speak("please tell me the name of the file")
            fil_name=takecommand().lower()
            speak("Hold on the screen , i am taking the screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{fil_name}.png")
            speak("image captured and saved")

               


        elif "thank you" in query:
            speak("It was good work with you")
            speak("I shara terminating myself")
            sys.exit()

        elif "thankyou" in query:
            speak("It was good work with you")
            speak("I shara terminating myself")
            sys.exit()
        
        elif "bye" in query:
            speak("It was good work with you")
            speak("I shara terminating myself")
            sys.exit()

        elif "about you" in query:
            speak("I am shara An a.i assisstant . i am able to do your work an desktop assisstant ")
        
        
        
        else:
            os.environ["GROQ_API_KEY"] = "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"



            client = Groq()
            speak("what do you want to know")
            user_ques=takecommand().lower()

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                    "role": "user",
                    "content": user_ques,
                }
         ],
            model="llama3-8b-8192",
            stream=False,
            )

            user_ans=chat_completion.choices[0].message.content
            speak(user_ans)


        
          

            
















