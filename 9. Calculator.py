import time, os


def imprimir_titulo(titulo, caracter="*"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))
    time.sleep(1)

def mostrar_menu():
    print('Ingrese la operacion que desea realizar')    
    print('''
          - 1 para sumar
          - 2 para restar
          - 3 para multiplicar
          - 4 para dividir
          - 5 para salir del programa
          
          '''  
    )
    
    
def check_opcion():
    while True:
        try:
            opcion=int(input("Ingrese una opcion "))
            break
        except ValueError:
            print("Numero invalido. Intente de nuevo")
            
    if opcion < 0 or opcion < 5:
        numero_1 = int(input("Ingrese el primer valor: "))    
        numero_2 = int(input("Ingrese el segundo valor: "))
    if opcion == 1:
        sumar(numero_1, numero_2)
    if opcion == 2:
        restar(numero_1, numero_2)
    if opcion == 3:
        multiplicar(numero_1, numero_2)
    if opcion == 4:
        dividir(numero_1, numero_2)
    if opcion == 5:
        os.system('cls')
        exit()
    if opcion < 1 or opcion > 5:
        print("La opcion ingresada no es correcta.")


def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"La suma de ambos numeros es igual a {resultado}")

def restar(numero1, numero2):
    resultado = numero1 - numero2
    print(f"La resta de ambos numeros es igual a {resultado}")

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    print(f"La multiplicacion de ambos numeros es igual a {resultado}")

def dividir(numero1, numero2):
    resultado = numero1 / numero2
    print(f"La division de ambos numeros es igual a {resultado}")

def elegir_otra_operacion():
      otra_vez = input("¿Desea realizar otra operacion? [si / no] ")                                   
      if otra_vez.lower()=="si" or otra_vez.lower() == "s":
            os.system('cls')
            time.sleep(1)
            mostrar_menu()
            check_opcion()
      if otra_vez.lower() == "no" or otra_vez.lower() == "n":
            print("Gracias")
            time.sleep(1)
            os.system('cls')
            exit()

imprimir_titulo("Calculadora de operaciones basicas")
mostrar_menu()
check_opcion()
elegir_otra_operacion()