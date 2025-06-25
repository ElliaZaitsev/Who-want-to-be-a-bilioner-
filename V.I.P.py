from нееееееееееееееееееееееееетттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттт import Chaynik
import random
PELMEN=[]
nabak=Chaynik(name="дратуте всем джентельменам",volume="ой летіли дикі гуси тай не долетіли",stan="очень вкусно",mode="!!!!!???????")
PELMEN.append(nabak)
dumplingnumber=random.randrange(1,100,2)
literu=random.choice(["E","R","F","A","S","M","N","K","L","O","P","Z","X"])
angryshrek=0
while True:
    print("1). Створити чайник")
    print("2). Обрати чайник зі списку")
    print("3). Включити чайник")
    print("4). Вимкнути чайник")
    print("5). Режим роботи")
    print("6). Інформація про всі чайники")
    print("7). Вихід з гри")
    A=int(input("Ореріть дію:"))
    if A==6:
        for i in PELMEN:
            i.info()
    elif A==3:
        PELMEN[angryshrek].on()
    elif A==4:
        PELMEN[angryshrek].off()
    elif A==5:
        PELMEN[angryshrek].IMAFLASH()
    elif A==1:
        KABANCHIKTOP1=input("введіть назву чайнику")
        KABANCHIKTOP2=int(input("введіть об'єм чайника"))
        KABANCHIKTOP3=input("введіть стан чайнічка")
        KABANCHIKTOP4=input("введіть мод чайнічка")
        kaban=Chaynik(name=KABANCHIKTOP1,volume=KABANCHIKTOP2,stan=KABANCHIKTOP3,mode=KABANCHIKTOP4)
        PELMEN.append(kaban)
    elif A==2:
        minipelmen=1
        for i in PELMEN:
            print(minipelmen,i.name)
            minipelmen+=1
        kortopelkia=int(input("введіть число"))
        angryshrek=kortopelkia-1