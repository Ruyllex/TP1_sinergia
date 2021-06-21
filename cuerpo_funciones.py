
#---------CUERPO DE FUNCIONES---------------#

def esconder_palabra(palabra):

    """Crea una de cadena formada por el simbolo ´?´ de la misma longitud que
    la palabra ingresada. Joaquín Maguiña
    """

    palabra_secreta = ""

    for caracter in palabra:
        palabra_secreta += "?"

    return palabra_secreta

#comentario 1
def lista_a_cadena(lista):

    """Convierte una lista en una cadena. Joaquín Maguiña"""

    # CORRECCION: No es necesaria esta función, se puede pasar de una lista a una cadena con " "".join(lista) "

    cadena = ""
    for caracter in lista:
        cadena += caracter

    return cadena

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
