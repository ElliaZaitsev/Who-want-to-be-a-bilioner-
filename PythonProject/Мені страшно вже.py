
print("Гра/хто хоче стати міліардером?")
pod50=True
podzn=True
summa=0
n_summa=0
def dost_podskaski():
    print("\t\t\t\t************")
    print("\t\t\t\t*50 на 50")
    print("\t\t\t\t************")
    print("\t\t\t\t*допомога знавця")
    print("\t\t\t\t************")
if pod50==True and podzn==False:
    print("\t\t\t\t\t\t*********")
    print("\t\t\t\t\*50 на 50")
if pod50==True and podzn==False:
    print("\t\t\t\t\t\t*********")
    print("\t\t\t\t\t\t\t*50 на 50*")
if pod50==True and podzn==False:
    print("\t\t\t\t\t\t*********")
    print("\t\t\t\t\t*50 на 50*")
    print("\t\t\t\t\t\t*********")
if pod50==False and podzn==True:
    print("\t\t\t\t\t\t*********")
    print("\t\t\t\t\t*Допомога гравця*")
    print("\t\t\t\t\t\t*********")
if pod50==False and podzn==False:
    print("\t\t\t\t\t\t***************")
    print("\t\t\t\t\t*Доступних підсказок нема")
    print("\t\t\t\t\t\t**************")
def podskazki(a,b):
    global pod50
    global podzn
    pods=""
    question=input("Хочете використати підзкаску?")
    if question=="Да" or question=="да" or question=="ДА":
        if pod50==False and podzn==True:
            print("Доступних підсказок нема")
        elif pod50==True and podzn==True:
            pods=(input("50 на 50 або допомага знавця?"))
        elif pod50==True and podzn==False:
            pods=input("50 на 50?")
        elif pod50==False and podzn==True:
             pods=input("допомога знавця?")
    if pods=="50 на 50?":
        print("1.",a,"\t2.",b)
        pod50=False
    elif pods=="допомога знавця":
        print("1."",b,")
        podzn=False
    else :
        print("не коректний")
def question(a,b, a1, a2, a3, a4,):
    print("Питання No"+str(a))
    print(b)
    print("1.",a1,"\t2.",a2,)
    print("3.",a3,"\t4.",a4,)

def loose(a):
    print("шкода ви програли!")
    print("Ваш виграш складає",n_summa,"грн.")

Continue=True
Number=0
begin=input("Хочете пограти знову?")
if begin=="Да" or begin=="да" or begin=="ДА":
    dost_podskaski()
    ques="Який континент складається лише з однієї країни?"
question(1,ques,"Europa","Asia","Africa","Australia")
podskazki("Europa","Australia")
answer=input("Введіть відповідь:")
if answer=="Australia":
    print("Чудово! Ви дали правильну відповідь")
    summa=5000
else:
    Continue=False
if Continue==False:
    loose(n_summa)
else:
    dost_podskaski()
    ques="Де росуть соняшники?"
    question(2,ques,"На землі","На сонці","На небі","В воді")
    podskazki("На сонці","На землі")
    answer=input("Дайте відповідь:")
    if answer=="На землі":
        print("Чудово!Ви дали правильну відповідь!")
        summa=10000
    else:
        Continue=False
if Continue==False:
    loose(n_summa)
else:
    dost_podskaski()
    ques="Яких грошей не буває?"
    question(2,ques,"Гривні","Льє","Долари","Ліри")
    podskazki("Ліри","Льє")
    answer=input("Введіть відповідь:")
    if answer=="Льє":
        print("Чудово! Ви дали правильну відповідь!")
        summa=20000
    else:
        Continue=False
    if Continue==False:
        loose(n_summa)
    else:
        dost_podskaski()
    ques="Як називається портрет,який написаний з самого себе?"
    question(4,ques,"Самовал","Самописка","Зеркальний","Автопортрет")
    answer=input("Введіть відповідь:")
    if answer=="Автопортрет":
        print("Чудово!Ви дали правильну відповідь")
        summa=50000
    else:
        Continue=False
if Continue==False:
    loose(n_summa)
else:
    dost_podskaski()
    ques="Як називаєть безпілотний літальний апарат"
    question(5,ques,"Дрон","Махаон","Десептикон","Аніон")
    podskazki("Аніон","Дрон")
    answer=input("Введіть відповідь:")
    if answer=="Дрон":
        print("Чудово!Ви вибрали правильну відповідь")
        summa=100000
        n_summa=1000000
    else:
        Continue=False
if Continue==False:
    loose(n_summa)
else:
    dost_podskaski()
    quest="В якій грі не використовуються м'яч?"
    question(6,ques,"Баскетбол","Керлінг","Теніс","Бейсбол")
    podskazki("Теніс","Керлінг")
    answer=input("Дайте відповідь:")
if answer=="Керлінг":
    print("Чудово!Ви дали правильну відповідь")
    summa=250000
else:
    Continue=False
    if Continue==False:
        loose(n_summa)
    else:
        dost_podskaski()
        ques="Який з цих мостів знаходится в Києві?"
        question(7,ques,"Кримський","Дарницький","Невський","Славутицький")
        podskazki("Невський","Дарницький")
        answer=input("Введіть відповідь:")
    if answer=="Дарницький":
        print("Чудово!Ви дали правильну відповідь")
        summa=1000000
    else:
        Continue=False
if Continue==False:
    loose(n_summa)

else:
    dost_podskaski()
    ques="Хто з цих людей письменник"
    question(8,ques,"Жанклод Вадам","Клод Моне","Едгар По","Усейм Болт")
    podskazki("Клод  Моне","Едгар По")
    answer = input("Введіть відповідь:")
if answer=="Едгар По":
    print("Чудово!Ви дали правильну відповідь!")
    summa=2500000
else:
    Continue=False
if Continue==False:
    loose(n_summa)
else:
    dost_podskaski()
    ques="Хто х цих мореплавців відкрив Мис Доброї надії?"
    question(9,ques,"Бартоломео Діаш","Джос Брюс","Васка Дагама","Христофор Колумб")
    podskazki("Христофор Колумб","Бартоломео Діаш")
    answer=input("Введіть відповідь")
if answer=="Бартоломео Діаш":
    print("Чудово!Ви дали правильну відповідь!")
    summa=5000000
else:
    Continue=False
if Continue==False:
    loose(n_summa)

else:
    dost_podskaski()
    ques="Який хімічний елемент отримав назву через синю лінію в його спектрі?"
    question(10,ques,"Індій","Родій","Церій","Нептуній")
    podskazki("Родій","Індій")
    answer=input("Введіть відповідь")
if answer=="Індій":
    print("Чудово!Ви дали правильну відповідь!")
    summa=10000000
    print("Ви ваграли супер приз!!!Вітаємо!!!")
    print("Ваш виграш складає",n_summa,"грн")
    print("Ти пельмень🙀🙀🙀???????")
    print("Ти вареник🙀🙀🙀???????")
else:
    Continue=False
    loose(n_summa)
    print("Ти пельмень🙀🙀🙀???????")
    print("Ти вареник🙀🙀🙀???????")