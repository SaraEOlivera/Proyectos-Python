import random
import os
import time

etapas_juego = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


def imprimir_titulo(titulo, caracter="*"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))
    time.sleep(1)
    print()
    print("Adivina la siguiente palabra:")
    time.sleep(1)

lista_palabra=["computadora", "novela", "corazon", "caminar", "velocidad", "dinosaurio", "mariposa", "lectura", "zapallo", "elefante", "peliculas", "viernes", "febrero", "cuarenta", "anillo", "pantalon", "amanecer", "primavera", "peludo", "minecraft", "capitulo", "salud", "estornudar", "dentista", "pizarron", "colores", "esmeralda", "tortuga", "hipo", "estomago", "milanesa", "pileta", "tormenta", "celeste", "frio", "agrio", "pomelo", "coliflor", "sirena"]
palabra_random = random.choice(lista_palabra)
palabras_con_espacios = []
for char in palabra_random:
      palabras_con_espacios.append(char + ' ')
      
letras_usadas = []

def adivinar_palabra():
      progreso = []
      errores = 0
      for i in range(len(palabra_random)):
            progreso.append("_ ")

      while errores < 7:
            if errores == 0:
                  time.sleep(.5)
                  print(etapas_juego[0])
            elif errores == 1:
                  time.sleep(.5)
                  print(etapas_juego[1])
            elif errores == 2:
                  time.sleep(.5)
                  print(etapas_juego[2])
            elif errores == 3:
                  time.sleep(.5)
                  print(etapas_juego[3])
            elif errores == 4:
                  time.sleep(.5)
                  print(etapas_juego[4])
            elif errores == 5:
                  time.sleep(.5)
                  print(etapas_juego[5])
            elif errores == 6:
                  print(etapas_juego[6])
                  time.sleep(1)
                  print(f"Perdiste! La palabra era {palabra_random}")
                  break
            print(''.join(progreso))
            print(f"Letras que ya ingresaste {letras_usadas}")
            print("Ingresa una letra: ")
            letra_usuario=input()
            if letra_usuario.isalpha() == False:
                  print("Caracter invalido. Ingresa una letra")
                  letra_usuario=input()
            if letra_usuario in letras_usadas:
                  print("!Esa letra ya la usaste!")
            else:
                  letras_usadas.append(letra_usuario)
                  
                  hay_error = True
                  for i in range(len(palabra_random)):
                        if letra_usuario == palabra_random[i]:
                              progreso[i] = letra_usuario + ' '
                              hay_error = False
                              
                  if hay_error:
                        errores += 1
                  
                  if palabras_con_espacios == progreso:
                        print(''.join(progreso))
                        time.sleep(1)
                        print(f"¡Ganaste! La palabra era {palabra_random}")                     
                        break
                  
                  
def jugar_de_nuevo():
      otra_vez = input("¿Jugamos de nuevo? [si / no] ")                                   
      if otra_vez.lower()=="si" or otra_vez.lower() == "s":
            os.system('cls')
            time.sleep(1)
            letras_usadas.clear()
            adivinar_palabra()
      else:
            print("Gracias por jugar.")
            time.sleep(1)
            os.system('cls')
            exit()
            
            
      
imprimir_titulo("Ahorcado")
adivinar_palabra()
jugar_de_nuevo()
