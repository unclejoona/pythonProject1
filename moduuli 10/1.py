class Talo():

    def __init__(self,ylinkerros,alinkerros,hissienmäärä):
        self.ylinkerros = ylinkerros
        self.alinkerros = alinkerros
        self.hissit =[]
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
