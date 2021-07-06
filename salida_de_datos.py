#---------- SALIDA DE DATOS--------------------#
import random
from cuerpo_funciones import esconder_palabra
#from entrada_de_datos import validar_letra,verificar_repetido

def mostrar_mensaje(mensaje, cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas):

    """Muestra resultados. Leonardo Ayuso"""
    if aciertos == 0 and desaciertos == 0:
        print(f"{cadena_secreta}\t\tAciertos: {aciertos:1}\t\tDesaciertos: {desaciertos:1} - {cadena_letras_incorrectas}\n")
    else:
        print(f"{mensaje:<20}{cadena_secreta}\t\tAciertos: {aciertos:1}\t\tDesaciertos: {desaciertos:1} - {cadena_letras_incorrectas}\n")



def elegir_palabra(diccionario, longitud_palabra_elegida_validada):

    """Elige una palabra aleatoria del diccionario para jugar, con la longitud que el jugador quiera, si elige una, sino, la palabra se elige de entre todas
    Zoilo Pazos"""
    vacio=""
    palabras_con_longitud_elegida = []
    if longitud_palabra_elegida_validada == vacio:
        for palabra in diccionario:
            palabras_con_longitud_elegida.append(palabra)
    else:
        for palabra in diccionario: 
            if len(palabra) == int(longitud_palabra_elegida_validada):
                palabras_con_longitud_elegida.append(palabra)
    return random.choice(palabras_con_longitud_elegida)



def eliminar_tildes(texto):

    """elimina las tildes de la palabra. Zoilo Pazos"""
    letra_con_tilde=0
    letra_sin_tilde=1
    lista = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ü", "u")]
    for caracter in lista:
        texto = texto.lower().replace(caracter[letra_con_tilde], caracter[letra_sin_tilde])
    return texto
def contar_puntajes(aciertos, desaciertos):

    """Cuenta la cantidad de puntos los aciertos valen 10 y los desaciertos valen -5. Zoilo Pazos"""

    valor_aciertos=10
    valor_desaciertos=-5
    return aciertos * valor_aciertos + desaciertos * (valor_desaciertos) 

puntaje_total = 0 # CORRECCION: Esto está mal



