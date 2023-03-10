import random

def number_to_words(numero:int) -> str:
    if numero == 0:
        return 'Cero'
    elif numero == 1000:
        return 'Mil'
    elif numero == 1000000:
         return 'Un millon'

    en_palabras= ''
    
    unidades =['', 'uno','dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve']
    decenas = ['', 'dieci', 'veinti', 'treinta y ', 'cuarenta y ', 'cincuenta y ', 'sesenta y ', 'setenta y ', 'ochenta y ', 'noventa y ']
    centenas = ['', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos']
    unidades_millon = unidades_mil = unidades
    decenas_mil = decenas
    centenas_mil = centenas
    
    numero = '0' * (7-len(str(numero))) + str(numero)
    
    unidad = int(numero[-1])
    decena = int(numero[-2])
    centena = int(numero[-3])
    unidad_mil = int(numero[-4])
    decena_mil = int(numero[-5])
    centena_mil = int(numero[-6])
    unidad_millon = int(numero[-7])
    
    if len(numero) == 1:
        en_palabras = '{}'.format(unidades[unidad]).strip()
    if len(numero) == 2:
        en_palabras = '{}{}'.format(decenas[decena], unidades[unidad]).strip()
    if len(numero) == 3:
        en_palabras = '{}{}{}'.format(centenas[centena], decenas[decena], unidades[unidad]).strip()
    if len(numero) == 4:
        en_palabras = '{} mil {} {}{}'.format(unidades_mil[unidad_mil], centenas[centena], decenas[decena], unidades[unidad]).strip()
    elif len(numero) == 5:
        en_palabras = '{}{} mil {} {}{}'.format(decenas_mil[decena_mil], unidades_mil[unidad_mil], centenas[centena], decenas[decena], unidades[unidad]).strip()
    elif len(numero) == 6:
        en_palabras = '{} {}{} mil {} {}{}'.format(centenas_mil[centena_mil],decenas_mil[decena_mil] ,unidades_mil[unidad_mil], centenas[centena], decenas[decena], unidades[unidad]).strip()
    elif len(numero) == 7:
        en_palabras = '{} millones {} {}{} mil {} {}{}'.format(unidades_millon[unidad_millon], centenas_mil[centena_mil],decenas_mil[decena_mil] ,unidades_mil[unidad_mil], centenas[centena], decenas[decena], unidades[unidad]).strip()
    
 
    #casos especiales a cambiar:
    en_palabras = en_palabras.replace('dieciuno', 'once')
    en_palabras = en_palabras.replace('diecidos', 'doce')
    en_palabras = en_palabras.replace('diecitres', 'trece')
    en_palabras = en_palabras.replace('diecicuatro', 'catorce')
    en_palabras = en_palabras.replace('diecicinco', 'quince')
    en_palabras = en_palabras.replace('uno mil', 'un mil')
    en_palabras = en_palabras.replace('uno millones', 'un millon')

    
    #cuando termina en:
    if en_palabras.endswith('dieci'):
        en_palabras = en_palabras.replace('dieci', 'diez')
    elif en_palabras.endswith('veinti'):
        en_palabras = en_palabras.replace('veinti', 'veinte')
    elif en_palabras.endswith(' y'):
        en_palabras = en_palabras[:-2]
    elif en_palabras.endswith('ciento'):
        en_palabras = en_palabras.replace('ciento', 'cien')

    
    return en_palabras.capitalize() 


valor= random.randint(0, 9999999)
print(valor , "se escribe:", number_to_words(valor))
    