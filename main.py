import speech_recognition as sr
import os
import webbrowser
import openai
import pyttsx3
from config import apikey
import datetime
import random

chatStr = ""
openai.api_key = apikey

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Harry: {query}\nJarvis: "
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=chatStr,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
    except Exception as e:
        say("Sorry, I encountered an error while processing your request.")
        return "Error"

def ai(prompt):
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")
        with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except Exception as e:
        say("Sorry, I encountered an error while processing your request.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Some Error Occurred. Sorry from Jarvis")
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Welcome to Jarvis A.I")
    while True:
        query = takeCommand().lower()
        
        sites = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"]
        ]
        
        for site in sites:
            if f"open {site[0]}" in query:
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        
      

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes")

       
        elif "using artificial intelligence" in query:
            ai(prompt=query)

        elif "jarvis quit" in query:
            say("Goodbye, sir!")
            break

        elif "reset chat" in query:
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)


