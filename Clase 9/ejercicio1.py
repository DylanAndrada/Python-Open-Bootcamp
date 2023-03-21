
def elegir_paises():

    mi_set= set()
    x=0

    for x in range(5):
        pais = (input('Ingrese un pais: '))
        mi_set.add(pais)
        x =+ 1
    
    new_set = sorted(list(mi_set))

    return(print(new_set))


elegir_paises()