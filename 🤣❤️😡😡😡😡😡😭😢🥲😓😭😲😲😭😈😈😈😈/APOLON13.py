from tkinter import *
import random
import json
oy=None
KABAN=None
KABAN1=None
tralalelotralala=None
logino="EZZ"
parolo1="NOOB"
JASTOMUWSYAAAAAAAAAAAAA=Tk()
LOGIN = Entry(bg='blue',font="4000000000000000000000000000000000000000000000000000000000000000")
LOGIN.place(x=530, y=40,height=50,width=500)
PLACELOGIN=Label(text="Впешіть login: ----> ",font="4000000000000000000000000000000000000000000000000000000000000000",height=4, width=30)
PLACELOGIN.place(x=170,y=20)
PLACEPAROL=Entry(bg="yellow",font="4000000000000000000000000000000000000000000000000000000000000000")
PLACEPAROL.place(x=530,y=300,height=50,width=500)
PLACEPAROOOOOOOL=Label(text="Впешіть password: ---->",font="4000000000000000000000000000000000000000000000000000000000000000",height=4,width=30)
PLACEPAROOOOOOOL.place(x=170,y=280)
def POVESTOCHKA_W_JSONEHEEHELOL(data,logino):
    for i in data:
        print(i)
        if i["loginoo"]==logino:
            print("хехе знайшли абобуса")
            return True
    return False
# app=Tk()
# kaban=Entry(bg='blue',font="4000000000000000000000000000000000000000000000000000000000000000")
# kaban.place(x=530, y=40, height=50, width=500)
# abobaaa=Entry(bg="yellow",font="4000000000000000000000000000000000000000000000000000000000000000")
# abobaaa.place(x=530, y=300, height=50, width=500)
# kaban2=kaban.get()
# abobaaa2=abobaaa.get()
# app.mainloop()
# def aboba(data,logino):
#     app=Tk()
#     kaban=Entry(bg='blue',font="4000000000000000000000000000000000000000000000000000000000000000")
#     kaban.place(x=530, y=40, height=50, width=500)
#     abobaaa=Entry(bg="yellow",font="4000000000000000000000000000000000000000000000000000000000000000")
#     abobaaa.place(x=530, y=300, height=50, width=500)
#     kabaaan2=kaban.get()
#     abobaaa2=abobaaa.get()
#     for i in data:
#         print(i)
#         if i["loginoo"] == logino:
#             app.destroy()
#             app.destroy()
def onetjakriaknuw():
    global oy
    oy=Tk()
    Label1=Label(bg='blue',font="4000000000000000000000000000000000000000000000000000000000000000")
    Label1.place(x=60, y=40, height=50, width=500)
    Label2 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label2.place(x=60, y=120, height=50, width=500)
    Label3 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label3.place(x=60, y=200, height=50, width=500)
    Label4 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label4.place(x=60, y=280, height=50, width=500)
    Label5 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label5.place(x=60, y=360, height=50, width=500)
    Label6 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label6.place(x=60, y=440, height=50, width=500)
    Label7 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label7.place(x=60, y=520, height=50, width=500)
    Label8 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label8.place(x=60, y=600, height=50, width=500)
    Label9 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    Label9.place(x=60, y=680, height=50, width=500)
    notiatoczka=Button(text="CDELAJTE NOTATOCHKU",fg="black", bg="red", height=4, width=30, font=100,command=kaban_propav)
    notiatoczka.place(x=1200,y=670)
    oy.mainloop()
def fly_to_json(tralalelotralala):

    with open("jason.json", "r", encoding="utf-8") as file:
        data = json.load(file)
def NENAVIDRZYYYY():
    global KABAN,KABAN1
    tralalelotralala=KABAN1.get()
    print(tralalelotralala)
        # data.append(KABAN_text)
        # KABAN1_text=KABAN1.get()
        # print(KABAN1_text)
        # data.append(KABAN1_text)
    KABAN1=Entry(bg='red',font="4000000000000000000000000000000000000000000000000000000000000000")
    KABAN1.place(x=530, y=120, height=50, width=500)
    shajtanknopka=Button(text="import to json",fg="black",bg="purple", height=4, width=30, font=100,command=lambda:fly_to_json(tralalelotralala))
    shajtanknopka.place(x=500,y=500)

