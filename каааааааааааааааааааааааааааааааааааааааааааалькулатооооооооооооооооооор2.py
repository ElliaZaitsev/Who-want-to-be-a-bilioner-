from tkinter import *
zeronul=0
lblx=0
lbly=0
nul=0
def q(number):
    global nul, zeronul, lblx, lbly
    if nul==0:
        nul=1
        A["text"]=str(number)
    else:
        A["text"]+=str(number)

    if zeronul==0:
        lblx=int(A["text"])
    else:
        lbly=int(A["text"])
def nabaK():
    global zeronul,lblx,lbly,nul
    zeronul = 0
    lblx = 0
    lbly = 0
    nul = 0
    A["text"]=0
    lambda:q(1)
def q1():
    q(1)
def q2():
    q(2)
def q3():
    q(3)
def q4():
    q(4)
def q5():
    q(5)
def q6():
    q(6)
def q7():
    q(7)
def q8():
    q(8)
def q9():
    q(9)
def q0():
    q(0)
def btnznak(z):
    global nul,zeronul,znak
    A["text"]=A["text"]+z
    nul=0
    zeronul=1
    znak=z
def plus():
    btnznak("+")
def minus():
    btnznak("-")
def pomnoshiti():
    btnznak("*")
def podiliti():
    btnznak("/")
def btrv():
    global znak,num,num2,lblx,lbly,nul,zeronul
    if znak=="+":
        A["text"]=str(lblx+lbly)
    elif znak=="-":
        A["text"]=str(lblx-lbly)
    elif znak=="*":
        A["text"]=str(lblx*lbly)
    elif znak=="/":
        if lbly==0:
            A["text"]="you can't divide by zero"
        else: A["text"]=str(lblx/lbly)
    lblx=int(A['text'])
app=Tk()
MEGAPLEMN="#1598d5"
MINIPELEMN="#154360"
SUPERMEGAPELEMEN="#33d176"
VERENICHIOK="#8e2f2f"
A=Label(text="calculator🦫",bg=SUPERMEGAPELEMEN,fg="black",height=5,width=50,font=1000000000000000000000)
A.grid(row=4,column=0,columnspan=4,sticky="nsew")
B=Button(text="1",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q1)
B.grid(row=0,column=0,sticky="nsew")
C=Button(text="2",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q2)
C.grid(row=0,column=1,sticky="nsew")
D=Button(text="3",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q3)
D.grid(row=0,column=2,sticky="nsew")
I=Button(text="4",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q4)
I.grid(row=1,column=0,sticky="nsew")
F=Button(text="5",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q5)
F.grid(row=1,column=1,sticky="nsew")
K=Button(text="6",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=lambda:q(6))
K.grid(row=1,column=2,sticky="nsew")
M=Button(text="7",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q7)
M.grid(row=2,column=0,sticky="nsew")
NNN=Button(text="8",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q8)
NNN.grid(row=2,column=1,sticky="nsew")
ZZZ=Button(text="9",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q9)
ZZZ.grid(row=2,column=2,sticky="nsew")
Bobrkabanchikplemen=Button(text="0",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=q0)
Bobrkabanchikplemen.grid(row=3,column=1,sticky="nsew")
brrrbrrrrnepatapim=Button(text=":",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=podiliti)
brrrbrrrrnepatapim.grid(row=0,column=3,sticky="nsew")
VARENIK=Button(text="X",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=pomnoshiti)
VARENIK.grid(row=1,column=3,sticky="nsew")
KORTOPLIA=Button(text="+",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=plus)
KORTOPLIA.grid(row=2,column=3,sticky="nsew")
MINUS=Button(text="-",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=minus)
MINUS.grid(row=3,column=2,sticky="nsew")
DORIVNIE=Button(text="=",bg=VERENICHIOK,fg="black",height=5,width=10,command=btrv)
DORIVNIE.grid(row=3,column=3,sticky="nsew")
KABAN=Button(text="C",bg=MEGAPLEMN,fg=MINIPELEMN,height=5,width=10,command=nabaK)
KABAN.grid(row=3,column=0,sticky="nsew")
for col in range(4):
    # робить колонки однаковими по ширині
    app.grid_columnconfigure(col, weight=1)

for row in range(5):
    # робить рядки однаковими по висоті
    app.grid_rowconfigure(row, weight=1)
app.mainloop()