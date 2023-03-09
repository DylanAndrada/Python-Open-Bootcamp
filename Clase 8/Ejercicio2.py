import pickle

path = "Clase 8\vehiculo.txt"

class Vehiculo:
        color: str
        velocidad: int
        
        def __init__(self):
                
                self.color = None
                self.velocidad = None
        
        def set_color(self,x):
               self.color = x
        
        def __str__(self):
               
               return(f"El auto color {self.color} tiene una velocidad de {self.velocidad}")

def do_file():
        with open(r"Clase 8\vehiculo.txt", 'wb') as tx:
             v = Vehiculo()
             pickle.dump(v,tx)
             tx.close

def load_file():
       with open(r"Clase 8\vehiculo.txt", 'rb') as tx:
              v = pickle.load(tx)
              v.set_color("rojo")
              print(v)


do_file()
load_file()