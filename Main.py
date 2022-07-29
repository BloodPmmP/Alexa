import random
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def alexa_say(text: str):
    engine.say(text)
    engine.runAndWait()

def sendMsg(number: str, timeHour: int, timeMins: int, message: str): 
    pywhatkit.sendwhatmsg(number, message, timeHour, timeMins)

def run_cmd():
    try:
        with sr.Microphone() as source:
            print("listening.... Please Say Somthing....  ")
            alexa_say('listening please say something')
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
        
    elif 'tongue twister' in command:
        twisters = [
            'Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter Piper picked a peck of pickled peppers Where\'s the peck of pickled peppers Peter Piper picked',
            'How much wood would a woodchuck chuck if a woodchuck could chuck wood He would chuck he would as much as he could and chuck as much wood as a woodchuck would if a woodchuck could chuck wood.',
            'I scream you scream We all scream for ice cream.',
            'Betty Botter bought some butter but said she, the butter\'s bitter If I put it in my batter it will make my batter bitter But a bit of better butter will make my bitter batter better So she bought some better butter better than the bitter butter put it in her bitter batter made her bitter batter better So better Betty Botter bought some better butter',
            'She sells seashells on the seashore The shells she sells are seashells I\'m sure And if she sells seashells on the seashore Then I\'m sure she sells seashore shells',
            'Birdie birdie in the sky laid a turdie in my eye If cows could fly I\'d have a cow pie in my eye',
            'How much ground would a groundhog hog if a groundhog could hog ground A groundhog would hog all the ground he could hog if a groundhog could hog ground',
            'Yellow butter purple jelly red jam black bread Spread it thick say it quick',
            'If you must cross a course cross cow across a crowded cow crossing cross the cross coarse cow across the crowded cow crossing carefully',
            'Brisk brave brigadiers brandished broad bright blades blunderbusses and bludgeons — balancing them badly'
        ]
        random.shuffle(twisters)
        randomTwister = random.randint(0, 9)
        print(twisters[randomTwister])
        alexa_say(twisters[randomTwister])

    elif 'send a mail' in command or 'send a email' in command or 'send an email' in command:
        alexa_say('this function is under process')

    elif 'repeat my words' in command or 'repeat' in command or 'say' in command:
        words = command.replace('repeat my words', '') or command.replace('repeat', '') or command.replace('say', '')
        alexa_say(words)

    elif 'what is' in command:
        if '+' in command:
            edit = command.replace('what is ', '')
            edit1 = edit.removeprefix(' ')
            edit = edit1.replace('+ ', '')

            question = edit.split(' ')
            ans = sum(map(int, question))
            print(ans)
            alexa_say(edit1 + 'is' + str(ans))

        # elif '-' in command:
        #     edit = command.replace('what is ', '')
        #     edit1 = edit.removeprefix(' ')
        #     edit = edit1.replace('- ', '')

        #     question = edit.split(' ')
        #     inint = list(map(int, question))
        #     ans = inint[1] - sum(inint[1:])
        #     print(ans)
        #     alexa_say(edit1 + 'is' + str(ans))

    elif 'send a message on whatsapp' in command or 'send a whatsapp message' in command:
        alexa_say('Please Write The Phone Number')
        phNum = str(input('Write The Phone Number: '))
        phNum = '+91 ' + phNum

        alexa_say('Please Write What The Message Should Be')
        msg = str(input('Write What Message You Want To Send To Them: '))

        alexa_say('Please Write At What Hours It Should Be Sended')
        timeHrs = int(input('Write At What Hour Time You Want To Send Message : '))

        alexa_say('Please Write At What Minutes It Should Be Sender')
        timeMins = int(input('Write At What Minutes Time You Want To Send Message: '))

        # alexa_say('Please Fill Up All The Necessary Details')

        alexa_say('Message Will Now Be Deliver At The Given Time')
        sendMsg(phNum, timeHrs, timeMins, msg)

        # if 'notify me to' in command:
        #     msg = command.replace('notify me to', '')


run_alexa()
