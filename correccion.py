#--------GRUPO: SINERGIA------------------#

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
#---------IMPORTES--------------------------#
from texto import obtener_texto
import random
import cuerpo_funciones

#---------------ENTRADA DE DATOS---------------#

def validar_letra(letra):
    
    """Solicita el ingreso hasta que sea una sola letra. Leonardo Ayuso"""

    # CORRECCIÓN: Mala modularización, ya tienen una función que pide el ingreso. Lo que debería hacer esta función es indicar si la letra es válida o no, y eso lo debe agarrar la función externa y decidir que hacer
    
    while (len(letra) != 1 or not letra.isalpha()) and (letra not in ("FIN","0")) :
        print("Ingreso inválido: ingresar solo UNA letra")
        letra = input("Ingresar letra: ")

    return letra

def verificar_repetido(letra,cadena_letras_repetidas):
    
    """Solicita el ingreso hasta que la letra no este repetida. Leonardo Ayuso"""

    #CORRECCION: Misma corrección que la función anterior
    
    while letra in cadena_letras_repetidas:
        print("Letra ya ingresada")
        letra = input("Ingresar letra: ")
        
    return letra


#---------- SALIDA DE DATOS--------------------#

def mostrar_mensaje(mensaje, cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas):

    """Muestra resultados. Leonardo Ayuso"""

    print(f"{mensaje:<20}{cadena_secreta}\t\tAciertos: {aciertos:1}\t\tDesaciertos: {desaciertos:1} - {cadena_letras_incorrectas}")

def esta_letra_en_palabra(letra, palabra_adivinar):

    """Me devuelve un booleano que dice si la letra pertenece a la palabra. Leonardo Ayuso """

    # CORRECCION: Función innecesaria

    return (letra in palabra_adivinar)

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
    return texto.lower() #esto deberia ser una linea del main() porque la funcion esta haciendo 2 cosas # CORRECCION: ver la correccion del fondo del archivo

def armar_lista_de_palabras(texto):

    """Arma la lista de palabras, sin repetir, todas en minuscula y de minimo 5 caracteres
    Ruy Mori"""

    lista_palabras_sin_repetir = []
    lista_palabras = texto.split(" ")
    for palabra in lista_palabras:
        if palabra.lower() not in lista_palabras_sin_repetir and palabra != '' and len(palabra) >= 5: # CORRECCION: Faltan constantes
            lista_palabras_sin_repetir.append(palabra.lower())
    return lista_palabras_sin_repetir

def armar_diccionario(lista_de_palabras, texto):

    """Arma el diccionario con las palabras en orden alfabetico como claves, y cada una contiene la cantidad de veces que aparece en la cadena original
    Ruy Mori"""

    diccionario_palabras = {}
    lista_ordenada = sorted(lista_de_palabras)
    for palabra in lista_ordenada:
        apariciones = apariciones_palabra_en_texto(palabra, texto)
        diccionario_palabras[palabra] = apariciones
    return diccionario_palabras

def apariciones_palabra_en_texto(palabra, texto):

    """Cuenta las apariciones de cada palabra en el texto, y devuelve el resultado a la funcion armar_diccionario
    Ruy Mori"""

    # CORRECCION: La función es innecesaria. Tampoco es óptima porque se podría devolver directamente "texto.count(palabra)"

    apariciones = texto.count(palabra)
    return apariciones

def elegir_palabra(diccionario, longitud_palabra_elegida_validada):

    """Elige una palabra aleatoria del diccionario para jugar, con la longitud que el jugador quiera, si elige una, sino, la palabra se elige de entre todas
    Zoilo Pazos"""

    palabras_con_longitud_elegida = []
    if longitud_palabra_elegida_validada == "": # CORRECCION: Falta una constante
        for i in diccionario: # CORRECCION: Usar mejores nombres para las variables "palabra" era mejor
            palabras_con_longitud_elegida.append(i)
        palabra = random.choice(palabras_con_longitud_elegida)
    else:
        for i in diccionario: # CORRECCION: Usar mejores nombres para las variables "palabra" era mejor
            if len(i) == int(longitud_palabra_elegida_validada):
                palabras_con_longitud_elegida.append(i)
        palabra = random.choice(palabras_con_longitud_elegida)

    # CORRECCION: En ambos casosos del if se hace al final "palabra = random.choice(...)", entonces esto se debe sacar afuera del if.
    # Hasta se puede retornar esto ("return random.choice(...)")

    return palabra

def eliminar_tildes(texto):

    """elimina las tildes de la palabra. Zoilo Pazos"""

    lista = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ü", "u")]
    for i in lista: # CORRECCION: Usar mejores nombres
        texto = texto.replace(i[0], i[1])  # CORRECCION: Usar constantes
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
    
    while (len(letra) > 1 or not letra.isalpha()) or (letra in cadena_letras_repetidas):
        
        if len(letra) > 1 or not letra.isalpha():
            letra = validar_letra(letra)
        
        elif letra in cadena_letras_repetidas:
            letra = verificar_repetido(letra,cadena_letras_repetidas)
            
        
              
    
    
    return letra
        

