import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour >= 12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am ani sir. Please tell me how may I help you")

def takeCommand():
    # it take microsoft input from the our and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")
    except Exception as e:
        # print(e)
        print("Say thet again please...")
        return "None"
    return query
    
         

if _name_ == "_main_":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia'in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stack overflow" in query:
            webbrowser.open("satckoverflow.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\\Admin\\Downloads\\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))