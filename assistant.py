import pyttsx3
import speech_recognition as sr
from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv() 

#creating an env file that holds the api key
#api key syntax OPENAI_API_KEY = "your api key"
client = OpenAI(api_key=os.environ.get(".env"))

#setting the voice for text to speech
#you can change the voice by setting the value in voices[]
#voices[1] if a girl voice voices[0] for boy
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',150)


#calling the aiAssistant function
#you must set first your api key to the env file to be able use this function
def aiAssistant(promp):
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  temperature=1,
  max_tokens=50,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": promp}
  ]
    )

  print(response.choices[0].message.content)
  engine.say(f"you ask me about {promp.replace("assistant", "")} {response.choices[0].message.content}")
  engine.runAndWait()
    


#main function
def main():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            print("recognizing...")
            promp = r.recognize_google(audio)
            if "assistant" in promp:
                aiAssistant(promp)
        except Exception as e:
            print("Say that again please...")
        
        

main()