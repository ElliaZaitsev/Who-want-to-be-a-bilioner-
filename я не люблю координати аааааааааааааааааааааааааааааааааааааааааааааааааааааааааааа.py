from tkinter import *
import random
can=Tk()
first=[1015,800,500,770]
can.title("board tenis")
dousomethingwin=["you win something🥳🥳🥳","you win nothing😓😭🥲😿"]
ujustdied=["Ти пограв💀... я навіть не знаю від чого LoL","киньте монетку щоб продовжити","Принцесса в іншій фортеці","ваше гра - рраз и нету","ABOBUS","wht","hehe boi","oops","SKADOOSH","апчхи! ой ти програв через те що я пчихнув???"]
lolrandom=random.choice(ujustdied)
nah=random.choice(dousomethingwin)
heheboi=1
can.geometry()
x_size=200
y_size=160
x=860
y=420
ball_x = 3
ball_y = 3
def buttoninbutton():
    lol1=Label(text=nah,height=4,width=50,font=100,bg="#FFF5A8")
    lol1.place(x=480,y=500)
tipa_orange="#FF6A14"
tipa_blue="#4196D2"
tipa_janeznaju="#64AF91"
tipa_banana="#FFF5A8"
tipa_zelenuj="#D1FF29"
tipa_figoletovuj="#8629FF"
tipa_krasivo="#568AD2"
tipa_WOOW="#79983E"
can.resizable(True,True)
ahh=Canvas(width=5000,height=5000,bg=tipa_zelenuj)
ahh.pack()
ahh.create_rectangle(0,0,1525,850,fill=tipa_orange)
plat=ahh.create_rectangle(1015,770,500,740,fill=tipa_WOOW)
ball=ahh.create_oval(126,650,196,720,fill=tipa_blue)
def moving(event):
    if event.keysym == "a" and ahh.coords(plat)[0] - 20 > -5:
        ahh.move(plat, -10, 0)
    elif event.keysym == "d" and ahh.coords(plat)[2] + 20 < 1530:
        ahh.move(plat, 10, 0)
can.bind("<a>", moving)
can.bind("<d>", moving)
def ballmove():
    global ball_x, ball_y,heheboi,ujustdied
    ahh.move(ball, ball_x, ball_y)
    ahh.after(10, ballmove)
    ups=Label(text=f"{heheboi}❤️",bg="#FF6A14",height=2, width=10, font=100000000000000000000000000000000000000000000000000000000000000000000000000)
    ups.place(x=1300, y=300)
    if heheboi==1:
        ups["text"]="❤️"
    if ahh.coords(ball)[3] + 25 > 810:

        ball_y = -ball_y
        heheboi-=1
    elif ahh.coords(ball)[2] + 25 > 1545:
        ball_x = -ball_x

    elif ahh.coords(ball)[1] - 25 < -25:
        ball_y = -ball_x
    elif ahh.coords(ball)[0] - 25 < 0:
        ball_x = -ball_x
    elif heheboi==0:
        can.destroy()
        app1=Tk()
        youjustdiedLOOOOOOOL=Label(text=lolrandom,bg="#FF6A14",height=4, width=111, font=100)
        youjustdiedLOOOOOOOL.place(x=100,y=50)
        lol_restart=Button(text="free 1 million of null $_$ :)",bg="#4196D2",height=4, width=50, font=100,command=app1.destroy)
        lol_restart.place(x=100,y=250)
        IWANNARUNAWAAAY=Button(text="it's a secret button🤔🤔🤔???",bg="#79983E",height=4,width=50,font=100)
        IWANNARUNAWAAAY.place(x=800,y=250)
        secret=Button(text="press if you want to win",height=4,width=50,font=100,bg="#568AD2",command=app1.destroy)
        secret.place(x=100,y=500)
        app1.mainloop()
        app2=Tk()
        yay=Label(text="you win i know it was easy",bg="#D1FF29",height=4, width=111, font=100)
        yay.place(x=100,y=50)
        lol=Button(text="click to find out what you won...",bg="#64AF91",height=4,width=50,font=100,command=buttoninbutton)
        lol.place(x=480,y=300)
        app2.mainloop()
for i in range(7):
    box1=ahh.create_rectangle(x,y,x-x_size,y+y_size,fill=tipa_janeznaju)
    if i == 1:
        y=230
        x = 990
    elif i==2:
        x = 740
    elif i == 3:
        x = 610
        y=40
    elif i==4:
        x=860
    elif i==5:
        x=1110
ballmove()
can.mainloop()