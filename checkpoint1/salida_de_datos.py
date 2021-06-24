#---------- SALIDA DE DATOS--------------------#
import random
from entrada_de_datos import validar_letra,verificar_repetido

def mostrar_mensaje(mensaje, cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas):

    """Muestra resultados. Leonardo Ayuso"""

    print(f"{mensaje:<20}{cadena_secreta}\t\tAciertos: {aciertos:1}\t\tDesaciertos: {desaciertos:1} - {cadena_letras_incorrectas}")



def elegir_palabra(diccionario, longitud_palabra_elegida_validada):

    """Elige una palabra aleatoria del diccionario para jugar, con la longitud que el jugador quiera, si elige una, sino, la palabra se elige de entre todas
    Zoilo Pazos"""

    palabras_con_longitud_elegida = []
    if longitud_palabra_elegida_validada == "": # CORRECCION: Falta una constante
        for palabra in diccionario:
            palabras_con_longitud_elegida.append(palabra)
    else:
        for palabra in diccionario: 
            if len(palabra) == int(longitud_palabra_elegida_validada):
                palabras_con_longitud_elegida.append(palabra)
    return random.choice(palabras_con_longitud_elegida)



def eliminar_tildes(texto):

    """elimina las tildes de la palabra. Zoilo Pazos"""

    lista = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ü", "u")]
    for caracter in lista:
        texto = texto.replace(caracter[0], caracter[1])  # CORRECCION: Usar constantes
    return texto
def contar_puntajes(aciertos, desaciertos):

    """Cuenta la cantidad de puntos los acirtos valen 10 y los desaciertos valen -5. Zoilo Pazos"""

    total_puntaje_de_palabra = aciertos * 10 + desaciertos * (-5) # CORRECCION: Usar constantes
    return total_puntaje_de_palabra # CORRECCION: Se puede retornar directamente "aciertos * 10 + ..."

puntaje_total = 0 # CORRECCION: Esto está mal

def solicitar_longitud_palabra(mensaje):
    
    """solicita la longitud de la palabra. Zoilo Pazos"""

    longitud_palabra_elegida = input(mensaje) #CORRECCION: Función innecesaria, se cambia "input(mensaje)" por "solicitar_longitud_palabra(mensaje)", básicamente se agrega un llamado a una función innecesario
    return longitud_palabra_elegida # CORRECICON: Se puede retornar directamente input(mensaje)


def validar_longitud_palabra(longitud_palabra_elegida):

    """valida el ingreso de la longitud de la palabra elegida (número entero mayor a 5 o caracter vacio). Zoilo Pazos"""

    bandera = False # CORRECICON: Utilizar nombres más descriptivos

    while not bandera :

        if longitud_palabra_elegida.isnumeric() and int(longitud_palabra_elegida) in range(5, 16):#en vez de 5 poner 6 y el 16 es la long max dentro del texto # CORRECCION: Utilizar constantes
            bandera = True
        elif longitud_palabra_elegida == "": # CORRECCION: Utilizar constantes
            bandera = True
        else:
            bandera = False
            mensaje="Ingrese la longitud de palabra (entre 5 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
            longitud_palabra_elegida = solicitar_longitud_palabra(mensaje)

    return longitud_palabra_elegida

def instrucciones():

    """muestra al usuario las reglas de juego. Zoilo Pazos"""

    mensaje1 = "Usted va a jugar al ahorcado"
    mensaje2 = "para interrumpir el juego ingrese un 0 o FIN"
    mensaje3 = "los Aciertos valen 10 puntos y los Desaciertos restan 5 puntos"
    print(f"{mensaje1:*^80}\n{mensaje2:^80}\n{mensaje3:-^80}")

def mostrar_mensaje_progreso(es_acierto):
    
    """Muestra mensaje de acierto o desacierto. Zoilo Pazos"""
    
    if es_acierto:
        mensaje="Muy bien!!! → "
    else:
        mensaje="Lo siento!!! → "
    return mensaje

def contador_aciertos_desaciertos(es_acierto,lista_aciertos_desaciertos):
    
    """devuelve lista aciertos y desaciertos. Zoilo Pazos """

    #CORRECCION: Función ineficiente, una mejor opcion es:

    #if es_acierto:
    #   lista_aciertos_desaciertos[0] += 1
    #else:
    #   lista_aciertos_desaciertos[1] += 1
    
    aciertos = lista_aciertos_desaciertos[0] # CORRECCION: Se puede hacer "aciertos, desaciertos = lista_aciertos_desaciertos"
    desaciertos = lista_aciertos_desaciertos[1]
    

    if es_acierto:
                aciertos += 1
    else:
                desaciertos += 1
    
    lista_aciertos_desaciertos = [aciertos,desaciertos]
    
    return lista_aciertos_desaciertos



def ultimo_mensaje(cadena_secreta,palabra_adivinar,aciertos,desaciertos,cadena_letras_incorrectas): # CORRECCION: El nombre de la función es malo, "ultimo_mensaje()" es vago "mostrar_resultado_partida()" es más decriptivo
    
    """muestra el ultimo mensaje. Agustín Sánchez Vergara y Jorge Sedek """
    
    if cadena_secreta == palabra_adivinar :
            aciertos += 1
            mostrar_mensaje("Ganaste!!! → ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)

    elif desaciertos == 8: # CORRECCION: Falta constante
            
            #cadena_letras_incorrectas += letra
            mostrar_mensaje("Perdiste!!! → ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)


def permitir_letra(letra,cadena_letras_repetidas):
    
    """se asegura que letra no sea ni repetida ni invalida. Agustín Sánchez Vergara y Jorge Sedek"""
    
    while letra not in ("FIN", "0") and ((len(letra) > 1 or not letra.isalpha()) or letra in cadena_letras_repetidas):
        
        if len(letra) > 1 or not letra.isalpha():
            letra = validar_letra(letra)
        
        elif letra in cadena_letras_repetidas:
            letra = verificar_repetido(letra,cadena_letras_repetidas)
            
        
              
    
    
    return letra
        
