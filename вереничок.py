# A="назва гри: Roblox"
# B="жанр гри: Я пельменю якій в цього вареника в маслні жанр :("
# C="тип гри: online"
# print(D)
# I="назва: гри Standoff"
# XD="жанр: шутер👻"
# KABANCHIK="тип гри: online"
# A=
# # print(A)
# class Game:
#     name="Roblox"
#     genre="Пельмень"
#     tipe="online"
#     description="не просто гра а спільнота ігор"
#     def info(self):
#         print(self.name,self.genre,self.description)
# A=Game()
# A.info()
# class Game:
#     def  __init__(self,name,genre,tipe,description):
#         self.name=name
#         self.genre=genre
#         self.tipe=tipe
#         self.description=description
#     def info(self):
#         print(self.name,self.genre,self.tipe,self.description)
# A=Game(name="name",genre="genre",tipe="tipe",description="description")
# A.info()
# B.info()
# print("у виборі є: лимонад чай сік")
# A=input("Виберіть напій:")
# if A=="лимонад":
#     print("у виборі є:лимон лимонний сік м'ята лід")
# B=input("виберіть добавку до лимонаду ")
# if B=="лимон" or B=="лимонний сік" or B=="м'ята" or B=="лід":
#     print("<<Лимонад та [ДОБАВКА]>>")
# else:
#     print("<<Лимонад>>")
# A==input("виберіть напій")
# if A=="чай":
#     print("у виборі є: лимон білий цукор тросниковий цукор м'ята")
#     B==input("виберіть добавку")
#     if B=="лимон" or B=="білий цукор" or B=="тросниковий цукор" or B=="м'ята":
#         print("<<Чай та [ДОБАВКА]>>")
#     else:
#         print("<<Чай>>")
# import random
# from random import randrange
# while True:
#     C=random.randrange(2,1000,)
#     print("1)🦫. ВСІ НАЗВИ ДОБАВОК МОЖНА ПИСАТИ ТІЛЬКИ АБО ВСІ ЛІТЕРИ В СЛОВІ БУДУТЬ МАЛЕНЬКИМИ АБО ВЕЛИКИМИ!!!!!!!")
#     print("2)🦫. виберіть добавку до вашого лимонаду в наявності є: лимон, лимонний сік, лід, м'ята, цукор.")
#     A=input("3)🦫. Виберіть добавку")
#     if A=="лимон":
#         print("замовлення №",C,"<<ЛИМОНАД>> з добавкою <<ЛИМОН🍋>>")
#     elif A=="лимонний сік":
#         print("замовлення №",C,"<<ЛИМОНАД>> з добавкою <<ЛИМОННИЙ СІК🍋>>")
#     elif A=="лід":
#         print("замовлення №",C,"<<ЛИМОНАД>> з добавкою <<ЛІД🥶>>")
#     elif A=="м'ята":
#         print("замовлення №",C,"<<ЛИМОНАД>> з добавкою <<М'ЯТА>>🍃")
#     elif A=="цукор":
#             print("замовлення №",C,"<<ЛИМОНАД>> з добавкою <<ЦУКОР>>🍭")
#     elif A!="лимон" or A!="ЛИМОН" or A!="лимонний сік" or A!="ЛИММОННИЙ СІК" or A!="лід" or A!="ЛІД" or A!="м'ята" or A!="М'ЯТА" or A!="цукор" or A!="ЦУКОР":
#         print("НЕ МОЖНА <<ЗМІШУВАТИ ДОБАВКИ😡!!!!!!>>")
#     else:
#         print("замовлення №",C,"<<ЛИМОНАД>> без добавки")
#         break
# class Drink:
#     def __init__(self,name,dobavka):
#         self.name=name
#         self.dobavka=dobavka
#     def info(self):
#         if not self.dobavka:
#             print("У ВАС НЕТУ ДОБАВОЧКИ!!!!")
#         else:
#             print(self.name,self.dobavka)
# lambordginidamborgini = input("виберіть добавочку🌈")
# A=Drink(name="ім'я")
# A.info()
A=input("Введіть число:")
B=input("Введіть число:")
C=input("Введіть число знову!:")
if A.isdigit() and B.isdigit() and C.isdigit():
    print("тільки числа")
    if int(A) <= 0 or int(B) <= 0 or int(C) <= 0:
        print("З негативними числами нічого не вийде!😡")
    elif A + B < C and A+C<B and B+C<A:
             print("Жаль, але з цього трикутника не зробити😭")
    else:
        print("Ура! Нарешті можна зробити трикутник🥳")
else:
    print("можна вписувати тільки числа!👻")

#     print("З негативними числами нічого не вийде!😡")
# if int(A)<=0 or int(B)<=0 or int(C)<=0:
#     print("З негативними числами нічого не вийде!😡")
# elif A+B<C:
#     print("Жаль, але з цього трикутника не зробити😭")
# elif not A.isdigit() or not B.isdigit() or not C.isdigit():
#     print("можна вписувати тільки числа!👻")
# else:
#     print("Ура! Нарешті можна зробити трикутник🥳")