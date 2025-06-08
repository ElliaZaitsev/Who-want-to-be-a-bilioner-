# A=-10
# while True:
#     print(A)
#     A+=1
#     if A==10:
#         break
# # A=1
#
# while A==1:
#     b=input("Як тебе звати?")
# K=0
# A=int(input("Введіть з якого числа ми почнемо"))
# B=A+20
# while True:
#     K+=A
#     print(A)
#     A+=1
#     if A==B+1:
#         break
# B=0
# C=0
# while True:
#     A=int(input("Введіть будь які числа"))
#     if A==0:
#         print(B)
#         print(C)
#         print(B//C)
#         break
#     B+=A
#     C=C+1
# A=int(input("Введіть ваше число"))
# C=0
# D=0
# while True:
#     B=A%10
#     D+=1
#     C+=B
#     A=A//10
#     if A==0:
#         print(C)
#         break
# K=0
# A=int(input("Введіть число"))
# N=int(input("Введіть число"))
# while True:
#     print(A**K)
#     K+=1
#     if K==N+1:
#         break
A=int(input("Введіть ваше число"))
while True:
    B=A%10
    print(B)
    A=A//10
    if A==0:
        break


