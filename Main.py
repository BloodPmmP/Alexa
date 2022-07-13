import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def alexa_say(text):
    engine.say(text)
    engine.runAndWait()

def run_cmd():
    try:
        with sr.Microphone() as source:
            print("listening.... Please Say Somthing....  ")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = run_cmd()
    if 'play' in command:
        song = command.replace('play', '')
        alexa_say('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H Hours %M Minutes and %S Seconds')
        print(time)
        alexa_say("Current Time Is" + time)
    elif 'turtles' in command or 'turtle' in command:
        alexa_say('I Love Watching Turtles they are my favorite')
    elif 'are you single' in command:
        alexa_say('sorry i am in a relationship with turtles')
    elif 'search' in command:
        search = command.replace('search', '')
        info = wikipedia.summary(search, 1)
        print(info)
        alexa_say(info)
run_alexa()
