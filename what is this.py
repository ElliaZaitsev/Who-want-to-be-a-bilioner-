clonbobra={}
BOBR=("пельмень")
for i in BOBR:
    print(i)
    if i in clonbobra:
        clonbobra[i]+=1
    else:
        clonbobra[i]=1
print(clonbobra)
print(BOBR)
BOBR["age"]=456
print(BOBR)
BOBR["work"]="bobr police"
for i in BOBR:
    print(BOBR[i])