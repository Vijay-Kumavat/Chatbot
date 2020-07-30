from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp  #pyttsx3
import speech_recognition as s
import threading
import tkinter
from PIL import Image, ImageTk
from _tkinter import *

engine= pp.init()

voices = engine.getProperty('voices')
print(voices)
engine.setProperty('vocies',voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

chatbot = ChatBot("My Bot")

conversation = [
    'Hello',
    'Hi there !!!',
    'What is your name ?',
    'My name is Python , I created by Kumavat vijay',
    'thank you',
    'Bye',
    'Cu soon'

]
#
trainer = ListTrainer(chatbot)
#
# #now trainner the bot with the help of trainer
trainer.train(conversation)

# answer = chatbot.get_response("Thank you")
#
# print(answer)

# print("Talk to a Bot")
# while True:
#     query=input()
#     if query == 'exit':
#         break
#     answer = chatbot.get_response(query)
#     print("Bot : " ,answer)

main = Tk()
main.geometry("600x600")
main.title("Kumavat.Bot")

# Image.open("lenna.jpg")
# print(tkinter.TkVersion)
img = PhotoImage(file="1.gif")

# image = Image.open("bot1.jpg")
# photo = ImageTk.PhotoImage(image)
photoL = Label(main, image=img)

photoL.pack(pady=5)

#take Query function for speech_recognition
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("bot is trying to listing to you")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not Recognized")

def ask_from_bot():
    query=textF.get()
    answer_from_bot=chatbot.get_response(query)
    msgs.insert(END,"You : "+ query)
    msgs.insert(END,"Bot : "+ str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=15,yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=15)

frame.pack()

# create the field
textF = Entry(main, font=("Verdana", 12))
textF.pack(fill=X, padx=50,pady=10)

btn = Button(main, text="Ask from Bot", font=("Verdana", 13), command=ask_from_bot)
btn.pack()

#creating a fuction for Ask from bot

def enter_function(event):
    btn.invoke()

#going to bind main window with enter key...
main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)

t .start()

main.mainloop()
