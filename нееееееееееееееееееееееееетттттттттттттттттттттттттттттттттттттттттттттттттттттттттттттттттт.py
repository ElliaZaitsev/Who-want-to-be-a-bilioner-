import random
class Chaynik:
    def __init__(self,name,volume,stan,mode):
        self.name=name
        self.volume=volume
        self.stan=stan
        self.mode=mode
        self.dumplingnumber=str(random.randrange(1,100,2))+random.choice(["E","R","F","A","S","M","N","K","L","O","P","Z","X"])
    def info(self):
        print(self.name,self.volume,self.stan,self.mode,self.dumplingnumber)
    def on(self):
        self.stan="включений режим пельмень"
    def off(self):
        self.stan="виключений режим пельмень😭😭😭"
    def IMAFLASH(self):
        self.mode="ААААААААА ЧАЙНІК СТАВ СУПЕР БИСТРИМ ВАРЕНИКОООММММ ААААААААААААААААА"
