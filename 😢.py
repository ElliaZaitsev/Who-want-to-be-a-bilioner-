import random
X=0
Bobrik=0
Xaxaxa=0
Bobr=0
while True:
    A = input("Чи будемо ми кидати кубик?")
    if A=="так":
        X=random.randint(1,6)
        print(X,"Player№1 випав такий кубик")
        Bobrik+=X
        print(Bobrik,"Player№1 знаходитесь на цій клітині")
        if Bobrik==20 or Bobrik==43 or Bobrik==31 or Bobrik==18:
            Bobrik-=5
            print("player№1 втратив 15 очок!")
            print(Bobrik,"player№1 знаходитесь на цій клітині")
        if Bobrik>=50:
            print("Player№1 виграв!")
    else:
        print("Ну не повезло не фартануло")
    A = input("Чи будемо ми кидати кубик?")
    if A == "так":
        Xaxaxa = random.randint(1, 6)
        print(Xaxaxa, "Player№2 випав такий кубик")
        Bobr += Xaxaxa
        print(Bobr, "Player№2 знаходитесь на цій клітині")
        if Bobr == 20 or Bobrik == 43 or Bobrik == 31 or Bobrik == 18:
            Bobr-=5
            print(Bobr,"player№2 знаходитесь на цій клітині")
        if Bobr >= 50:
            print("Player№2 виграв!")
    else:
        print("Ну не повезло не фартануло")
