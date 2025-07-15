from tkinter import *
XO=1
bobr=[]
bobrA=[0,0,0,0,0,0,0,0,0]
def kaban(Button,number):
    print(number)
    global XO
    if number not in bobr:
        bobrA[number]=XO
        print(bobrA)
        if XO==1:
            Button["bg"]="green"
            XO=2
        elif XO==2:
            Button["bg"]="blue"
            XO=1
        bobr.append(number)
    winner()
def winner():
    if bobrA[0]==bobrA[1]==bobrA[2]!=0:
        print("you are so noob🫥")
    if bobrA[3]==bobrA[4]==bobrA[5]!=0:
        print("perfect")
    if bobrA[6]==bobrA[7]==bobrA[8]!=0:
        print("win")
    if bobrA[0]==bobrA[3]==bobrA[6]!=0:
        print("easy")
    if bobrA[1]==bobrA[4]==bobrA[7]!=0:
        print("uiiaiaiuiai")
    if bobrA[2]==bobrA[5]==bobrA[8]!=0:
        print("AMQG#$")
    if bobrA[2]==bobrA[4]==bobrA[6]!=0:
        print("what!?")
    if bobrA[0]==bobrA[4]==bobrA[8]!=0:
        print("open please don't worry it's youtube video:) ----->                  https://youtu.be/dQw4w9WgXcQ?si=0NnHDVMt1YVW7G61")
P=["green",]
app=Tk()
app["bg"]="red"
A=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(A,4))
A.place(x=725,y=400)
B=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(B,7))
B.place(x=725,y=500)
C=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(C,1))
C.place(x=725,y=300)
D=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(D,3))
D.place(x=620,y=400)
I=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(I,6))
I.place(x=620,y=500)
F=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(F,0))
F.place(x=620,y=300)
G=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(G,2))
G.place(x=830,y=300)
Y=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(Y,5))
Y.place(x=830,y=400)
V=Button(text="",fg="blue",bg="white",height=5,width=12,command=lambda: kaban(V,8))
V.place(x=830,y=500)
app.mainloop()