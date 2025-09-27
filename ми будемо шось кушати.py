
from tkinter import *
can=Tk()
can.title("board tenis")
can.geometry()
can.resizable(True,True)
ahh=Canvas(width=5000,height=5000,bg="white")
ahh.pack()
ahh.create_rectangle(0,0,1525,850,fill="green")
ahh.create_line(760,1,760,900,dash=250)
ball=ahh.create_oval(726,350,796,420,fill="white")
plat1=ahh.create_rectangle(100,230,90,530,fill="white")
plat2=ahh.create_rectangle(1345,230,1335,523,fill="white")
pelmenius=ahh.create_text(500,120,text="0",font="arial 50")
pelmen=ahh.create_text(1000,120,text="0",font="arial 50")
print(ahh.coords(plat1))
odin=0
dwa=0
ball_x=3
ball_y=3
PELMEN6="#2BA5C4"
app1=None
def relpay():
    odin=0
    dwa=0
def closesomething():
    global app1
    app1.destroy()
def moving(event):
    if event.keysym == "w" and ahh.coords(plat1)[1]-20>0:
        ahh.move(plat1, 0, -20)
    elif event.keysym == "s" and ahh.coords(plat1)[3]+20<850:
        ahh.move(plat1, 0, 20)
    elif event.keysym == "e" and ahh.coords(plat2)[1]-20>0:
        ahh.move(plat2,0,-20)
    elif event.keysym=="q" and ahh.coords(plat2)[3]+20<850:
        ahh.move(plat2,0,20)
def ballmove():
    global ball_x, ball_y,pelmen,pelmenius,odin,dwa,closesomething
    ahh.move(ball,ball_x,ball_y)
    ahh.after(10,ballmove)
    if ahh.coords(ball)[3]+25>850:
        ball_y=-ball_y
    elif ahh.coords(ball)[2]+25>1545:
        ball_x=-ball_x
        ahh.delete(pelmenius)
        odin+=1
        pelmenius=ahh.create_text(500, 120, text=odin, font="arial 50")
    elif ahh.coords(ball)[1]-25<-25:
        ball_y=-ball_y
    elif ahh.coords(ball)[0]-25<0:
        ball_x=-ball_x
        ahh.delete(pelmen)
        dwa += 1
        pelmen = ahh.create_text(1000, 120, text=dwa, font="arial 50")
    if ahh.coords(ball)[2] > ahh.coords(plat2)[0] and ahh.coords(ball)[2] < ahh.coords(plat2)[2] \
            and ahh.coords(ball)[3] > ahh.coords(plat2)[1] and ahh.coords(ball)[3] < ahh.coords(plat2)[3]:
        ball_x=-ball_x
    if ahh.coords(ball)[0] > ahh.coords(plat1)[0] and ahh.coords(ball)[0] < ahh.coords(plat1)[2] \
            and ahh.coords(ball)[1] > ahh.coords(plat1)[1] and ahh.coords(ball)[1] < ahh.coords(plat1)[3]:
        ball_x=-ball_x
    global app1
    if odin==1:
        can.destroy()
        app1 = Tk()
        pelmememeememem = Label(text=f"виграв гравець 1 з рахунком <<{odin}>>", bg=PELMEN6, height=4, width=50, font=1000000000000000000)
        pelmememeememem.place(x=0, y=120)
        pelmen1 = Label(text=f"гравець 2 програв за рахунком <<{dwa}>>", bg=PELMEN6, height=4, width=50, font=1000000000000000000)
        pelmen1.place(x=1000, y=120)
        closeit = Button(text="Restart", bg="orange", height=4, width=50, font=1000000000000000000,
                         command=closesomething)
        closeit.place(x=80, y=500)
        replay = Button(text="Retry", bg="blue", height=4, width=50, font=1000000000000000000, command=relpay)
        replay.place(x=700, y=500)
        app1.mainloop()
    elif dwa==1:
        can.destroy()
        app1=Tk()
        pelmen1=Label(text=f"гравець 2 виграв за рахунком <<{dwa}>>",bg=PELMEN6, height=4, width=50,font=1000000000000000000)
        pelmen1.place(x=80,y=120)
        pelmememeememem = Label(text=f"гравець 1 програв з рахунком <<{odin}>>", bg=PELMEN6, height=4, width=50,font=1000000000000000000)
        pelmememeememem.place(x=80, y=120)
        closeit = Button(text="Restart",bg="orange",height=4, width=50,font=1000000000000000000,command=closesomething)
        closeit.place(x=100,y=500)
        can.destroy()
        replay=Button(text="Retry",bg="blue",height=4, width=50,font=1000000000000000000,command=relpay)
        replay.place(x=10000,y=500)
        app1.mainloop()
ballmove()
can.focus_set()
can.bind("<s>",moving)
can.bind('<w>', moving)
can.bind("<e>",moving)
can.bind('<q>', moving)
can.mainloop()
