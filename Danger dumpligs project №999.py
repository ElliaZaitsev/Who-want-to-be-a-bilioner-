import math
while True:
    print("Доступні дії:")
    print("1-сума")
    print("2-різниця")
    print("3-добутки")
    print("4-частки")
    print("5-факторіал")
    print("6-1/X")
    print("7-степінь")
    print("8-корінь квадрата")
    print("9-вихід")
    A=int(input("Оберіть дію:"))
    if A==1:
        B=int(input("Введіть перше число"))
        C=int(input("Введіть друге число"))
        print("Ваша відповідь:",B+C)
    elif A==2:
        Z=int(input("Введіть перше число"))
        X=int(input('Введіть друге число'))
        print("Ваша відповідь:",Z-X)
    elif A==3:
        W=int(input("Введіть перше число"))
        D=int(input("Введіть друге число"))
        print("Ваша відповідь:",W*D)
    elif A==4:
        S=int(input("Введіть друге перше число"))
        B=int(input("Введіть друге число"))
        print("Ваша відповідь:",S//B)
    elif A==5:
        O=int(input("Ввеідть ваш факторіал:"))
        pelmen=1
        for i in range(0,O):
            pelmen = pelmen * (i+1)
            print(pelmen)
    elif A==6:
        rabbit=int(input("😭😭😭 я вже стомився від цього калькулятора ну ладно введіть число:"))
        print("Ваша відповідь:",1/rabbit)
    elif A==7:
        privetik=int(input("Введіть вашого бобра на процидуру:"))
        poka=int(input("Виводьте свого бобра із процидури:"))
        print("Ваша відповідь:",privetik**poka)
    elif A==8:
        FV4005=(int(input("Киньте пельменя в каструлю:")))
        print("Ваш пельмень приготовиться через:",math.sqrt(FV4005),"років")
    elif A==9:
        print("Ти пельмень пережарени-и-и-и-и-й-й-й-й-й!-!-!-!-!-!😭😭😭😭😭😭😭😭")
        break
    elif A>=10 or A<1:
        print("💀💀💀")

