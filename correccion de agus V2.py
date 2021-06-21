#-----------GRUPO: SINERGIA------------------#

"""
    Integrantes:
        
    -Jorge Sedek
    -Zoilo Pazos
    -Joaquín Maguiña
    -Leonardo Ayuso
    -Ruy Mori
    -Agustín Sánchez Vergara

    Fecha: 1° Cuatrimestre del 2021
    
"""

#------------CUERPO DE FUNCIONES---------------#

def esconder_palabra(palabra):

    """Crea una de cadena formada por el simbolo ´?´ de la misma longitud que
    la palabra ingresada
    """

    palabra_secreta = ""

    for caracter in palabra:
        palabra_secreta += "?"

    return palabra_secreta

def lista_a_cadena(lista):

    """Convierte una lista en una cadena"""

    cadena = ""
    for caracter in lista:
        cadena += caracter

    return cadena

def posicion_letra_en_palabra(letra, palabra_adivinar):

    """Devuelve la posición de una letra o
    letras repetidas que ya se encuentran en palabra"""

    lista_posicion = []
    longitud = len(palabra_adivinar)

    for i in  range(longitud):
        if palabra_adivinar[i] == letra:
            lista_posicion.append(i)
    return lista_posicion

def ingresar_letra_en_lista_secreta(letra, lista_secreta, lista_posicion):

    """Ingresa la letra a la lista secreta en la posición correspondiente"""

    for i in lista_posicion:
        lista_secreta[i] = letra
    return lista_secreta

#---------------ENTRADA DE DATOS---------------#

def validar_ingreso(cadena_letras_repetidas):

    fusible = False
    
    while fusible==False:
        
        letra=input("Ingresar una sola letra para jugar: ")
        
        if len(letra) == 1:
            
            if letra.isalpha():
                
                if letra.lower() in cadena_letras_repetidas:
                    
                    print("Letra ya ingresada")
                    
                else:
                    fusible = True
                    
            elif letra == "0":
                fusible = True
                
            else:
                print("Ingresó un caracter que no es un letra")
                
        elif letra == "FIN":
            fusible = True
            
        else:
            print("Ingresó más de un caracter")
            
    return letra

#---------- SALIDA DE DATOS--------------------#

def mostrar_mensaje(mensaje, cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas):

    """Muestra resultados al usuario"""

    print(f"\n{mensaje:<20}{cadena_secreta}\t\tAciertos: {aciertos:1}\t\tDesaciertos: {desaciertos:1} - {cadena_letras_incorrectas}")

def esta_letra_en_palabra(letra, palabra_adivinar):

    """Me devuelve un booleano que dice si la letra pertenece a la palabra """

    return (letra in palabra_adivinar)

# DESDE ACÁ LA PARTE DEL DICCIONARIO


def eliminar_caracteres_especiales(texto, signos):
    
    for signo in signos:
        
        if signo in texto:
            
            texto=texto.replace(signo," ")

    texto_sin_espacio=texto.split()
        
    texto_unido_sin_espacio=" ".join(texto_sin_espacio)
    
    return texto_unido_sin_espacio

def armar_lista_de_palabras(texto):

    """Arma la lista de palabras, sin repetir, todas en minuscula y con un mínimo de 5 caracteres
    Zoilo Pazos"""

    lista_palabras_sin_repetir = []
    lista_palabras = texto.split(" ")
    CINCO=5
    for palabra in lista_palabras:
        if palabra.lower() not in lista_palabras_sin_repetir and palabra != '' and len(palabra) >= CINCO:
            lista_palabras_sin_repetir.append(palabra.lower())
    return lista_palabras_sin_repetir

def armar_diccionario(lista_de_palabras, texto):

    """Arma el diccionario con las palabras en orden alfabetico como claves, y cada una contiene la cantidad de veces que aparece en la cadena original
    Zoilo Pazos"""

    diccionario_palabras = {}
    lista_ordenada = sorted(lista_de_palabras)
    for palabra in lista_ordenada:
        apariciones = texto.count(palabra)
        diccionario_palabras[palabra] = apariciones
    return diccionario_palabras

