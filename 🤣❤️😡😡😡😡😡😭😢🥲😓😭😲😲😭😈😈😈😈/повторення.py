"завдання 1."
# A=[1,5,9,8,-2,-5,-12,-3,-5]
# O=0
# E=0
# for i in A:
#     if i>0:
#         O+=1
#     if i<0:
#         E+=i
# B=[O,E]
# print(B)
# "завдання 2."
# A=[1,1,2,3,1,2,1,3]
# B=[]
#
# for i in A:
#     print(i)
#     if i not in B:
#         B.append(i)
# print(B)
# C=sum(B),
# print(C)
# C=0
# for i in B:
#     C+=i
#     print(C)
# print(list(set(A)))
# A=[-5,-8,-6,-7,-10,-2]
# b=A[0]
# for i in A:
#    if  i<b:
#        b=i
# list1=min(A)
# list2=max(A)
# print([list1,list2])
#        print(b)
# A=[-4,3,5,1,6,-123,-7,-7,12,3,-123,653,456,-67]
# EZ=0
# GG=[]
# aaa=0
# for i in range(len(A)):
#     else:
#         GG.append(A[i])
#         print(GG)
# for i in A:
#     if i<0:
#         EZ+=1
#         print(EZ)
    # if i%2:
    #     aaa+=A[i]
# A=[1,999,5]
# for i in A:
#     lena=len(A)
#     print(A[lena-1])
# A=[3920578326,3285972123,218412,58812,19472812,267473272164,12847266742189,956324]
# print(A[6:1:-1])
# B=[]
# for i in A:
#     B.insert(0,i)
#     print(B)
# for i in range(len(A)-1,-1,-1):
#     B.append(A[i])
#     print(B,"***")
A="Картинка уявна: Бобер стоїть біля вирубаного лісу, навколо хаос, повалені дерева. Зверху: 👉 «Я: тільки один шматочок і спати» Знизу: 👉 Також я через 5 хвилин: Бобер: «Але ж дерево саме просило!» 🪵😅"
B={}
e=0
for i in A.lower():
    print(i)
    if i.isalpha():
        if i not in B:
            B[i]=1
            print(B,"******************************************")
        else:
            B[i]+=1
print(B,"******************************************")






















