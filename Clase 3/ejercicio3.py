peso = float(input('Ingrese su peso en kg: '))

altura = float(input('Ingrese su altura en metros: '))


masa_corporal = peso / altura**2

print('La masa corporal es',masa_corporal)

print('Redondeada:',round(masa_corporal, 2))