def imprimir_titulo(titulo, caracter="º"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))

def mostrar_menu():
    print('Ingrese la operacion que desea realizar')    
    print('''
          - 1 para sumar
          - 2 para restar
          - 3 para multiplicar
          - 4 para dividir
          
          '''  
    )

def elegir_opcion():
    opcion = int(input('Opcion: ' ))
    numero1 = int(input('Ingrese el primer valor: '))
    numero2 = int(input('Ingrese el segundo valor: '))



def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2



imprimir_titulo("Calculadora de operaciones basicas")
mostrar_menu()
elegir_opcion()