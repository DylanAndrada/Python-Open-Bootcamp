from functools import reduce

lista = [2,4,5,8,9,13]


par = list(filter(lambda x: x % 2 == 0, lista))
suma = reduce(lambda x, y: x + y, par)
print(suma)