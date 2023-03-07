class Alumno:
    nombre: str
    nota: float

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_alumno(self):
        print("Nombre:",self.nombre, "- Nota:",self.nota)

    def calcular_nota(self):
        if self.nota >= 6:
            print("El alumno aprobo")
        else:
            print("El alumno desaprobo")


a = Alumno('Juan',5)
a.mostrar_alumno()
a.calcular_nota()

