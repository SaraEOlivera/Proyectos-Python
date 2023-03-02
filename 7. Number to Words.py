# 1. Definir lista de unidades, decenas, centenas. ok
# 2. Lograr una funcion que lea el primer bloque 
# 3. Realizar funcion que separe el numero en bloques de 3.
#   a. Bloque 1: lee centenas decenas unidades  --> 999
#   b. Bloque 2: lee bloque 2 + "miles" + bloque 1  999.999  
#   c. Bloque 3: lee bloque 3 + "milones" + bloque 2
# 4. Revisar casos especiales
import random

unidades = ['', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve',]
decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ', 'sesenta y ', 'setenta y', 'ochenta y ', 'noventa y ',]
centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos',]


def leer_numeros_bloque_dos(numero):
    en_palabras = ''
    numero = '0' *(3-len(str(numero))) + str(numero)
            
    unidad = int(numero[-1])
    decena = int(numero[-2])
    centena = int(numero[-3])
    numero = str(numero)
    en_palabras = '{} {}{} mil'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()
        
    return en_palabras.capitalize()


def leer_numeros_bloque_uno(numero):
    
    if numero == 0:
        return 'Cero'
    elif numero == 100:
        return 'Cien'
    
    numero_en_palabras = ''

    
    numero = '0' *(3-len(str(numero))) + str(numero)
    
    unidad = int(numero[-1])
    decena = int(numero[-2])
    centena = int(numero[-3])
    if len(numero) > 3:
        return leer_numeros_bloque_dos(numero)
    numero = str(numero)
    numero_en_palabras = '{} {}{}'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()
    
    numero_en_palabras = numero_en_palabras.replace('dieciuno', 'once')
    numero_en_palabras = numero_en_palabras.replace('diecidos', 'doce')
    numero_en_palabras = numero_en_palabras.replace('diecitres', 'trece')
    numero_en_palabras = numero_en_palabras.replace('diecicuatro', 'catorce')
    numero_en_palabras = numero_en_palabras.replace('diecicinco', 'quince')
    
    if numero_en_palabras.endswith('dieci'):
        numero_en_palabras = numero_en_palabras.replace('dieci', 'diez')
    elif numero_en_palabras.endswith('veinti'):
        numero_en_palabras = numero_en_palabras.replace('veinti', 'veinte')
    elif numero_en_palabras.endswith(' y'):
        numero_en_palabras = numero_en_palabras[:-2] 
            
    return numero_en_palabras.capitalize()




#valor = random.randint(0, 99999)
valor = 773614
print(valor[0])
#print (leer_numeros_bloque_dos(valor))
print(leer_numeros_bloque_uno(valor))
    
    

        
    