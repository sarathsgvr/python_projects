import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import subprocess
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is %s" %Time)

def date():
    Year = int(datetime.datetime.now().year)
    Month = int(datetime.datetime.now().month)
    Day = int(datetime.datetime.now().day)
    speak("Today's date is %d \n %d \n %d" % (Day, Month, Year))

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        speak("Hello!, Good Morning!")
    elif hour >= 12 and hour <= 16:
        speak("Hello!, Good Afternoon")
    else:
        speak("Hello!, Good Evening")
    speak("I am Jarvis, AI assistant of Mr. Sarath")
    #time()
    #date()
    speak("Jarvis at your service \n How can I help you?")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server = ehlo()
    server.starttls()
    server.login('sarathsgvr@gmail.com', '######')
    server.sendmail('sarathsgvr@gmail.com', to, content)
    server.close()


def listenvoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = listenvoice().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak('searching')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif ('send email' or 'sent email') in query:
            try:
                speak("What is the content?")
                content = listenvoice()
                speak("Please tell me the to address")
                to = listenvoice()
                sendemail(to, content)
                speak("Email successfully sent")

            except Exception as e:
                print(e)
                speak("Sorry, unable to send the email")
        
        elif 'search in chrome' in query:
            try:
                speak('What should I search')
                chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                search = listenvoice()
                wb.get(chromepath).open_new_tab(search)
            except Exception as e:
                print(e)
                speak("Sorry I couldn't understand")

        #elif 'logout' in query:
         #   speak("Signing out")
          #  os.system("shutdown -l")

        elif 'lock' in query:
            speak('Locking the system')
            cmd='rundll32.exe user32.dll, LockWorkStation'
            subprocess.call(cmd)
            quit()

        #elif 'shutdown' or 'poweroff' in query:
         #   speak("shutting down system")
          #  os.system("shutdown /s /t 1")

        #elif 'restart' in query:
         #   speak("restarting system")
          #  os.system("shutdown /r /t 1")

        elif 'remember' in query:
            speak('Tell me, what should I remeber?')
            data = listenvoice()
            speak("You said to remember that" +data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif ('who' or 'why' or 'how' or 'when' or 'what') in query:
            #os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
            search = listenvoice()
            #speak('searching...')
            #speak("Showing you some results")
            wb.open_new(search)

        elif 'thank you' in query:
            speak("Good bye, Have a nice day")
            quit()
        





    



