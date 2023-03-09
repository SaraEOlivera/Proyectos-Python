import time, os


def imprimir_titulo(titulo, caracter="*"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))
    print()
    time.sleep(1)
    

imprimir_titulo("Cuenta regresiva")   

while True:
    try:
        numero = int(input('Ingrese un numero: '))
        assert numero > 0
        break
    except ValueError:
        print("Numero invalido. Intente de nuevo")
    except AssertionError :
        print("El numero es negativo")
            
for num in range(1, numero+1):
    time.sleep(1)
    print(numero - num)
print(f"Hasta la vista, baby, \U0001F60E")
time.sleep(2)
os.system('cls')