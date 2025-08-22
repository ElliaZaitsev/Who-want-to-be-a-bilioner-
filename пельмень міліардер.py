import json
import random
from sys import set_asyncgen_hooks
from tkinter import *
with open("pelmen.json", "r", encoding="utf-8") as file:
    data = json.load(file)
NET=["100000","200000","300000","400000","500000","600000","700000","800000","900000","1000000"]
PELMEN="#F54927"
PELEMEN1="#3383AB"
PELEMEN2="#A4C240"
PELMEN3="#B8251F"
PELMEN4="#8E9638"
PELEMEN5="#4E7E8A"
PELMEN6="#2BA5C4"
PELMEN7="#781111"
PELMEN8="#111A78"
PELMEN9="#A67F26"
PELEMEN10="#3A6B52"
PELMEN11="#3A456B"
PELMEN12="#4D5234"
PELMEN13="#367A65"
i=0
global niam,playedadvice,update_question
def advice50_advice50():
    podskazka50na50["state"]="disabled"
    answer1["state"] = "disabled"
    answer2["state"] = "disabled"
    answer3["state"] = "disabled"
    answer4["state"] = "disabled"
    answer5["state"] = "disabled"
    answer6["state"] = "disabled"
    question=data[i]
    answer_number = question['answers'].index(question['correctanswer'])
    while True:
        PEELMEEN = random.randint(0, 5)
        if PEELMEEN!=answer_number:
            break
    while True:
        numnumnum = random.randint(0, 5)
        if numnumnum!=PEELMEEN and numnumnum!=answer_number:
            break

    while True:
        answers = [answer1, answer2, answer3, answer4, answer5, answer6]

        for i in range(6):
            if numnumnum == i or answer_number == i or PEELMEEN == i:
                answers[i]["state"] = "normal"

def playeradviec():
    podskazkaporada["state"] = "disabled"
    answer1["state"] = "disabled"
    answer2["state"] = "disabled"
    answer3["state"] = "disabled"
    answer4["state"] = "disabled"
    answer5["state"] = "disabled"
    answer6["state"] = "disabled"
        # podskazkaporada["state"]="disabled"
        question = data[i]
        answer_number = question['answers'].index(question['correctanswer'])
        if answer_number == 0:
            answer1["state"] = "normal"
        elif answer_number == 1:
            answer2["state"] = "normal"
        elif answer_number == 2:
            answer3["state"] = "normal"
        elif answer_number == 3:
            answer4["state"] = "normal"
        elif answer_number == 4:
            answer5["state"] = "normal"
        elif answer_number == 5:
            answer6["state"] = "normal"
def getmoney():
    app.destroy()
    theend=Tk()
    yougetmoney=Label(text=f"ви забрали всі гроші! і заробили {i*10000000} won!",bg=PELMEN7,fg="black",height=4,width=62,font=100)
    yougetmoney.place(x=465,y=300)
def rightanswer(Button):
    global i,pelmenchiku
    print(Button['text'])
    if Button["text"]==data[i]["correctanswer"]:
        question["text"]="ПРАВИЛЬНО!"
        answers["text"]="відповідь 1/10"
        cashprize["text"]="100.000"
        i+=1
        cashprize["text"]=i*10000000
        answers["text"] = f"відповідь {i}/{len(data)}"
    if i == len(data):
        app.destroy()
        pelmencik = Tk()
        AC130GUNSHIPHERCULES = Label(text=f"easy win i play these ganes before😎😎😎 and {i * 10000000} 🤑🤑🤑", bg=PELMEN7,fg="black", height=4, width=62, font=100)
        AC130GUNSHIPHERCULES.place(x=465, y=300)
    app.mainloop()
    print("КАБУМ!")
git stash
    # else:
    #     update_question()
# app1 = Tk()
# AAAAA = Label(text="печельно ето очень печально:(", bg="white", fg="black", height=4, width=30, font=100)
# AAAAA.place(x=573, y=300)
# BBBBB = Label(text=f"ви б могли виграти {NET[i]} ви відповіли на {answerforanswer}", bg="white", fg="black",font=1000000000000000000000)
# BBBBB.place(x=503, y=500)
def update_question():
    global timer, cashprize, getallmoney, answers, question, answer1, answer2, answer3, answer4, answer5, answer6, cashprize
    global data
    question["text"] = data[i]["name"]
    answer1["text"] = data[i]["answers"][0]
    answer2["text"] = data[i]["answers"][1]
    answer3["text"] = data[i]["answers"][2]
    answer4["text"] = data[i]["answers"][3]
    answer5["text"] = data[i]["answers"][4]
    answer6["text"] = data[i]["answers"][5]
    answer1["state"] = "normal"
    answer2["state"] = "normal"
    answer3["state"] = "normal"
    answer4["state"] = "normal"
    answer5["state"] = "normal"
    answer6["state"] = "normal"
app = Tk()
app["bg"] = "#1157A6"
        # elif Button["text"] != data[i]["correctanswer"]:
        #         question["text"] = "НЕПРАВИЛЬНО!"
        # cashtext = cashprize["text"]
        # answerforanswer = answers["text"]
    # app.destroy()
timer = Label(text="", bg=PELMEN13, fg="blue", height=5, width=15)
timer.place(x=710, y=20)
cashprize = Label(text="дєнужка:)", fg="black", bg=PELEMEN1, height=5, width=30, font=1000)
cashprize.place(x=1100, y=20)
podskazka50na50 = Button(text="підсказка 50 на 50", fg="black", bg=PELEMEN2, height=5, width=25, font=1000,command=advice50_advice50)
podskazka50na50.place(x=100, y=170)
podskazkaporada = Button(text="порaда гравця", fg="black", bg=PELMEN3, height=5, width=25, font=1000,command=playeradviec)
podskazkaporada.place(x=623, y=170)
getallmoney = Button(text="заберіть виграні гроші", fg="black", bg=PELMEN4, height=5, width=25, font=1000,command=getmoney)
answers = Label(text="відповідь 0/10", bg="black", fg=PELEMEN5, height=5, width=30, font=1000)
answers.place(x=100, y=20)
getallmoney.place(x=1150, y=170)
question = Label(text=data[i]["name"], fg="black", bg=PELMEN6, height=4, width=113, font=100)
question.place(x=100, y=355)
answer1 = Button(text=data[i]["answers"][0], fg="black", bg=PELMEN7, height=4, width=30, font=100,command=lambda: rightanswer(answer1))
answer1.place(x=120, y=490)
answer2 = Button(text=data[i]["answers"][1], fg="black", bg=PELMEN8, height=4, width=30, font=100,command=lambda: rightanswer(answer2))
answer2.place(x=120, y=650)
answer3 = Button(text=data[i]["answers"][2], fg="black", bg=PELMEN9, height=4, width=30, font=100,command=lambda: rightanswer(answer3))
answer3.place(x=595, y=490)
answer4 = Button(text=data[i]["answers"][3], fg="black", bg=PELEMEN10, height=4, width=30, font=100,command=lambda: rightanswer(answer4))
answer4.place(x=595, y=650)
answer5 = Button(text=data[i]["answers"][4], fg="black", bg=PELMEN11, height=4, width=30, font=100,command=lambda: rightanswer(answer5))
answer5.place(x=1070, y=650)
answer6 = Button(text=data[i]["answers"][5], fg="black", bg=PELMEN12, height=4, width=30, font=100,command=lambda: rightanswer(answer6))
answer6.place(x=1070, y=490)
app.mainloop()