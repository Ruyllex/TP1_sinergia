
# DESDE ACÁ LA PARTE DEL DICCIONARIO
import string


def eliminar_caracteres_especiales(texto):

    """Elimina los caracteres no alfabeticos de la cadena
    Ruy Mori"""
    caracteres_especiales=list(string.punctuation)
    LONGITUD1 = len(caracteres_especiales)
    for i in range(LONGITUD1):
            texto = texto.replace(caracteres_especiales[i], " ")
    return texto

def armar_lista_de_palabras(texto, lista_palabras_sin_repetir):

    """Arma la lista de palabras, sin repetir, todas en minuscula y de minimo 5 caracteres
    Ruy Mori"""

    lista_palabras_sin_repetir = []
    for palabra in texto:
        if palabra.lower() not in lista_palabras_sin_repetir and palabra != '' and len(palabra) >= 5: # CORRECCION: Faltan constantes
            lista_palabras_sin_repetir.append(palabra.lower())
    return lista_palabras_sin_repetir

def armar_diccionario(lista_de_palabras, texto):

    """Arma el diccionario con las palabras en orden alfabetico como claves, y cada una contiene la cantidad de veces que aparece en la cadena original
    Ruy Mori"""

    diccionario_palabras = {}
    lista_ordenada = sorted(lista_de_palabras)
    for palabra in lista_ordenada:
        apariciones = texto.count(palabra)
        diccionario_palabras[palabra] = apariciones
    return diccionario_palabras
