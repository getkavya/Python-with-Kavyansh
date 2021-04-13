import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id  )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


    def wishme():
        hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")

    else:
        print("Good Morning!")

        speak("I am Jarvis. Please tell me how may I help you")

if __name__ == " __main__":
    speak("kavyansh is a good boy")