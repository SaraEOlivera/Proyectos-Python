tablero = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
]

# print en formato tablero:
def imprimir_tablero(tablero):
    for fila in tablero:
        for elem in range(len(fila)):
            if elem == len(fila) -1:
                print(fila[elem], end='\n')
            else:
                print(fila[elem], end='  ')


imprimir_tablero(tablero)