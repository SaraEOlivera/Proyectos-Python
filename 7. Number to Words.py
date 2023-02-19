import random

def number_to_words(numero:int) -> str:
    if numero == 0:
        return 'Cero'
    en_palabras= ''
    unidades =['', 'uno','dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ', 'sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y ']
    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
    
    # descomponer el numero. Hay que completar con 0 a la izquierda segun cantidad digitos
    # la 1° expresion rellena con 0 si hay menos de 3 digitos y a esto le agrega el numero
    numero = '0' * (3-len(str(numero))) + str(numero)
    
    # Convertir cada digito str a int:
    unidad = int(numero[-1])
    decena = int(numero[-2])
    centena = int(numero[-3])
    
    # Strip saca espacio en blanco al tener 2 o 1 digito
    en_palabras = '{} {}{}'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()
    
    
    #casos especiales a cambiar:
    en_palabras = en_palabras.replace('dieciuno', 'once')
    en_palabras = en_palabras.replace('diecidos', 'doce')
    en_palabras = en_palabras.replace('diecitres', 'trece')
    en_palabras = en_palabras.replace('diecicuatro', 'catorce')
    en_palabras = en_palabras.replace('diecicinco', 'quince')
    
    #cuando termina en:
    if en_palabras.endswith('dieci'):
        en_palabras = en_palabras.replace('dieci', 'diez')
    elif en_palabras.endswith('veinti'):
        en_palabras = en_palabras.replace('veinti', 'veinte')
    elif en_palabras.endswith(' y'):
        en_palabras = en_palabras[:-2]
    elif en_palabras.endswith('ciento'):
        en_palabras = en_palabras.replace('ciento', 'cien')
    
    
    
    return en_palabras.capitalize() #imprime en mayuscula la primera letra


valor = random.randint(0, 999)
print(valor , "se escribe:", number_to_words(valor))
    