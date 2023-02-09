import random

def imprimir_titulo(titulo, caracter="♥"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))
    
def adivinar_numero():
    intento = 0
    respuesta = random.randint(1, 20)
    while intento < 3:
        respuesta_usuario = int(input("¡Solo 3 intentos! Ingrese un numero entre 1 - 20: "))
        if respuesta_usuario < respuesta or respuesta_usuario > respuesta:
            print(f"{respuesta_usuario} no es el numero")
        if respuesta_usuario == respuesta:
            print(f"¡Adivinaste! El numero era {respuesta_usuario}")
            break
        intento+=1
    if intento == 3:
        print(f"Perdiste! El numero era {respuesta}")

    
imprimir_titulo("Number Guessing")
adivinar_numero()


    





