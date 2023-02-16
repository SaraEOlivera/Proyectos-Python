import time
import os
import random

etapas_juego  = ['''
                 |=======
                 |      |
                 |
                 |
                 |
                 |
                 ''',
                 '''
                 |========
                 |       |
                 |       0
                 |
                 |
                 |
                 ''',
                 '''
                 |========
                 |       |
                 |       0
                 |       |
                 |
                 |
                 ''',
                 '''
                 |========
                 |       |
                 |       0
                 |      /|
                 |
                 |
                 ''',
                 '''
                 |========
                 |       |
                 |       0
                 |      /|\\
                 |
                 |                
                 ''',
                 '''
                 |========
                 |       |
                 |       0
                 |      /|\\
                 |      /
                 |                
                 ''',
                 '''
                 |========
                 |       |
                 |       0
                 |      /|\\
                 |      / \\
                 |                
                 '''
    ]

def imprimir_titulo(titulo, caracter = "*"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))
    print()
    time.sleep(1)
    print("Adivina la siguiente palabra")

lista_palabra=["computadora", "novela", "corazon", "caminar", "velocidad", "dinosaurio", "mariposa", "lectura", "zapallo", "elefante", "peliculas", "viernes", "febrero", "cuarenta", "anillo", "pantalon", "amanecer", "primavera", "peludo", "minecraft", "capitulo", "salud", "estornudar", "dentista", "pizarron", "colores", "esmeralda", "tortuga", "hipo", "estomago", "milanesa", "pileta", "tormenta", "celeste", "frio", "agrio", "pomelo", "coliflor", "sirena"]
letras_usadas = []

def adivinar_palabra():
    palabra_aleatoria = random.choice(lista_palabra)
    palabra_espaciada = []
    for char in palabra_aleatoria:
        palabra_espaciada.append(char + ' ')    
    progreso=[]
    errores = 0
    for i in range(len(palabra_aleatoria)):
        progreso.append("_ ")
        
    while errores < 7:
        if errores == 0:
            print(etapas_juego[0])
        elif errores == 1:
            print(etapas_juego[1])
        elif errores == 2:
            print(etapas_juego[2])
        elif errores == 3:
            print(etapas_juego[3])
        elif errores == 4:
            print(etapas_juego[4])
        elif errores == 5:
            print(etapas_juego[5])
        elif errores == 6:
            print(etapas_juego[6])
            time.sleep(0.5)
            print(f"Perdiste. La palabra era {palabra_aleatoria}")
            jugar_de_nuevo()
            break
        
        print(''.join(progreso))
        print(f"Letras usadas: {letras_usadas}")
        print("Ingresa una letra:")
        letra_usuario = input()
        if letra_usuario.isalpha():
            if letra_usuario in letras_usadas:
                print("Ese letra ya la ingresaste")
            else:
                letras_usadas.append(letra_usuario)
                
                un_error = True
                for i in range(len(palabra_aleatoria)):
                    if letra_usuario == palabra_aleatoria[i]:
                        progreso[i] = letra_usuario + ' '
                        un_error = False
            
            if un_error:
                errores+=1
            
            if palabra_espaciada == progreso:
                print(''.join(progreso))
                time.sleep(0.5)
                print(f"¡¡Ganaste!! La palabra era {palabra_aleatoria}")
                jugar_de_nuevo()
                break


def jugar_de_nuevo():
    otra_vez = input("¿Jugamos de nuevo? [si/no] ")    
    if otra_vez.lower() == "si" or otra_vez.lower() == "s":
        os.system('cls')
        time.sleep(1)
        letras_usadas.clear()
        adivinar_palabra()
    if otra_vez.lower() == "no" or otra_vez.lower() == "n":
        print("Gracias por jugar")
        time.sleep(1)
        os.system('cls')
        exit()
    
    
imprimir_titulo("El ahorcado")
adivinar_palabra()
jugar_de_nuevo()