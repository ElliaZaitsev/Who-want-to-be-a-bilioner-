from tkinter.ttk import Label
CCCP=["дратуте","ow hello yea","OMG!!!!!!","!?1?!?!!???!???!!!????","hehe vay","i love breavers🥺🥺🥺","she was a fair","ITS A BIG FAKE I DO NOT BELIVE YOU FAKE!!!!","amogus😱"]
P=["red","#ff9e00","#2ff610","#45855a","#2bdcd4","#22a3ec","#2420ea","black"]
L=["red","yellow","orange","green","white"]
i=0
B=0
BOBR=0
varenik="???"
from tkinter import *
app=Tk()
C=0
def bobr():
    global C,i,B,BOBR
    C+=1
    A["text"]=C
    if C%100==0:
        A["bg"]=L[B]
        B+=1
    if B==len(L):
        B=0
    app["bg"]=P[i]
    i+=1
    if i==len(P):
        i=0
    if C%100==0:
        pelmenchik["text"]=CCCP[BOBR]
        BOBR+=1
        if BOBR==len(CCCP):
            BOBR=0
app.title("котофей котофейович котофа")
A=Label(text="блінчики з обжареним фаршом циболькою і посипаним сиром ТОП1!!!",bg="blue",fg="black",font=1000000)
kaban=Button(text="DISCO PARTY!!! recommend: op autoclicker",bg="white",fg="red",height=3,width=35,font="30",command=bobr)
pelmenchik=Label(text="...",bg="black",fg="white",font=1000000)
kaban.place(x=608,y=400)
A.place(x=608,y=370)
pelmenchik.place(x=0,y=0)
app.mainloop()