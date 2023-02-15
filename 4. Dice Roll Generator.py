import random
import os

def imprimir_titulo(titulo, caracter="§"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))

def arrojar_dados():
    while True:
        
        try:
            cantidad_dados = int(input("¿Cuántos dados? [1 / 2] "))
            
            if cantidad_dados < 1 or cantidad_dados > 2:
                raise ValueError("Tenes que elegir entre 1 ó dos dados...")
            
            if cantidad_dados == 1:
                dado1 = random.randint(1,6)
                resultado = dado1
                print(f"El resultado es {resultado}")
            if cantidad_dados == 2:
                dado1 = random.randint(1,8)
                dado2 = random.randint(1,8)
                resultado = dado1 + dado2
                print(f"Primer dado: {dado1}")
                print(f"Segundo dado: {dado2}")
                print(f"Total: {resultado}")
                
        except ValueError as error:
            print("El numero que ingresaste no es correcto.")
            print(error)
            
        otra_vez = input("¿Tirar de nuevo? Si / No ")
        if otra_vez.lower() == "si":
            os.system('cls' if os.name == 'nt' else 'clear')
            arrojar_dados()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        
        
            
    




arrojar_dados()
