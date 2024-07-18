import pyttsx3
import speech_recognition as sr

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Corrected the attribute name
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except sr.UnknownValueError:
            print("Sorry, I did not understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""
        return query

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis AI")
    while True:
        text = takeCommand()
        if text:
            say(text)