def elegir_palabra(diccionario, longitud_palabra_elegida_validada):

    """Elige una palabra aleatoria del diccionario para jugar, con la longitud que el jugador quiera, si elige una, sino, la palabra se elige de entre todas
    Zoilo Pazos"""

    palabras_con_longitud_elegida = []
    VACIO=""
    if longitud_palabra_elegida_validada == VACIO:
        for palabra in diccionario:
            palabras_con_longitud_elegida.append(palabra)
    else:
        for palabra in diccionario:
            if len(palabra) == int(longitud_palabra_elegida_validada):
                palabras_con_longitud_elegida.append(palabra)

    return random.choice(palabras_con_longitud_elegida)

def eliminar_tildes(texto):

    """elimina las tildes de la palabra"""

    lista = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ü", "u")]
    PRIMER_POSICION=0
    SEGUNDA_POSICION=1
    for vocales in lista:
        texto = texto.replace(vocales[PRIMER_POSICION], vocales[SEGUNDA_POSICION])
    return texto

def contar_puntajes(aciertos, desaciertos):

    """Cuenta la cantidad de puntos los acirtos valen 10 y los desaciertos valen -5"""
    
    ACIERTO_VALOR=10
    DESACIERTO_VALOR=-5

    return aciertos * ACIERTO_VALOR + desaciertos * (DESACIERTO_VALOR)


def validar_longitud_palabra(longitud_palabra_elegida):

    """valida el ingreso de la longitud de la palabra elegida (número entero mayor a 5 o caracter vacio)"""

    bandera = False
    VACIO=""
    CARACTER_MINIMO=6
    CARACTER_MAXIMO=16 #habría que buscar en el texto el máximo
    
    while not bandera :

        if longitud_palabra_elegida.isnumeric() and int(longitud_palabra_elegida) in range(CARACTER_MINIMO, CARACTER_MAXIMO):
            bandera = True
        elif longitud_palabra_elegida == VACIO:
            bandera = True
        else:
            bandera = False
            mensaje="Ingrese la longitud de palabra (entre 6 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
            longitud_palabra_elegida = input(mensaje)

    return longitud_palabra_elegida

def instrucciones():

    """muestra al usuario las reglas de juego"""

    mensaje1 = "Usted va a jugar al ahorcado"
    mensaje2 = "para interrumpir el juego ingrese un 0 o FIN"
    mensaje3 = "los Aciertos valen 10 puntos y los Desaciertos restan 5 puntos"
    print(f"{mensaje1:*^80}\n{mensaje2:^80}\n{mensaje3:-^80}\n")

def mostrar_mensaje_progreso(es_acierto):
    if es_acierto:
        mensaje="Muy bien!!! → "
    else:
        mensaje="Lo siento!!! → "
        
    return mensaje

def contador_aciertos_desaciertos(es_acierto,lista_aciertos_desaciertos):
    
    """devuelve lista aciertos y desaciertos """
    PRIMER_POSICION=0
    SEGUNDA_POSICION=1
    
    if es_acierto:
                    lista_aciertos_desaciertos[PRIMER_POSICION] += 1
    else:
                    lista_aciertos_desaciertos[SEGUNDA_POSICION] += 1
        
    lista_aciertos_desaciertos = [lista_aciertos_desaciertos[PRIMER_POSICION],lista_aciertos_desaciertos[SEGUNDA_POSICION]]
        
    return lista_aciertos_desaciertos

###################################246#####################################

