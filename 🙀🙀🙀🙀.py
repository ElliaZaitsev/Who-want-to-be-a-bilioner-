import random
C=5
F=5
P=0
Z=random.randrange(1,10)
print("Змінна Z=від 1-10 включно якому числу дорівнює Z?🤔")
A=int(input("Введіть якому числу дорівнює Z:"))
while True:
    if C==0:
        print("Ви програли🙄🙄🙄🙄🙄🙄🙄🙄🙄🙀🤭🤭🙀🙀👍🏽🤔🤔🫠🫠")
        break
    if A==Z:
        print("Ви дали правильну відповідь!👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽👍🏽")
        if C == 5:
            P += 500
        elif C == 4:
            P += 400
        elif C == 3:
            P += 300
        elif C == 2:
            P += 200
        elif C == 1:
            P += 100
        elif C == 0:
            P += 2
            P+=P
        print("У вас є",P,"балів")
        G=(input("Чи хотіли б ви купити підсказку?"))
        if G=="так":
            C+=1
            print(C)
            print("У вас є",C+1,"підсказок")
            if P==101:
                P-100
                print("У вас є",P-100,"балів")
            A = int(input("Введіть якому числу дорівнює Z:😃"))

        else:
            print("У вас немає певної кількості балів!")
            A = int(input("Введіть якому числу дорівнює Z:😃"))
        C=5
        Z = random.randrange(1, 10)
    else:
        print("Не вірна відповідь😭😭😭! Спробуйте ще раз🫠")
        if F>0:
            B = input("Чи хотіли б ви використати підсказку?🤔🤔🤔")
            if B=="так" or B=="ТАК" or B=="yes" or B=="YES" or B=="Yes" or B=="yES" or B=="Так" or B=="тАК" or B=="BOBR!":
                F-=1
                if F==0:
                    print("У вас закінчились підсказки🙀")
                minus_hint=random.randint(1,3)
                plus_hint=random.randint(1,3)
                print("Ваше число знаходится в",Z-minus_hint,"До",Z+plus_hint)
        A = int(input("Введіть якому числу дорівнює Z:"))
        C-=1
        print(C,"Кількість спроб")

