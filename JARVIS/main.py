import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def process_command(c):
    if "open google"in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif"open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith("play "):
        song = c.lower()[5:].strip()
        if song in musiclibrary.Music:
            link = musiclibrary.Music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")

if __name__ == "__main__":
    speak("initializing jarvis")
    while True:
        r = sr.Recognizer()


        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening..")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            word = r.recognize_google(audio)
            if( word.lower() == "jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                    print("jarvis active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    process_command(command)

        except Exception as e:
            print("Error: {0}".format(e))
 

   

        
    