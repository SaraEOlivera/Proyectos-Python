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
        respuesta_usuario = int(input("Ingresa '0' para piedra,'1' para papel o '2' para tijera: "))
        respuesta = random.randint(0, 2)

        if respuesta_usuario == 0 and respuesta == 1:
            puntaje_pc+=1
            print(f"Papel. ¡Te Gane! Vamos {puntaje_usuario} a {puntaje_pc}")
        elif respuesta_usuario == 0 and respuesta == 2:
            puntaje_usuario+=1
            print(f"Tijeras. ¡Me ganaste! Vamos {puntaje_usuario} a {puntaje_pc}")
        elif respuesta_usuario == 0 and respuesta == 0:
            print(f"Elejimos piedra. Vamos {puntaje_usuario} a {puntaje_pc}")
        
        if respuesta_usuario == 1 and respuesta == 0:
            puntaje_usuario+=1
            print(f"Piedra.¡Me ganaste! Vamos {puntaje_usuario} a {puntaje_pc}")
        elif respuesta_usuario == 1 and respuesta == 1:
            print(f"Elejimos papel. Vamos {puntaje_usuario} a {puntaje_pc}")
        elif respuesta_usuario == 1 and respuesta == 2:
            puntaje_pc+=1
            print(f"Papel. ¡Te gané! Vamos {puntaje_usuario} a {puntaje_pc}")  
            
        if respuesta_usuario == 2 and respuesta == 0:
            puntaje_pc +=1
            print(f"Piedra. ¡Te gané! Vamos {puntaje_usuario} a {puntaje_pc}")
        elif respuesta_usuario == 2 and respuesta == 1:
            puntaje_usuario += 1
            print(f"Piedra. ¡Me ganaste! Vamos {puntaje_usuario} a {puntaje_pc}")
        elif respuesta_usuario == 2 and respuesta == 2:
            print(f"Elegimos tijeras. Vamos {puntaje_usuario} a {puntaje_pc}")
            
        jugadas+=1
    
    if jugadas == 3 and puntaje_usuario == puntaje_pc:
        print(f"Ya jugamos {jugadas} veces. Empatamos {puntaje_pc} a {puntaje_pc}.")            
    if jugadas == 3 and puntaje_usuario > puntaje_pc:
        print(f"Ya jugamos {jugadas} veces. Me ganaste {puntaje_usuario} a {puntaje_pc}")
    if jugadas == 3 and puntaje_usuario < puntaje_pc:
        print(f"Ya jugamos {jugadas} veces. Te gané {puntaje_pc} a {puntaje_usuario}")
        
    jugar_de_nuevo = input("¿Jugamos de nuevo? s/n ")
    if jugar_de_nuevo.lower() == "s":
        jugar()
    else:
        print("Gracias por jugar conmigo ♥ ♥ ♥")
        exit()
        
        
imprimir_titulo("Rock Paper Scissors")
jugar()