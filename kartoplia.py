# A="шось смачненєке"
# print(A*5)
# B="Шось вже не смачненьке😱"
# # print(A[2:])
# print(ord("H"))
# print(chr(1))
# number="+1-234-567-89-10"
# print(number.replace("+"," "))
# pelmen=input("Введіть слово:")
# B=input("Введіть всоє ім'я:")
# for i in pelmen:
#     if i=="a" or i=="A":
#         print(B.replace("a",pelmen))
# print(A.isalpha())
# A=(input("Ведіть слово або цифра або слово з цифрами"))
# if A.isalpha():
#     print("Ваше слово складаєтся тільки з букв")
#     if A.islower():
#         print("Ваше слово складаєтся тільки з малих букв")
#     elif A.isupper():
#         print("Ваше слово склалається лише з великих букв")
#     else:
#         print("Ваше слово складаєтся з великих і малих букв")
# elif A.isdigit():
#     print("Ваше слово складаєтся лише з цифр")
# else:
#     print("ваше слово складаєься з букв і чисел")
# pelmen=("nenavishy NESPREVEDLIVIST")
# print(pelmen.split("h"))
# # C=0
# for i in pelmen:
#     if i.islower():
#         C+=1
# print(C)
# S=input("Введіть літеру яку ви хочете дублювати:")
# print(pelmen.replace(S,S*2))
# A="два плюс один дорівнює три бобра"
# B=(A.split(" "))
# C=0
# for i in B:
#     if "а" in i:
#         C+=1
# print(C)
# print(B)
# my_words=A.split(" ")
# for i in my_words:
#     print(i)
#     if A==A:
#         C+=1
# print(C)
# B=A.split(" ")
# C=0
# D=1000
# for i in B:
#     print(i)
#     if (len(i))>C:
#         C=(len(i))
#         print(C)
#     if D>(len(i)):
#         D=(len(i))
# print(D)
# A="abac lakeradsa barabolia waaaaaaaaa abac off vip kabac abac babak bardac"
# D=""
# C=0
# while True:
#     word = A.find("abac")
#     if word ==-1:
#         break
#     else:
#         A=A[word+4:]
#         C+=1
# print(C)
# # string="babakabacbabakkakakaaaakakaayabacvnage"
# C=0
# B=string.split("    ")
# for i in B:
#     if "abac" in string:
#         C+=1
#         print(C)
# for i in A:
#     print(i)
#     if A.startswith("abac"):
#         C+=1
# print(C)
#     print(i)
#     if "abac" in i:
#         C+=1
# A="pelmen bobr waaa barbara barabarebiririri walk vip"
# B=A.split(" ")
# C=0
# for i in B:
#     if (len(i))<=4:
#         C+=1
# # print(C)
# A="ядерочка на москву!"
# C=0
# P=["а","я","о","у","е","є","и","и","і","ї"]
# for i in A:
#     if i in P:
#         C+=1
# print(C)
# import random
# A=["пельмень","привет", "дратуте", "хеллоу", "mister", "jones"]
# C=[]
# while True:
#     number=random.randint(0,5)
#     if A[number] not in C:
#         C.append(A[number])
#     if (len(A))==(len(C)):
#         break
# print(C)
# A=(input("Введіть свого пельменя з фамілілею"))
# B=A.split(" ")
# for i in B:
#     print(B[0][0],'.',B[1][0])
# A=input("Введіть слово")
# if A[::-1]==A:
#     print("Ваше слово є паліндромом")
# else:
#     print("Ваше число не є паліндроном")
A="давай на кнф Устима"
for i in range(A,50000):
    print(A)