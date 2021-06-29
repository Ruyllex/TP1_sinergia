
#---------CUERPO DE FUNCIONES---------------#

def esconder_palabra(palabra):

    """Crea una de cadena formada por el simbolo ´?´ de la misma longitud que
    la palabra ingresada. Joaquín Maguiña
    """

    palabra_secreta = ""

    for caracter in palabra:
        palabra_secreta += "?"

    return palabra_secreta


def posicion_letra_en_palabra(letra, palabra_adivinar):

    """Devuelve la posición de una letra o
    letras repetidas que ya se encuentran en palabra. Joaquín Maguiña"""

    lista_posicion = []
    for i in  range(len(palabra_adivinar)):
        if palabra_adivinar[i] == letra:
            lista_posicion.append(i)
    return lista_posicion

def ingresar_letra_en_lista_secreta(letra, lista_secreta, lista_posicion):

    """Ingresa la letra a la lista secreta en la posición correspondiente. Joaquín Maguiña"""

    for i in lista_posicion:
        lista_secreta[i] = letra
    return lista_secreta

def validar_nombres():
    
    """Crea una lista con los nombres validos ingresados por los usuarios. Jorge Sedek"""
    
    nombres = []
    print("Pueden jugar hasta 5 jugadores. Cuando haya ingresado todos los nombres ingrese ENTER")
    i = 1
    nombre = 1
    while nombre !="" and i != 6:
        
        nombre = input("Ingrese el nombre del jugador {} : ".format(i))
        if nombre != "":
            if nombre not in nombres:
                nombres.append(nombre)
                i += 1
            else:
                print("Nombre ya ingresado")
        
        
    return nombres

    