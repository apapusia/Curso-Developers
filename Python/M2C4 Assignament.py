import decimal
import math
#___ Exercise 1 ___
# Create a list
mi_lista=['perro','gato','elefante','hormiga']
# Create a tuple
mi_tupla=('perro','gato','elefante','hormiga')
# Create a float
dato_1=float(241.67)
# Create a integer
dato_2=241
# Create a decimal,
dato_3=decimal.Decimal(241.67)
# Create a  dictionary
mi_dict={
    'perro':'Zuri',
    'gato':'Argi',
    'elefante':'Totoro',
    'hormiga':'Carmen'
}
#___ Exercise 2 ___
dato_1_red=math.ceil(dato_1)

#___ Exercise 3 ___
dato_1_raiz=math.sqrt(dato_1)

#___ Exercise 4 ___
print(mi_dict['perro'])

#___ Exercise 5 ___
print(mi_tupla[1])
#___ Exercise 6 ___
mi_lista.extend(['caballo'])

#___ Exercise 7 ___
mi_lista[0]='delfin'

#___ Exercise 8 ___
mi_lista.sort()
print(mi_lista)
#___ Exercise 9 ___
mi_tupla+=('halcon',)
print(mi_tupla)

[]