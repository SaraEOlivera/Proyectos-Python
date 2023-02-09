def imprimir_titulo(titulo, caracter="*"):
    print(caracter * len(titulo))
    print(titulo)
    print(caracter * len(titulo))
    
def imprimir_juego():

    noun = input("Insert a noun ")
    adjective = input("Insert an adjective ")
    verb = input("Insert a verb ")
    adjective2 = input("Insert an adjective ")

    print(f"El otro día me encontré con un {adjective} {noun} y lo invité a {verb}. La pasamos {adjective2}")
    



imprimir_titulo("Mad libs generator")
imprimir_juego()
