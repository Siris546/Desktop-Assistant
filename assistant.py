import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
# import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#you can change voice by changing the array index of voices 0 is for guy and 1 is for girl.
# print(voices[2].id)
engine.setProperty('voice', voices[2].id)

def speak(speech):
    engine.say(speech)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning mister Siris")
    elif hour>=12 and hour<18:
        speak("Good Afternoon mister Siris")
    else:
        speak("Good Evening mister Siris")
    
    speak("Give me your command.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print("Something went wrong, Please speak again.")
        return "None"
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        try:
            if "wikipedia" in query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences = 2)
                print(results)
                speak(results)

            elif "open youtube" in query:
                webbrowser.open("youtube.com")

            elif "open google" in query:
                webbrowser.open("google.com")

            elif "open stackoverflow" in query:
                webbrowser.open("stackoverflow.com")

            elif "play music" in query:
                music_folder = "C:\\Users\\user\\Music"
                songs = os.listdir(music_folder)
                print(songs)
                randomSong= random.randint(1,len(songs)+1)
                print(songs[randomSong])
                os.startfile(os.path.join(music_folder, songs[randomSong]))
            
            elif "open code" in query:
                codepath = 'C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(codepath)

            # elif "email siris" in query:
            #     try:
            #         speak("What should i say")
            #         content = takeCommand()
            #         tonaruto = "narutohero12345@gmail.com"
            #         sendEmail(tonaruto,content)
            #         speak("Email has been sent.")
            #     except:
            #         print(f"{e} : Something wrong occured there.")

            elif "quit the program" in query:
                exit()

        except Exception as e:
            print(f"{e}: An error has occured")