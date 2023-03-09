import os

path = "Clase 8\myfile.txt"
isfile = os.path.isfile(path)

def create_file():
        with open(r"Clase 8\myfile.txt", 'x') as tx:
             tx.write('Me he creado\n')

def write_file():

    with open(r"Clase 8\myfile.txt", 'a') as tx:
        texto = "Hola Mundo\n"
        tx.write(texto)
    

def __main__():

    create_file()
    write_file()
    


if __name__ == '__main__':
    
    __main__()
    

