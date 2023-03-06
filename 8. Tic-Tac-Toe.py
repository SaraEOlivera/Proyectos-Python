import os
import time

tablero = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
]


#Titulo juego
def imprimir_titulo(titulo, caracter="*"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo),)
    print()
    

# print en formato tablero:
def imprimir_tablero(tablero):
    for fila in tablero:
        for elem in range(len(fila)):
            if elem == len(fila) -1:
                print(fila[elem], end='\n')
            else:
                print(fila[elem], end='  ')


#cambia el tablero segun jugadas

def cambiar_tablero(tablero, posicion, turno_jugador):
    if turno_jugador:
        simbolo = 'x'
    else:
        simbolo = 'o'
    
    #ubicar simbolo x/o en la posicion que el jugador quiera:
    if posicion == 1:
        if tablero[4][0] == ' ':
            tablero[4][0] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 2:
        if tablero[4][2] == ' ':
            tablero[4][2] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 3:
        if tablero[4][4] == ' ':
            tablero[4][4] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 4:
        if tablero[2][0] == ' ':
            tablero[2][0] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 5:
        if tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 6:
        if tablero[2][4] == ' ':
            tablero[2][4] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 7:
        if tablero[0][0] == ' ':
            tablero[0][0] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 8:
        if tablero[0][2] == ' ':
            tablero[0][2] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    elif posicion == 9:
        if tablero[0][4] == ' ':
            tablero[0][4] = simbolo
            return 0
        else:
            return 'Ese lugar esta ocupado'
    else:
        return 'Ese lugar está fuera del tablero'


def quien_gano(tablero):
    #chequear fila seguida de simbolo en todas direcciones 
    for simbolo in ['x', 'o']:
        fila_0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero[0][4] == simbolo
        fila_2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero[2][4] == simbolo
        fila_4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero[4][4] == simbolo
        columna_0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero[4][0] == simbolo
        columna_2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero[4][2] == simbolo
        columna_4 = tablero[0][4] == simbolo and tablero[2][4] == simbolo and tablero[4][4] == simbolo
        diagonal_1 = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero[0][4] == simbolo
        diagonal_2 = tablero[4][4] == simbolo and tablero[2][2] == simbolo and tablero[0][0] == simbolo
        
        if fila_0 or fila_2 or fila_4 or columna_0 or columna_2 or columna_4 or diagonal_1 or diagonal_2:
            if simbolo == 'x':
                return 1
            elif simbolo == 'o':
                return 2
            break

turno1 = True
jugador_1 = ''
jugador_2 = ''
cant_turnos = 0

""" def resetear_tablero(tablero):
    for simbolo in ['x', 'o']:
            if tablero[4][0] == simbolo:
                tablero[4][0] = ' '
            elif tablero[4][2] == simbolo:
                tablero[4][2] = ' '
            elif tablero[4][4] == simbolo:
                tablero[4][4] = ' '
            elif tablero[2][0] == simbolo:
                tablero[2][0] = ' '
            elif tablero[2][2] == simbolo:
                tablero[2][2] = ' '
            elif tablero[2][4] == simbolo:
                tablero[2][4] = ' '
            elif tablero[0][0] == simbolo:
                tablero[0][0] = ' '
            elif tablero[0][2] == simbolo:
                tablero[0][2] = ' '
            elif tablero[0][4] == simbolo:
                tablero[0][4] = ' '
            cant_turnos = 0
                

def jugar_de_nuevo():
      otra_vez = input("¿Jugamos de nuevo? [si / no] ")                                   
      if otra_vez.lower()=="si" or otra_vez.lower() == "s":
            os.system('cls')
            time.sleep(1)
            resetear_tablero(tablero)
      if otra_vez.lower() == "no" or otra_vez.lower() == "n":
            print("Gracias por jugar.")
            time.sleep(1)
            os.system('cls')
            exit()
 """

imprimir_titulo("Tatetí")
imprimir_tablero(tablero)

while cant_turnos < 9:
    if jugador_1 == '':
        print('El primer jugador utiliza "x" para jugar. Ingresa tu nombre:')
        jugador_1 = input()
        print('El segundo jugador utiliza "o" para jugar. Ingresa tu nombre:')
        jugador_2 = input()
    else:
        if turno1:
            print(f"{jugador_1} elegí una posicion entre 1-9 (el primer cuadrito de abajo es la posición 1)")
        else:
            print(f"{jugador_2} elegí una posicion entre 1-9 (el primer cuadrito de abajo es la posición 1)")
            
        posiciones = int(input())
        
        valor = cambiar_tablero(tablero, posiciones, turno1)
        if valor == 0:
            turno1 = not turno1
            cant_turnos+=1
            imprimir_tablero(tablero)
            if quien_gano(tablero) == 1:
                print(f"Gano {jugador_1}!")
                time.sleep(1)
                print("Gracias por jugar.")
                time.sleep(1)
                os.system('cls')
                exit()
            elif quien_gano(tablero) == 2:
                print(f"Gano {jugador_2}!")
                time.sleep(1)
                print("Gracias por jugar.")
                time.sleep(1)
                os.system('cls')
                exit()
        else:
            print(valor)
        if cant_turnos == 9:
            print("Empate...")
            print("Gracias por jugar.")
            time.sleep(1)
            os.system('cls')
            exit()
    

imprimir_tablero(tablero)
# jugar_de_nuevo()