def validar_longitud_palabra(longitud_palabra_elegida):

    """valida el ingreso de la longitud de la palabra elegida (número entero mayor a 5 o caracter vacio). Zoilo Pazos"""

    bandera = False # CORRECICON: Utilizar nombres más descriptivos
    vacio=""

    while not bandera :

        if longitud_palabra_elegida.isnumeric() and int(longitud_palabra_elegida) in range(5, 16):#en vez de 5 poner 6 y el 16 es la long max dentro del texto # CORRECCION: Utilizar constantes
            bandera = True
        elif longitud_palabra_elegida == vacio:
            bandera = True
        else:
            bandera = False
            mensaje="Ingrese la longitud de palabra (entre 5 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
            longitud_palabra_elegida = input(mensaje)

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
        mensaje=" \033[32m" + "Muy bien!!!" + "\033[0m" + "      "
    else:
        mensaje=" \033[31m" + "Lo siento!!!" + "\033[0m" + "     "
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
    cant_MAX_desaciertos=8
    
    if cadena_secreta == palabra_adivinar :
        aciertos += 1
        mostrar_mensaje("Ganaste!!! → ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)

    elif desaciertos == cant_MAX_desaciertos:
            
        #cadena_letras_incorrectas += letra
        mostrar_mensaje("Perdiste!!! → ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)


"""" se cambio esta funcion por devolver_letra_verificada(valida,repetida) , verificar_repetido(letra,cadena_letras_repetidas) y validar_letra(letra)"""
# def permitir_letra(letra,cadena_letras_repetidas):
#     
#     """se asegura que letra no sea ni repetida ni invalida. Agustín Sánchez Vergara y Jorge Sedek"""
#     
#     while letra not in ("FIN", "0") and ((len(letra) > 1 or not letra.isalpha()) or letra in cadena_letras_repetidas):
#         
#         if len(letra) > 1 or not letra.isalpha():
#             letra = validar_letra(letra)
#         
#         elif letra in cadena_letras_repetidas:
#             letra = verificar_repetido(letra,cadena_letras_repetidas

def validar_nombres(MAX_USUARIOS):
    
    """Crea una lista con los nombres validos ingresados por los usuarios. Jorge Sedek"""
    
    nombres = []
    print(f"Pueden jugar hasta {MAX_USUARIOS} jugadores. Cuando haya ingresado todos los nombres ingrese ENTER")
    cantidad = 1
    nombre = 1
    while nombre !="" and cantidad <= MAX_USUARIOS:
        
        nombre = input("Ingrese el nombre del jugador {} : ".format(cantidad))
        if nombre != "":
            if nombre not in nombres:
                nombres.append(nombre)
                cantidad += 1
            else:
                print("Nombre ya ingresado")
        
        
    return nombres


def ordenar_nombres_aleatoriamente(nombres,ganador):
    
    """Ordena una lista de nombres de manera aleatoria. Jorge Sedek"""

    nombres_ordenados = []
    if ganador:
        nombres.remove(ganador)
        nombres_ordenados.append(ganador)
        for nombre in range(1,len(nombres[:])):
            nombre = random.choice(nombres)
            nombres_ordenados.append(nombre)
            nombres.remove(nombre)
    for nombre in range(len(nombres[:])):
        nombre = random.choice(nombres)
        nombres_ordenados.append(nombre)
        nombres.remove(nombre)

    return nombres_ordenados

def crear_diccionario_palabras(nombres_ordenados,longitud_palabra_elegida,diccionario):
    
    """Crea un diccionario que asigna las palabras a adivinar a los usuarios"""
    
    dicc_palabra_adivinar_e_secreta = {}
    if longitud_palabra_elegida=='':
        longitud_palabra_elegida=random.randint(5,16)

    for nombre in nombres_ordenados:
        palabra_adivinar = eliminar_tildes(elegir_palabra(diccionario, longitud_palabra_elegida))
        cadena_secreta = esconder_palabra(palabra_adivinar)
        lista_secreta = list(cadena_secreta)
        dicc_palabra_adivinar_e_secreta[nombre] = [ palabra_adivinar, lista_secreta]
    
    return dicc_palabra_adivinar_e_secreta

def crear_diccionario_aciertos_desaciertos(nombres_ordenados):
    
    """Crea un diccionario con los aciertos y desaciertos"""
    
    desaciertos = 0
    aciertos = 0
    
    dicc_aciertos_desaciertos = {}
        
    for nombre in nombres_ordenados:
        dicc_aciertos_desaciertos[nombre] = [ aciertos, desaciertos]
    
    return dicc_aciertos_desaciertos

def descubrio_palabra(nombre,dicc_palabra_adivinar_e_secreta):
    
    """booleano que muestra si se descubrio la palabra secreta"""
    
    palabra_secreta = "".join(dicc_palabra_adivinar_e_secreta[nombre][1])
    palabra_adivinar = dicc_palabra_adivinar_e_secreta[nombre][0]
    
    return palabra_secreta == palabra_adivinar


    
def crear_diccionario_letras_repetidas_e_incorrectas(nombres_ordenados):
    
    """ Crea un diccionario con las letras repetidas y incorrectas"""
    
    cadena_letras_repetidas = ""
    cadena_letras_incorrectas = ""
    dicc_repetidas_incorrectas = {}
    
    for nombre in nombres_ordenados:
        dicc_repetidas_incorrectas[nombre] = [cadena_letras_repetidas,cadena_letras_incorrectas] 
    
    return dicc_repetidas_incorrectas
    
puntaje = lambda x,y,a,b: a*x - b*y

def crear_diccionario_puntaje(nombres_ordenados):
    
    puntaje_jugador = 0
    
    dicc_puntaje = {}
    for nombre in nombres_ordenados:
        dicc_puntaje[nombre] = [puntaje_jugador] 
    
    return dicc_puntaje
    

def mostrar_diccionarios(nombres,dicc1,dicc2,dicc3,ganador):
    for nombre in nombres:
        print("Los resultados de {}: \n".format(nombre))
        print("La palabra a adivinar era : {}".format(dicc1[nombre][0]))
        print("Tubo {} aciertos y {} desaciertos".format(dicc2[nombre][0],dicc2[nombre][1]))
        print("Su puntaje fue {}".format(dicc3[nombre][0]))
        if ganador:
            print("El ganador fue {}".format(ganador))
    
#def diccionario_total(nombres,intentos,dicc_Puntaje,dicc_aciertos_desaciertos,ganadores):
    