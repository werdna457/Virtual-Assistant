#This is a Virtual Assistant that doesn't a) have a personality or b) sell your data
#https://dev.to/vinayveerappaji/create-your-own-simple-virtual-assistant-1kfp

#First import libraries
import speech_recognition as sr #speech to text
from gtts import gTTS #Text to speech
import playsound #play audio
import os #Talk to Windows
import sys
import time #Tells the time
from time import ctime

def listen():   #Listening Function
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening..")
        audio = r.listen(source,phrase_time_limit = 10)
    data=""
    try:
        data = r.recognize_google(audio,language='en-GB')
        print("You said: "+data)
    except sr.UnknownValueError:
        print("I cannot hear you")
    except sr.RequestError as e:
        print("Request Failed")
    return data

def respond(String):  #Response Function
    print(String)
    tts = gTTS(text=String,lang="en")
    tts.save("Speech.mp3")
    playsound.playsound("Speech.mp3")
    os.remove("Speech.mp3")

def voice_assistant(data):  #Assistant program
    if "who are you" in data:
        listening = True
        respond("I am your assistant")
    if "hello" in data:
        listening = True
        respond("Hello")
    if "time" in data:
        listening  = True
        respond(ctime())
    if "make an appointment" in data:
        listening = True
        f = open('Aps.txt','a') #Make an appointment to appointments document
        respond("Please state date, time, and description of your new appointment")
        apoin = listen()
        f.write("\n" + apoin)
        f.close()
    if ("appointment" in data) or ("appointments" in data) or ("calendar" in data):
        listening = True
        f = open('Aps.txt','r')  #Open in read mode
        aps = f.read()
        words = str("Your appointments are: " + aps);
        respond(words)
        f.close()
    if "goodbye" in data:
        respond("Goodbye")
        sys.exit()
    try:
        return listening
    except UnboundLocalError:
        print("TimedOut-->Re-Launch")

time.sleep(2)    #Call functions
respond("Hello, What can I do for you?")
listening = True
while listening == True:
    data = listen() #calling the listen()
    listening = voice_assistant(data)











    
