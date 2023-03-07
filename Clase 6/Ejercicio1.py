class Vehiculo:
    color: str
    ruedas:int
    puertas: int

    def get_color(self):
        print(self.color)

    def set_color(self,c):
        self.color = c

    def get_ruedas(self):
        print(self.ruedas)
    
    def set_ruedas(self,r):
        self.ruedas = r

    def get_puertas(self):
        print(self.puertas)

    def set_puertas(self,p):
        self.puertas = p

class Auto(Vehiculo):
    velocidad: int
    cilindrada: int


    def get_velocidad(self):
        print(self.velocidad)

    def set_velocidad(self,v):
        self.velocidad = v
    
    def get_cilindrada(self):
        print(self.cilindrada)

    def set_cilindrada(self,cil):
        self.cilindrada = cil

    def crear_auto(self,v,cil,c,r,p):
        self.set_velocidad(v)
        self.set_cilindrada(cil)
        self.set_color(c)
        self.set_ruedas(r)
        self.set_puertas(p)

    def mostrar_auto(self):
        print("El auto color:",self.color,"con",self.puertas, "puertas y",self.ruedas, "ruedas.",
              "Tiene una velocidad de", self.velocidad, "y cilindrada de", self.cilindrada)
        
a = Auto()
a.crear_auto(180,50,"rojo",4,4)
a.get_velocidad()
a.mostrar_auto()
