
# DESDE ACÁ LA PARTE DEL DICCIONARIO



def identificar_caracter_especial(texto):

    """Itera la cadena e identifica caracteres no alfabeticos. Ruy Mori"""

    # CORRECCION: Está bien la idea de querer identificar los caracteres especiales en el texto, pero en este caso está mal ejecutada, porque en esta función recorren todos los caracteres para
    # identificar los especiales; y luego, en "eliminar_caraceteres_especiales" vuelven a recorrer toda la lista para ponerlos en blanco.

    caracteres_especiales = []
    for palabra in texto:
        for caracter in palabra:
            if not caracter.isalpha():
                lista_caracteres_especiales(caracter, caracteres_especiales)
    return caracteres_especiales


def lista_caracteres_especiales(caracter, caracteres_especiales):

    """Arma una lista de caracteres especiales y numericos sin repetir (no contempla ' ' para simplificar tareas posteriores).
    Ruy Mori"""

    if caracter not in caracteres_especiales and caracter != " ":
        caracteres_especiales.append(caracter)
    return caracteres_especiales

def eliminar_caracteres_especiales(texto, caracteres_especiales):

    """Elimina los caracteres no alfabeticos de la cadena
    Ruy Mori"""

    LONGITUD1 = len(caracteres_especiales)
    for i in range(LONGITUD1):
            texto = texto.replace(caracteres_especiales[i], " ")
    return texto #esto deberia ser una linea del main() porque la funcion esta haciendo 2 cosas # CORRECCION: ver la correccion del fondo del archivo

def armar_lista_de_palabras(texto):

    """Arma la lista de palabras, sin repetir, todas en minuscula y de minimo 5 caracteres
    Ruy Mori"""

    lista_palabras_sin_repetir = []
    lista_palabras = texto.split(" ")
    for palabra in lista_palabras:
        if palabra.lower() not in lista_palabras_sin_repetir and palabra != '' and len(palabra) >= 5: # CORRECCION: Faltan constantes
            lista_palabras_sin_repetir.append(palabra.lower())
    return lista_palabras_sin_repetir

def armar_diccionario(texto):

    """Arma el diccionario con las palabras en orden alfabetico como claves, y cada una contiene la cantidad de veces que aparece en la cadena original
    Ruy Mori"""
    
    caracteres_especiales = identificar_caracter_especial(texto)
    texto = eliminar_caracteres_especiales(texto, caracteres_especiales).lower()
    lista_de_palabras = armar_lista_de_palabras(texto)
    diccionario_palabras = {}
    lista_ordenada = sorted(lista_de_palabras)
    for palabra in lista_ordenada:
        apariciones = texto.count(palabra)
        diccionario_palabras[palabra] = apariciones
    return diccionario_palabras
