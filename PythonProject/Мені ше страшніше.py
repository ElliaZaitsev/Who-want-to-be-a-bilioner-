# A=input("Введіть слово або число")
# for i in range(78,99,10):
#     print(i)
# N=int (input("Введіть число"))
# K=input("Введіть слово")
# for i in range(N):
#     print(K)
# A=int(input("Введіть ціну грн. цукерок за 1 кг."))
# B=int(input("Введіть скільки кг. цукерок ви хочете купити"))
# if A==20 and B==1:
#     print("Badge:слідкоєшка")
# elif A==40 and B==2:
#         print("Badge:нівроку сладкоєшка!!! 2 кг канхвет😎")
# elif A==60 and B==3:
#     print("Badge:🙀")
# elif A==80 and B==4:
#     print("Badge:нам очень страшно ми не знаеє што ето такоє єсліб ми зналі что ето такое но ми не знаем что ето такое")
# elif A==100 and B==5:
#      print("Badge:OMG!")
# else:
#     print("дєточка...А ТИ НЕ ЛОПНИШ ДЄТОЧКА!!!!!!!")
# A=int(input("Введіть ціну грн. цукерок за 1 кг."))
# # print(A*2,"за 2 кілограми")
# # print(A*3,"за 3 кілограми")
# # print(A*4,"за 4 кілограми")
# # print(A*5,"за 5 кілограм")
# # print(A*6,"за 6 кілограм")
# # print(A*7,"за 7 кілограм")
# # print(A*8,"за 8 кілограм")
# # print(A*9,"за 9 кілограм")
# # print(A*10,"за 10 кілограм")
# for i in range(1,11):
#     print(i,"кілограм коштує" ,i*A,"грн")
# A=int(input("Введіть число"))
# B=int(input("Введіть число"))
# C=0
# for i in range(A,B+1):
#     print("i=",i,"C=",C)
#     C=C+i
#     print(C)
# A=(input("Введіть слово"))
# for i in range(10000):
#     print(A)
# coins=0
# M=int(input("Скільки монет покладемо в скарбницю"))
# N=int(input("Скільки монет віддаватимемо мамі:"))
# for week in range(1,53):
#     coins=coins+7*M-N
#     print("Тиждень №",week,"кількість монет",coins)
# for i in range(10,100):
#     if i%4==0 and i%6!=0:
#         print(i)
K=0
N=int(input("Скільки людей працювало"))
M=int(input("Скільки годин працювала перша людина"))
for i in range(1,N+1):
    print("Працівник №",M)
    K += M
    M+=1/4
print("загально відпрацьованих годин",K)