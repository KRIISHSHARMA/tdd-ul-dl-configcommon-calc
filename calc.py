class Slotconfig : 
    def __init__(self , ds , us , tp , scs):
        self.ds = ds
        self.us = us
        self.tp = tp
        self.scs = scs
    def slotc(self):
        ts = self.tp * (2**self.scs)
        spc = ts - (self.ds+self.us)
        l = []
        for i in range(int(self.ds)) : 
            l.append('D')
        for i in range(int(spc)) :
            l.append('S')
        for i in range(int(self.us)) :
            l.append('U')
        
        print(l)
ds = int(input("ENTER DL SLOT ::  "))
us = int(input("ENTER UL SLOT ::  "))
tp = float(input("ENTER TRASMISSION PERIODICITY :: "))
scs = int(input("ENTER SCS (0 = 15 , 1 = 30 , 2 = 60 , 3 = 120) :: "))
pattern1 = Slotconfig(ds,us,tp,scs)
pattern1.slotc()
