
# P=["фарш","тісто","каструля","вода","сіль","сметанка","."]
# P.insert(2,"котофєй котофєєвич котофа")
# m=P.pop(7)
#
# print(P)
N=int(input("Введіть чому дорівнює число N:"))
P=[]
for i in range(N):
    P.append(i*2+1)
print(P)
print(len(P))
