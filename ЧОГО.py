
from tkinter import *
import random
import json
app=Tk()
pelmenchiku={}
app["bg"]="#F24624"
global SLOVA
color1="#779FBF"
color2="#700AFF"
color3="#020330"
color4="#009CFF"
color5="#596F7D"
colortowinner="#CF1313"
colortodefeated="#1368CF"
colortodumpling="#F2BE00"
mylives=3
mycoins=0
root=Tk()
user_name=''
root.geometry("2500x2500")
ent=Entry()
ent.pack()
def funkcija_XEXEEXEXEXE():
    global user_name
    WHATTHEHEEEEELOOMG=-1
    user_name=ent.get()
    print(user_name)
    print("если хочеш депнуть в каз то бепни все ну а если есть до деп то кинь еще а последний деп оставь вить окуп ждет все окупиться поверь еще еще!   (ГИМН КАЗИНО)")
makarena=Button(bg="red",fg="white",height=5,width=20,font=1000000000000000000,command=funkcija_XEXEEXEXEXE)
makarena.place(x=300,y=400)
root.mainloop()
name="бобрик"
LAVRENIK=None
def desk():
    shtoeto=""
    for i in data:
        print(i["name"],i["mycoins"])
        shtoeto+=f"{i["name"]} --- {i["mycoins"] } балів\n"
    global kria
    kria=Label(text=shtoeto,bg="white",fg="black",font=1000000000000000000000000)
    kria.place(x=130,y=50)
def q(number):
    print(number)
    G = random.choice(["камінь","ножниці","папір"])
    global mylives,mycoins,LAVRENIK,i,data,kria
# I["text"]="Вибір комп'ютера:"+G
    # if G=="папір" and SLOVA["text"]=="ножниці":
    #     I["text"]="Вибір комп'ютера:папір ваш вибір ножниці"
    #     D["text"]="гравець преміг!!!"
    # if G=="камінь" and SLOVA["text"]=="папір":
    #     I["text"]="Вибір компютера: камінь ваш вибір: папір "
    #     D["text"]="гравець преміг!!!"
    # if G=="ножниці" and SLOVA["text"]=="камінь":
    #     I["text"]="Вибір комп'ютера: ножниці ваш вибір: камінь "
    #     D["text"]="гравець преміг!!!"
    # if SLOVA["text"]=="камінь" and G=="ножниці":
    #     I["text"] = "Вибір комп'ютера:ножниці ваш вибір папір"
    #     D["text"] = "комп'ютер переміг!!"
    # if SLOVA["text"]=="камінь" and G=="папір":
    #     I["text"] = "Вибір компютера: папір ваш вибір: камінь"
    #     D["text"]="комп'ютер переміг!!"
    # if SLOVA["text"]=="ножниці" and G=="камінь":
    #     I["text"] = "Вибір комп'ютера: камінь ваш вибір: ножниці"
    #     D["text"] = "комп'ютер переміг!!"
    # if SLOVA["text"]=="" and G=="камінь":
    #     D["text"]="нічія"
    # if SLOVA["text"]=="ножниці" and G=="ножниці":
    #     D["text"]="нічія"
    # if SLOVA["text"]=="папір" and G=="папір":
    #     D["text"]="нічія"
    my_choice = number
    print(my_choice,"***")
    if my_choice=='камінь':
        if G=='папір':
            D['text']="комп'ютер виграв"
            mylives-=1
            app["bg"]="#99CC3D"
            D["bg"]=colortodefeated
            with open("scrore.json", "r", encoding="utf-8") as file:
                A = json.load(file)
                ent = Entry()
            with open("scrore.json", "w", encoding="utf-8") as file:
                A = json.load(file)
                ent = Entry()
            ent.pack()
        elif G =='ножниці':
            D['text'] = 'користувач виграв'
            mycoins+=100
            D["bg"]=colortowinner
            app["bg"]="#EB9C60"
        else:
            D["text"] = "нічія"
            mycoins+=50
            D["bg"]=colortodumpling
            app["bg"]="#376BDB"
    elif my_choice=="ножниці":
        if G=="камінь":
            D['text'] = "комп'ютер виграв"
            mylives-=1
            app["bg"] = "#2082A1"
            D["bg"]=colortodefeated
        elif G == 'папір':
            D['text'] = 'користувач виграв'
            mycoins+=100
            app["bg"] = colortowinner
            D["bg"]=colortowinner
        else:
            D["text"] = "нічія"
            mycoins+=50
            app["bg"] = colortodumpling
            D["bg"]=colortodumpling
    elif my_choice=="папір":
        if G=="ножниці":
            D['text'] = "комп'ютер виграв"
            mylives-=1
            app["bg"] = "#8BCCC8"
            D["bg"]=colortodefeated
        elif G == 'камінь':
            D['text'] = 'користувач виграв'
            mycoins+=100
            app["bg"] = colortowinner
        else:
            D["text"] = "нічія"
            mycoins+=50
            app["bg"] = "#376BDB"
            D["bg"]=colortodumpling
    I['text'] = f"Вибір комп'ютера: {G} ваш вибір: {my_choice}"
    if D['text'] == "нічія":
        D["bg"] = colortodumpling
    elif D['text'] =='користувач виграв':
        D["bg"] = colortowinner
    elif D['text'] =="комп'ютер виграв":
        D["bg"] = colortodefeated
    def exit():
        global LAVRENIK
        app.destroy()
        app1=Tk()
        app1.geometry("500x500")
        pelmen=Label(text=f"ви програли😣 ваші бали {mycoins}",bg="white",fg="black",height=5,width=25,font=10000000000000000000000000000000000000000000)
        pelmen.place(x=600,y=150)
        LAVRENIK=Button(text="Таблиця",bg="white",fg="black",height=5,width=30,font=1000,command=desk)
        LAVRENIK.place(x=570,y=350)
        app1.mainloop()
    if mylives==0:
        pelmenchiku["name"]=A
        pelmenchiku["mycoins"] = mycoins
        with open("my.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            data.append(pelmenchiku)
            with open("my.json", "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            exit()
    # I['text'] = "Вибір комп'ютера: " + G +" ваш вибір: "+ my_choice
def q1():
    q("камінь")
    SLOVA["text"]="камінь"
def q2():
    q("ножниці")
    SLOVA["text"]="ножниці"
def q3():
    q("папір")
    SLOVA["text"]="папір"
A=Button(text="камінь",fg="black",bg=color1,height=5,width=25,font=10000000000000000000000000000000000000,command=q1)
A.place(x=283,y=570)
B=Button(text="ножниці",fg="black",bg=color2,height=5,width=25,font=10000000000000000000000000000000000000,command=q2)
B.place(x=633,y=570)
C=Button(text="папір",fg="white",bg=color3,height=5,width=25,font=10000000000000000000000000000000000000,command=q3)
C.place(x=983,y=570)
D=Label(text="",fg="black",bg=color5,height=7,width=35,font=10000000000000000000000000000000000)
D.place(x=610,y=290)
I=Label(text="Вибір комп'ютера:",fg="black",bg=color4,height=10,width=50,font=1)
I.place(x=519,y=10)
SLOVA=Label(text="",fg="black",bg=color5,height=15,width=15)
SLOVA.place(x=1000,y=1000)
app.mainloop()