def ultimo_mensaje(cadena_secreta,palabra_adivinar,aciertos,desaciertos,cadena_letras_incorrectas):
    
    """muestra el ultimo mensaje"""
    
    if cadena_secreta == palabra_adivinar :
            aciertos += 1
            mostrar_mensaje("Ganaste!!! → ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)

    elif desaciertos == 8:
            
            mostrar_mensaje("Perdiste!!! → ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)

#------------------CUERPO--------------------------------#

def main():

    intento = 1
    puntaje_total = 0
    pregunta = "si"

    while pregunta == "si":

        #Diccionario
        
        signos=list(string.punctuation)
        texto = obtener_texto()
        texto = eliminar_caracteres_especiales(texto, signos)
        lista_de_palabras = armar_lista_de_palabras(texto)
        diccionario = armar_diccionario(lista_de_palabras, texto)

        #instrucciones para el usuario
        if intento == 1: instrucciones()

        #Elección de palabra
        mensaje = "Ingrese la longitud de palabra (ente 5 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
        longitud_palabra_elegida = input(mensaje)

        #validación de palabra
        longitud_palabra_elegida = validar_longitud_palabra(longitud_palabra_elegida)
        palabra_adivinar = eliminar_tildes(elegir_palabra(diccionario, longitud_palabra_elegida))

        #Inicialización de variables del juego
        desaciertos = 0
        aciertos = 0
        lista_aciertos_desaciertos = [aciertos,desaciertos]
        cadena_letras_incorrectas = ""
        cadena_letras_repetidas = ""
        palabra_secreta = esconder_palabra(palabra_adivinar)    
        lista_secreta = list(palabra_secreta)         #1°corección
        cadena_secreta = "".join(lista_secreta)       

        #Se le pregunta por 1era vez al usuario que adivine una letra

        mostrar_mensaje("\nPalabra a adivinar(sin tildes): ", palabra_secreta, aciertos, desaciertos, cadena_letras_incorrectas)
        
        print(palabra_adivinar)
        
        """Se evalua que tipo de condición cumple el ingreso de usuario y se repite hasta
        que cumpla algunas de las condiciones de salida"""
       
        letra_verificada="a"

        while letra_verificada not in ("0","FIN"):
    
            letra_verificada = validar_ingreso(cadena_letras_repetidas)   # solo una letra no repetida, 0 o FIN
            
            if letra_verificada not in ("0","FIN"):    
                
                letra_verificada=letra_verificada.lower()
                letra_verificada=eliminar_tildes(letra_verificada) #elimina tildes
                cadena_letras_repetidas += letra_verificada
                es_acierto = letra_verificada in palabra_adivinar
                lista_aciertos_desaciertos = contador_aciertos_desaciertos(es_acierto, lista_aciertos_desaciertos)
                        
                if es_acierto:
                    lista_posicion = posicion_letra_en_palabra(letra_verificada, palabra_adivinar) #lista con las posiciones que esta la letra
                    lista_secreta  = ingresar_letra_en_lista_secreta(letra_verificada, lista_secreta, lista_posicion) #cambia listas de ???? x ?a?a
                                    
                else:
                    cadena_letras_incorrectas += letra_verificada
                        
                cadena_secreta = lista_a_cadena(lista_secreta)
                
                if lista_aciertos_desaciertos[1]<8 and cadena_secreta != palabra_adivinar: 
                    mostrar_mensaje(mostrar_mensaje_progreso(es_acierto), cadena_secreta, lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1], cadena_letras_incorrectas)
                
                if lista_aciertos_desaciertos[1]==8 or cadena_secreta == palabra_adivinar:
                     letra_verificada="0"
                     
        ultimo_mensaje(cadena_secreta,palabra_adivinar,lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1],cadena_letras_incorrectas)
        
        print("\nTu puntaje fue: ",contar_puntajes(lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1]))

        #Se le pregunta al jugador si quiere volver a jugar, si nó devuelve el puntaje total

        puntaje_total = puntaje_total + contar_puntajes(lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1])
        
        pregunta = input("Queres seguir jugando? si/no: ").lower()

        intento += 1

        print("Tu puntaje total fue: ", puntaje_total)

from texto import obtener_texto
import random
import string
main()
            
# ruy         
                
            

            
            
            

            
            
            
            
           
                    
            
            
        








