# A=True
# bobr=["dumplings top","i love dumplings","flick","dumplings fat but delicios",1,"flick","super bobrik"]
# pelmen=[]
# for i in bobr:
#     if i =='flick':
#         A=not A
#     pelmen.append(A)
# print(pelmen)
# A=[1,5,3,7,6]
# B=[]
# C=0
# # for i in A:
# #     print(i**2)
# #     B.append(i**2)
# # for i in B:
# #     C+=i
# #     print(C)
# for i in A:
#     C+=i**2
# print(C)
A=[1,5,26,38,48,13,64,31,76,11,93,100]
C=0
kartoplia=0
for i in A:
    if i>=60:
        kartoplia+=1
        print(kartoplia)
    if i>60:
        C+=i
        print(C)