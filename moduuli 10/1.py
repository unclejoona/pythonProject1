class Talo():

    def __init__(self,ylinkerros,alinkerros,hissienmäärä):
        self.hissit =[]
        self.alinkerros = alinkerros
        for i in range(hissienmäärä):
            self.hissit.append(Hissi(ylinkerros,alinkerros))

    def aja_hissiä(self,kohdehissi,kerros):
        hissi = self.hissit[kohdehissi-1]
        hissi.siirry_kerrokseen(kerros)
    def palohälytys(self):
        print("Talossasi on palohälytys")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(self.alinkerros)
class Hissi():
    def __init__(self,ylinkerros,alinkerros):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.kerros = alinkerros

    def siirry_ylös(self):
        self.kerros += 1
        print(self.kerros)

    def siirry_alas(self):
        self.kerros -= 1
        print(self.kerros)

    def siirry_kerrokseen(self, kerros):
        if(kerros > self.ylinkerros or kerros < self.alinkerros):
            print("Virheellinen kerros")
            return
        if(kerros > self.kerros):
            self.siirry_kerrokseen(kerros-1)
            self.siirry_ylös()
        elif(kerros < self.kerros):
            self.siirry_kerrokseen(kerros+1)
            self.siirry_alas()

h = Hissi(5,0)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(0)
Talo