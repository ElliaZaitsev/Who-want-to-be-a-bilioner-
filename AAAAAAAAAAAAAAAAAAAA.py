from tkinter import *
class BOOOBBEEEEER:
    odin = 0
    dwa = 0
    ball_x = 3
    ball_y = 3
    PELMEN6 = "#2BA5C4"
    def window(self):
        self.can = Tk()
        self.can.title("board tenis")
        self.can.geometry()
        self.can.resizable(True, True)
        self.ahh = Canvas(width=5000, height=5000, bg="white")
        self.ahh.pack()
        self.ahh.create_rectangle(0, 0, 1525, 850, fill="green")
        self.ahh.create_line(760, 1, 760, 900, dash=250)
        self.ball = self.ahh.create_oval(726, 350, 796, 420, fill="white")
        self.plat1 = self.ahh.create_rectangle(100, 230, 90, 530, fill="white")
        self.plat2 = self.ahh.create_rectangle(1345, 230, 1335, 523, fill="white")
        self.pelmenius = self.ahh.create_text(500, 120, text="0", font="arial 50")
        self.pelmen = self.ahh.create_text(1000, 120, text="0", font="arial 50")
        print(self.ahh.coords(self.plat1))

    def ballmove(self):

        self.ahh.move(self.ball, self.ball_x, self.ball_y)
        self.ahh.after(10, self.ballmove)
        if self.ahh.coords(self.ball)[3] + 25 > 850:
            self.ball_y = -self.ball_y
        elif self.ahh.coords(self.ball)[2] + 25 > 1545:
            self.ball_x = -self.ball_x
            self.ahh.delete(self.pelmenius)
            self.odin += 1
            self.pelmenius = self.ahh.create_text(500, 120, text=self.odin, font="arial 50")
        elif self.ahh.coords(self.ball)[1] - 25 < -25:
            self.ball_y = -self.ball_y
        elif self.ahh.coords(self.ball)[0] - 25 < 0:
            self.ball_x = -self.ball_x
            self.ahh.delete(self.pelmen)
            self.dwa += 1
            self.pelmen = self.ahh.create_text(1000, 120, text=self.dwa, font="arial 50")
        if self.ahh.coords(self.ball)[2] > self.ahh.coords(self.plat2)[0] and self.ahh.coords(self.ball)[2] < self.ahh.coords(self.plat2)[2] \
                and self.ahh.coords(self.ball)[3] > self.ahh.coords(self.plat2)[1] and self.ahh.coords(self.ball)[3] < self.ahh.coords(self.plat2)[3]:
            self.ball_x = -self.ball_x
        if self.ahh.coords(self.ball)[0] > self.ahh.coords(self.plat1)[0] and self.ahh.coords(self.ball)[0] < self.ahh.coords(self.plat1)[2] \
                and self.ahh.coords(self.ball)[1] > self.ahh.coords(self.plat1)[1] and self.ahh.coords(self.ball)[1] < self.ahh.coords(self.plat1)[3]:
            self.ball_x = -self.ball_x
        
        if self.odin == 1:
            self.can.destroy()
            self.app1 = Tk()
            self.pelmememeememem = Label(text=f"виграв гравець 1 з рахунком <<{self.odin}>>", bg=self.PELMEN6, height=4, width=50,
                                    font=1000000000000000000)
            self.pelmememeememem.place(x=0, y=120)
            self.pelmen1 = Label(text=f"гравець 2 програв за рахунком <<{self.dwa}>>", bg=self.PELMEN6, height=4, width=50,
                            font=1000000000000000000)
            self.pelmen1.place(x=1000, y=120)
            self.closeit = Button(text="Restart", bg="orange", height=4, width=50, font=1000000000000000000,
                             command=self.closesomething)
            self.closeit.place(x=80, y=500)
            self.replay = Button(text="Retry", bg="blue", height=4, width=50, font=1000000000000000000, command=self.relpay)
            self.replay.place(x=700, y=500)
            self.app1.mainloop()
        elif self.dwa == 1:
            self.can.destroy()
            self.app1 = Tk()
            self.pelmen1 = Label(text=f"гравець 2 виграв за рахунком <<{self.dwa}>>", bg=self.PELMEN6, height=4, width=50,
                            font=1000000000000000000)
            self.pelmen1.place(x=80, y=120)
            self. pelmememeememem = Label(text=f"гравець 1 програв з рахунком <<{self.odin}>>", bg=self.PELMEN6, height=4, width=50,
                                    font=1000000000000000000)
            self.pelmememeememem.place(x=80, y=120)
            self.closeit = Button(text="Restart", bg="orange", height=4, width=50, font=1000000000000000000,
                             command=self.closesomething)
            self.closeit.place(x=100, y=500)
            self.can.destroy()
            self.replay = Button(text="Retry", bg="blue", height=4, width=50, font=1000000000000000000, command=self.relpay)
            self.replay.place(x=10000, y=500)
            self.app1.mainloop()
kria=BOOOBBEEEEER()
kria.window()