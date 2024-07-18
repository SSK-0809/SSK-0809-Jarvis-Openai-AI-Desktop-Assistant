import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis AI")

