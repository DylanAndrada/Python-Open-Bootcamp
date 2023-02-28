
def año_biciesto(year):
    if year % 4 != 0:
        return False
    elif year % 100 !=0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True
    

if año_biciesto(int(input('Ingrese el año '))) == True:
    print('El año es año biciesto')

else:
    print('El año no es biciesto') 