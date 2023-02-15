import random

def imprimir_titulo(titulo, caracter="º"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))


def jugar():
    jugadas = 0
    puntaje_usuario = 0
    puntaje_pc = 0
    while jugadas < 3:
        try:
            respuesta_usuario = int(input("Ingresa '0' para piedra,'1' para papel o '2' para tijera: "))
            respuesta = random.randint(0, 2)
            
            if respuesta_usuario < 0 or respuesta_usuario > 2:
                raise ValueError("Tenes que ingresar un numero entre el 0 y el 2")

            if respuesta_usuario == 0 and respuesta == 1:
                puntaje_pc+=1
                print(f"Papel. ¡Te Gane! Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F60E")
            elif respuesta_usuario == 0 and respuesta == 2:
                puntaje_usuario+=1
                print(f"Tijeras. ¡Me ganaste! Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F608")
            elif respuesta_usuario == 0 and respuesta == 0:
                print(f"Elejimos piedra. Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F610")
            
            if respuesta_usuario == 1 and respuesta == 0:
                puntaje_usuario+=1
                print(f"Piedra.¡Me ganaste! Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F608")
            elif respuesta_usuario == 1 and respuesta == 1:
                print(f"Elejimos papel. Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F610")
            elif respuesta_usuario == 1 and respuesta == 2:
                puntaje_pc+=1
                print(f"Papel. ¡Te gané! Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F60E")  
                
            if respuesta_usuario == 2 and respuesta == 0:
                puntaje_pc +=1
                print(f"Piedra. ¡Te gané! Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F60E")
            elif respuesta_usuario == 2 and respuesta == 1:
                puntaje_usuario += 1
                print(f"Piedra. ¡Me ganaste! Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F608")
            elif respuesta_usuario == 2 and respuesta == 2:
                print(f"Elegimos tijeras. Vamos {puntaje_usuario} a {puntaje_pc}, \U0001F610")
                
            jugadas+=1
        
        except ValueError as error:
            print("Esa no es una opcion correcta, \U0001F643")
            print(error)
    
    if jugadas == 3 and puntaje_usuario == puntaje_pc:
        print(f"Ya jugamos {jugadas} veces. Empatamos {puntaje_pc} a {puntaje_pc}. \U0001F610")            
    if jugadas == 3 and puntaje_usuario > puntaje_pc:
        print(f"Ya jugamos {jugadas} veces. Me ganaste {puntaje_usuario} a {puntaje_pc}, \U0001F608. Ganaste la \U0001F3C6!")
    if jugadas == 3 and puntaje_usuario < puntaje_pc:
        print(f"Ya jugamos {jugadas} veces. Te gané {puntaje_pc} a {puntaje_usuario}, \U0001F60E. La \U0001F3C6 es mía!!")
    
    
    jugar_de_nuevo = input("¿Jugamos de nuevo? Ingresa 'si' o 'no' ")
    if jugar_de_nuevo.lower() == "s":
        print("\U0001F60D")
        jugar()
    else:
        print("Gracias por jugar conmigo \U0001F497")
        exit()
        
        
imprimir_titulo("Piedra, papel o tijera")
jugar()