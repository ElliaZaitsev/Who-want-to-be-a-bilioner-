from tkinter import *
from tkinter import messagebox
XD="gren"
bobr=[]
bobrA=[0,0,0,0,0,0,0,0,0]
def kaban(Button,number):
    print(number)
    global XD
    if number not in bobr:
        bobrA[number]=XD
        print(bobrA)
        if XD=="gren":
            Button["bg"]="green"
            XD="blu"
        elif XD=="blu":
            Button["bg"]="blue"
            XD="gren"
        bobr.append(number)
    winner()
def winner():
    winner=None
    if bobrA[0]==bobrA[1]==bobrA[2]!=0:
        winner=bobrA[0]
        print("скуфікі були легкими)))")
    elif bobrA[3]==bobrA[4]==bobrA[5]!=0:
        winner = bobrA[3]
    elif bobrA[6]==bobrA[7]==bobrA[8]!=0:
        winner=bobrA[6]
    elif bobrA[0]==bobrA[3]==bobrA[6]!=0:
        winner=bobrA[0]
    elif bobrA[1]==bobrA[4]==bobrA[7]!=0:
        winner=bobrA[1]
    elif bobrA[2]==bobrA[5]==bobrA[8]!=0:
        winner=bobrA[2]
    elif bobrA[2]==bobrA[4]==bobrA[6]!=0:
        winner=bobrA[2]
    elif bobrA[0]==bobrA[4]==bobrA[8]!=0:
        winner = bobrA[0]
        print("open please don't worry it's youtube video:) ----->                  https://youtu.be/dQw4w9WgXcQ?si=0NnHDVMt1YVW7G61")
    if winner=='gren':
        messagebox.showinfo("перемога","виграли зелені")
        global Restart
        Restart()
    if winner=="blu":
        messagebox.showinfo("перемога","виграли сині")
        Restart()
    # if A["bg"]!=Color and B["bg"]!=Color and C["bg"]!=Color and D["bg"]!=Color and I["bg"]!=Color and F["bg"]!=Color and G["bg"]!=Color and Y["bg"]!=Color and V["bg"]!=Color:
    if len(bobr)==9:
        messagebox.showinfo("НІЧІЯ!","ніхто не виграв")
        Restart()
Color="orange"
P=["green",]
app=Tk()
app["bg"]="red"
A=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(A,4))
A.place(x=725,y=400)
B=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(B,7))
B.place(x=725,y=500)
C=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(C,1))
C.place(x=725,y=300)
D=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(D,3))
D.place(x=620,y=400)
I=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(I,6))
I.place(x=620,y=500)
F=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(F,0))
F.place(x=620,y=300)
G=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(G,2))
G.place(x=830,y=300)
Y=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(Y,5))
Y.place(x=830,y=400)
V=Button(text="",fg="blue",bg="orange",height=5,width=12,command=lambda: kaban(V,8))
V.place(x=830,y=500)
def Restart():
    global bobr,bobrA,XD
    XD="gren"
    bobrA = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    bobr = []
    A["bg"]="orange"
    A.config(state="normal")
    B["bg"]="orange"
    B.config(state="normal")
    C["bg"]="orange"
    C.config(state="normal")
    D["bg"]="orange"
    D.config(state="normal")
    I["bg"]="orange"
    I.config(state="normal")
    F["bg"]="orange"
    F.config(state="normal")
    G["bg"]="orange"
    G.config(state="normal")
    Y["bg"]="orange"
    Y.config(state="normal")
    V["bg"]="orange"
    V.config(state="normal")
def instructions():
    messagebox.showinfo("інструкція для гри","інструкція для гри привила продія хрестики нулики: в цій грі командам потрібно викласти лінію свого зеленого або синього кольору та команда яка зробить це швидше виграла а єслі ти не поняв ці привила з 1 раза то ти пельмень пережарений")
def exit():
    app.destroy()
app.bind("<q>",lambda e:kaban(F,0))
app.bind("<w>",lambda e:kaban(C,1))
app.bind("<e>",lambda e:kaban(G,2))
app.bind("<a>",lambda e:kaban(D,3))
app.bind("<s>",lambda e:kaban(A,4))
app.bind("<d>",lambda e:kaban(Y,5))
app.bind("<z>",lambda e:kaban(I,6))
app.bind("<x>",lambda e:kaban(B,7))
app.bind("<c>",lambda e:kaban(V,8))
app.bind("<p>",lambda e:Restart())
app.bind("<i>",lambda e:instructions())
app.bind("<m>",lambda e:exit())
print("легендарна піснека ----------> https://youtu.be/kk3_5AHEZxE?feature=shared")
app.bind("<O>")
print("котики муркотики тьоплєнкі животік ------> https://youtu.be/qnSVF7EEjSQ?si=Azmfz5tNhB0jpl5I")
app.bind("<K>")
print("а муха тоже вертольот -------> https://youtu.be/3iTL04GiNrY?feature=shared")
app.bind("<M>")
print("йожики топ --------> https://youtu.be/i-pgvaB3LMA?feature=shared")
app.bind("<R>")
print("ГУСЬ -----------> https://youtu.be/gJiPccEws3k?feature=shared")
app.bind("<G>")
app.mainloop()

























