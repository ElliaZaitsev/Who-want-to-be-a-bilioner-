from tkinter import *
import random
import json
nothing="..."
shajtanknopka=None
damiorgrr=None
damiorgrr1=None
oy = None
KABAN = None
KABAN1 = None
tralalelotralala = None
text_kaban = None
abobaa=None
logino = None
parolo1 = "NOOB"
JASTOMUWSYAAAAAAAAAAAAA = Tk()
from tkinter import *
from PIL import Image, ImageTk  # Import Image and ImageTk

image_path = "e9cadc132e1444dca238426a9ec1aea9.jpg"
original_image = Image.open(image_path)
photo = ImageTk.PhotoImage(original_image)
label = Label(JASTOMUWSYAAAAAAAAAAAAA,image=photo)
label.image = photo
label.pack()
LOGIN = Entry(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
LOGIN.place(x=530, y=40, height=50, width=500)
PLACELOGIN = Label(text="Впешіть login: ----> ",
                   font="4000000000000000000000000000000000000000000000000000000000000000", height=4, width=30)
PLACELOGIN.place(x=170, y=20)
PLACEPAROL = Entry(bg="yellow", font="4000000000000000000000000000000000000000000000000000000000000000")
PLACEPAROL.place(x=530, y=300, height=50, width=500)
PLACEPAROOOOOOOL = Label(text="Впешіть password: ---->",
                         font="4000000000000000000000000000000000000000000000000000000000000000", height=4, width=30)
PLACEPAROOOOOOOL.place(x=170, y=280)

def POVESTOCHKA_W_JSONEHEEHELOL(data, logino):
    for i in data:
        print(i)
        if i["loginoo"] == logino:
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
def KABYYYYYYM():
    global damiorgrr1
    damiorgrr1(text="sho?")
def onetjakriaknuw():
    global oy
    oy = Tk()
    image_path = "channels4_profile.jpg"
    original_image = Image.open(image_path)
    photo = ImageTk.PhotoImage(original_image)
    label = Label(oy,image=photo)
    label.image = photo
    label.pack()
    with open("jason.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    bb=0
    for i in data:
        print(logino,'****')
        if i["автор"]==logino:
            damiorgrr=Label(text=i['what we need to do?'],fg="black", bg="blue", height=4, width=60, font=100)
            bb+=1
            damiorgrr.place(x=50,y=20+100*bb)
            damiorgrr1 = Label(text=i['dead-line'], fg="black", bg="blue", height=4, width=60, font=100)
            damiorgrr1.place(x=850, y=20 + 100 * bb)
            damiorgrr2=Label(text="що нам потрібно зробити?",fg="white", bg="purple", height=2, width=30, font=100)
            damiorgrr2.place(x=50,y=50)
            damiorgrr3 = Label(text="dead-line", fg="white", bg="purple", height=2, width=30, font=100)
            damiorgrr3.place(x=1177, y=50)
            damiorgrr5=Button(text="    🗑️",bg="red",fg="black",
                            height=2, width=5, font=100,command=lambda i=i:babax(note=i))
            damiorgrr5.place(x=750,y=135+(bb-1)*100)
    def babax(note):
        global damiorgrr, data, i

        with open("jason.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            data.remove(note)
        with open("jason.json", "w", encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
        # damiorgrr6 = Button(text="    🗑️",bg="red", fg="black", height=2, width=5, font=100,command=KABYYYYYYM)
        # damiorgrr6.place(x=750, y=230)
    # Label1 = Label(text=data,bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label1.place(x=60, y=40, height=50, width=500)
    # Label2 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label2.place(x=60, y=120, height=50, width=500)
    # Label3 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label3.place(x=60, y=200, height=50, width=500)
    # Label4 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label4.place(x=60, y=280, height=50, width=500)
    # Label5 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label5.place(x=60, y=360, height=50, width=500)
    # Label6 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label6.place(x=60, y=440, height=50, width=500)
    # Label7 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label7.place(x=60, y=520, height=50, width=500)
    # Label8 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label8.place(x=60, y=600, height=50, width=500)
    # Label9 = Label(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    # Label9.place(x=60, y=680, height=50, width=500)
    notiatoczka = Button(text="створіть нову нотатку", fg="black", bg="red", height=4, width=30, font=100,
                         command=kaban_propav)

    notiatoczka.place(x=1200, y=670)
    with open("jason.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for i in data:
        print(data)
    oy.mainloop()
def fly_to_json():
    global KABAN, KABAN1,a,b,shajtanknopka
    print_text=Label(text="натисніть <<МОЇ НОТАТКИ>> ",fg="black", bg="green", height=4, width=30, font=100,)
    print_text.place(x=110,y=400)
    shajtanknopka['state'] = "disabled"
    with open("jason.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    a = KABAN.get()
    b = KABAN1.get()
    data.append({"what we need to do?":a,"dead-line":b,"автор":logino})
    print(a, "\n", b)
    with open("jason.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
def RESTARTO50PROCENTO():
    global abobaa
    abobaa.destroy()
    onetjakriaknuw()

def NENAVIDRZYYYY():
    global KABAN, KABAN1,shajtanknopka
    # data.append(KABAN_text)
    # KABAN1_text=KABAN1.get()
    # print(KABAN1_text)
    # data.append(KABAN1_text)
    KABAN1 = Entry(bg='red', font="4000000000000000000000000000000000000000000000000000000000000000")
    KABAN1.place(x=530, y=120, height=50, width=500)
    shajtanknopka = Button(text="зберегти", fg="black", bg="purple", height=4, width=30, font=100,
                           command=lambda: fly_to_json())
    # KABAN1=text_kaban.get()
    shajtanknopka.place(x=600, y=500)
    shajtanknopka1=Button(text="мої нотатки",bg="purple",fg="black",height=4, width=30, font=100,command=RESTARTO50PROCENTO)
    shajtanknopka1.place(x=110,y=500)


def kaban_propav():
    global oy, KABAN,abobaa
    oy.destroy()
    abobaa = Tk()
    image_path = "maxresdefault.jpg"
    original_image = Image.open(image_path)
    photo = ImageTk.PhotoImage(original_image)
    label = Label(abobaa, image=photo)
    label.image = photo
    label.pack()
    KABAN = Entry(bg='blue', font="4000000000000000000000000000000000000000000000000000000000000000")
    KABAN.place(x=530, y=40, height=50, width=500)
    kla = Button(text="натисніть щоб вписати dead-line", fg="black", bg="purple", height=4, width=30, font=100, command=NENAVIDRZYYYY)
    kla.place(x=1100, y=500)
    abobaa.mainloop()


def cheap_user(logino, parolo):
    with open("../kapustochka.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        for i in data:
            if i["loginoo"] == logino and i["paroloo"] == parolo:
                return True
        return False


def funkcija_skadoosh():
    sekret_text = button_for_sekret_text.get()
    print(sekret_text)
    if sekret_text == "советский союз":
        print("https://youtu.be/aWt9bGilBa0?si=G4z65iXgsGQ8pKLx")
    elif sekret_text == "you get rickrolled":
        print("https://youtu.be/dQw4w9WgXcQ?si=FnoYu5u_x-tg6GEF")
    elif sekret_text == "crabiki":
        print("https://youtu.be/cE0wfjsybIQ?si=40IzgvQoCcAwS4FR")
    elif sekret_text == "ух емма ето шо такое?":
        print("https://youtu.be/pVHKp6ffURY?si=XcL4G4JkrYc1VUsC")
    elif sekret_text == "BUSI BUSI?":
        print("https://youtu.be/BL4P7QGLZ4M?si=VWpCH-Kq_UC2_DdZ")
    elif sekret_text == "ШРЕК ":
        print("https://youtu.be/vXYVfk7agqU?si=OYw1bfxwXasUbg0L")
    elif sekret_text == "топ 1 фанк":
        print("https://youtu.be/UcRtFYAz2Yo?si=p1GyEbDYs19WKvBF")
    elif sekret_text == "SUIII":
        print("https://youtu.be/8EMy_ZGAdU0?si=6N_1SIP6_6QvjRGj")
    elif sekret_text == "LIVSEY":
        print("https://youtu.be/UcRtFYAz2Yo?si=woEiLAAy4N62nRaM")
    elif sekret_text == "ммм какой балдеж":
        print('https://youtu.be/wu4NYMmk8pk?si=mLcy4m0aa9dAxL91')
    elif sekret_text == "pedrooo":
        print("https://youtu.be/UgAwZ1aQFJc?si=FtZhyR_gYzhCJoDl")
    global logino
    logino = LOGIN.get()
    parolo = PLACEPAROL.get()
    with open("../kapustochka.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    FOUNDFOOTAGE = POVESTOCHKA_W_JSONEHEEHELOL(data=data, logino=logino)
    if FOUNDFOOTAGE == True:
        print("свинокабанчик")
        czujesz_kiegosz_toimordkasiecziszy = cheap_user(logino=logino, parolo=parolo)
        if czujesz_kiegosz_toimordkasiecziszy == True:
            print(
                "heloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo net")
            JASTOMUWSYAAAAAAAAAAAAA.destroy()
            onetjakriaknuw()
        else:
            print("Я ЗНАЮ ТИ ЧІТЄР ЯКИЙ ХОЧЕ ХАЦКНУТИ МІЙ КОМП ПРОВАЛЮЙ!!!!")
    else:
        print("БАБАК ТИ ЖАРЕНИЙ")
        data.append({"SEKRETO": sekret_text, "paroloo": parolo, "loginoo": logino})
        # data.append({)
        # data.append({})
        with open("../kapustochka.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            JASTOMUWSYAAAAAAAAAAAAA.destroy()


KNOPKA = Button(text="confirm :P ", bg="purple", height=4, width=30, font=100, command=funkcija_skadoosh)
KNOPKA.place(x=140, y=590)
button_for_sekret_text = Entry(font="4000000000000000000000000000000000000000000000000000000000000000")
button_for_sekret_text.place(x=530, y=560, height=50, width=500)
# with open("../kapustochka.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# POVESTOCHKA_W_JSONEHEEHELOL(data=data,parolo="A NOBIARAAA",logino="ez")
JASTOMUWSYAAAAAAAAAAAAA.mainloop()