def kaban_propav():
    global oy,KABAN
    oy.destroy()
    abobaa=Tk()
    KABAN=Entry(bg='blue',font="4000000000000000000000000000000000000000000000000000000000000000")
    KABAN.place(x=530, y=40,height=50,width=500)
    kla=Button(text="SKUF", fg="black",bg="purple", height=4, width=30, font=100,command=NENAVIDRZYYYY)
    kla.place(x=1000,y=500)
    abobaa.mainloop()
def cheap_user(logino,parolo):
    with open("../kapustochka.json", "r", encoding="utf-8") as file:
        data=json.load(file)
        for i in data:
            if i["loginoo"] == logino and i["paroloo"]==parolo:
                return True
        return False
def funkcija_skadoosh():
    sekret_text = button_for_sekret_text.get()
    print(sekret_text)
    if sekret_text=="советский союз":
        print("https://youtu.be/aWt9bGilBa0?si=G4z65iXgsGQ8pKLx")
    elif sekret_text=="you get rickrolled":
        print("https://youtu.be/dQw4w9WgXcQ?si=FnoYu5u_x-tg6GEF")
    elif sekret_text=="crabiki":
        print("https://youtu.be/cE0wfjsybIQ?si=40IzgvQoCcAwS4FR")
    elif sekret_text=="ух емма ето шо такое?":
       print("https://youtu.be/pVHKp6ffURY?si=XcL4G4JkrYc1VUsC")
    elif sekret_text=="BUSI BUSI?":
        print("https://youtu.be/BL4P7QGLZ4M?si=VWpCH-Kq_UC2_DdZ")
    elif sekret_text=="ШРЕК ":
        print("https://youtu.be/vXYVfk7agqU?si=OYw1bfxwXasUbg0L")
    elif sekret_text=="топ 1 фанк":
        print("https://youtu.be/UcRtFYAz2Yo?si=p1GyEbDYs19WKvBF")
    elif sekret_text=="SUIII":
        print("https://youtu.be/8EMy_ZGAdU0?si=6N_1SIP6_6QvjRGj")
    elif  sekret_text=="LIVSEY":
        print("https://youtu.be/UcRtFYAz2Yo?si=woEiLAAy4N62nRaM")
    elif sekret_text=="ммм какой балдеж":
        print('https://youtu.be/wu4NYMmk8pk?si=mLcy4m0aa9dAxL91')
    elif sekret_text=="pedrooo":
        print("https://youtu.be/UgAwZ1aQFJc?si=FtZhyR_gYzhCJoDl")
    logino=LOGIN.get()
    parolo=PLACEPAROL.get()
    with open("../kapustochka.json", "r", encoding="utf-8") as file:
        data=json.load(file)

    FOUNDFOOTAGE=POVESTOCHKA_W_JSONEHEEHELOL(data=data,logino=logino)
    if FOUNDFOOTAGE==True:
        print("свинокабанчик")
        czujesz_kiegosz_toimordkasiecziszy=cheap_user(logino=logino,parolo=parolo)
        if czujesz_kiegosz_toimordkasiecziszy==True:
            print("heloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo net")
            JASTOMUWSYAAAAAAAAAAAAA.destroy()
            onetjakriaknuw()
        else:
            print("Я ЗНАЮ ТИ ЧІТЄР ЯКИЙ ХОЧЕ ХАЦКНУТИ МІЙ КОМП ПРОВАЛЮЙ!!!!")
    else:
        print("БАБАК ТИ ЖАРЕНИЙ")
        data.append({"SEKRETO":sekret_text,"paroloo":parolo,"loginoo": logino})
        # data.append({)
        # data.append({})
        with open("../kapustochka.json", "w", encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=4)
            JASTOMUWSYAAAAAAAAAAAAA.destroy()
KNOPKA=Button(text="confirm :P ",bg="purple",height=4, width=30, font=100,command=funkcija_skadoosh)
KNOPKA.place(x=140,y=590)
button_for_sekret_text=Entry(font="4000000000000000000000000000000000000000000000000000000000000000")
button_for_sekret_text.place(x=530,y=560,height=50,width=500)
# with open("../kapustochka.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# POVESTOCHKA_W_JSONEHEEHELOL(data=data,parolo="A NOBIARAAA",logino="ez")
JASTOMUWSYAAAAAAAAAAAAA.mainloop()
