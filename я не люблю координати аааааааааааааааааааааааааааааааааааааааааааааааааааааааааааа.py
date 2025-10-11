from tkinter import *
can=Tk()
first=[1015,800,500,770]
can.title("board tenis")
can.geometry()
x_size=200
y_size=160
x=860
y=420
ball_x = 3
ball_y = 3
can.resizable(True,True)
ahh=Canvas(width=5000,height=5000,bg="white")
ahh.pack()
ahh.create_rectangle(0,0,1525,850,fill="white")
plat=ahh.create_rectangle(1015,800,500,770,fill="white")
ball=ahh.create_oval(126,650,196,720,fill="white")
def moving(event):
    if event.keysym == "a" and ahh.coords(plat)[0] - 20 > -5:
        ahh.move(plat, -10, 0)
    elif event.keysym == "d" and ahh.coords(plat)[2] + 20 < 1530:
        ahh.move(plat, 10, 0)
can.bind("<a>", moving)
can.bind("<d>", moving)
# box1=ahh.create_rectangle(860,420,860-x_size,420+y_size,fill="white")
# box2=ahh.create_rectangle(610,40,610-x_size,40+y_size,fill="white")
# box3=ahh.create_rectangle(860,40,860-x_size,40+y_size,fill="white")
# box4=ahh.create_rectangle(1110,40,1110-x_size,40+y_size,fill="white")
# box5=ahh.create_rectangle(740,230,740-x_size,230+y_size,fill="white")
# box6=ahh.create_rectangle(990,230,990-x_size,230+y_size,fill="white")
def ballmove():
    global ball_x, ball_y, pelmen, pelmenius, odin, dwa, closesomething
    ahh.move(ball, ball_x, ball_y)
    ahh.after(10, ballmove)
    if ahh.coords(ball)[3] + 25 > 850:

        ball_y = -ball_y

    elif ahh.coords(ball)[2] + 25 > 1545:
        ball_x = -ball_x

    elif ahh.coords(ball)[1] - 25 < -25:
        ball_y = -ball_y
    elif ahh.coords(ball)[0] - 25 < 0:
        ball_x = -ball_x
for i in range(7):
    box1=ahh.create_rectangle(x,y,x-x_size,y+y_size,fill="white")
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