def main():

    #CORRECCION: El main puede modularizarse más
    #CORRECCION: Regla de Oro: si un código necesita comentarios para que se entendible, algo estamos haciendo mal

    intento = 1
    puntaje_total = 0
    pregunta = "si" # CORRECCION: Esto no es una pregunta, es una respuesta. Mal nombre de variable

    while pregunta == "si":

        # CORRECCION: Cada vez que se va a jugar una nueva partida, vuelven a procesar todo el texto, MAL

        #Diccionario
        texto = obtener_texto()
        caracteres_especiales = identificar_caracter_especial(texto)
        texto = eliminar_caracteres_especiales(texto, caracteres_especiales)
        lista_de_palabras = armar_lista_de_palabras(texto)
        diccionario = armar_diccionario(lista_de_palabras, texto)

        #instrucciones para el usuario
        if intento == 1: instrucciones()

        #Elección de palabra
        mensaje = "Ingrese la longitud de palabra (ente 5 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
        longitud_palabra_elegida = solicitar_longitud_palabra(mensaje)

        #validación de palabra
        longitud_palabra_elegida = validar_longitud_palabra(longitud_palabra_elegida)
        palabra_adivinar = eliminar_tildes(elegir_palabra(diccionario, longitud_palabra_elegida))

        

        #Inicialización de variables
        desaciertos = 0
        aciertos = 0
        lista_aciertos_desaciertos = [aciertos,desaciertos]
        cadena_letras_incorrectas = ""
        cadena_letras_repetidas = ""
        palabra_secreta = esconder_palabra(palabra_adivinar) 
        
        lista_secreta = list(palabra_secreta)  
        cadena_secreta = list(lista_secreta) 

        #Se le pregunta por 1era vez al usuario que adivine una letra

        mostrar_mensaje("Palabra a adivinar(sin tildes): ", palabra_secreta, aciertos, desaciertos, cadena_letras_incorrectas)



        """Se evalua que tipo de condición cumple el ingreso de usuario y se repite hasta 
        que cumpla algunas de las condiciones de salida"""
        letra = input("Ingresar letra: ")
        letra_validada = validar_letra(letra)
        letra_verificada = verificar_repetido(letra_validada,cadena_letras_repetidas)
            
        while letra_verificada not in ("0","FIN") and lista_aciertos_desaciertos[1] < 8 and cadena_secreta != palabra_adivinar:
            
            letra_verificada = letra_verificada.lower()
            cadena_letras_repetidas += letra_verificada 
            es_acierto = esta_letra_en_palabra(letra_verificada, palabra_adivinar)
            
            lista_aciertos_desaciertos = contador_aciertos_desaciertos(es_acierto, lista_aciertos_desaciertos)
            
            if es_acierto:
                lista_posicion = posicion_letra_en_palabra(letra_verificada, palabra_adivinar) #lista con las posiciones que esta la letra
                lista_secreta  = ingresar_letra_en_lista_secreta(letra_verificada, lista_secreta, lista_posicion) #cambia listas de ???? x ?a?a
                
            
            else:
                cadena_letras_incorrectas += letra_verificada
                
            cadena_secreta = lista_a_cadena(lista_secreta)
            if lista_aciertos_desaciertos[1] < 8 and cadena_secreta != palabra_adivinar: # CORRECCION: Usar constantes
                mostrar_mensaje(mostrar_mensaje_progreso(es_acierto), cadena_secreta, lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1], cadena_letras_incorrectas) # CORRECCION: Usar constantes
                letra = input("Ingresar letra: ")
                letra_validada = validar_letra(letra)
                letra_verificada = permitir_letra(letra_validada,cadena_letras_repetidas)
            
                
            
                
            
            
        ultimo_mensaje(cadena_secreta,palabra_adivinar,lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1],cadena_letras_incorrectas)
        print("\nTu puntaje fue: ",contar_puntajes(lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1]))

        #Se le pregunta al jugador si quiere volver a jugar, si nó devuelve el puntaje total
        #puntaje_inicial=0

        puntaje_total = puntaje_total + contar_puntajes(lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1])
        pregunta = input("Queres seguir jugando? si/no: ").lower() #CORRECCION: No hay validaciones

        intento += 1

        print("Tu puntaje total fue: ", puntaje_total)


main()

# CORRECCION: Dividir el programa en mas archivos, puede dividirse por funcionalidad.
# CORRECCION: MUY IMPORTANTE! Se estan tomando muy en serio lo de que cada función haga una única cosa, se lo estan tomando muy literal. Tienen que hacerte esta pregunta "Que hace esta función?".
# Si la respuesta es de la forma: "la función hace esto Y esto" entonces hay algo mal (por ejemplo: la función pide ingreso al usuario Y valida ese ingreso) (otro ejemplo en base a lo que pusieron
# en la linea 169: la función devuelve un texto en minúscula sin caracteres especiales  <-- está bien)
         
            
            
                
            

            
            
            

            
            
            
            
           
                    
            
            
        








