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
from configuraciones import check, constantes
from texto import obtener_texto
from cuerpo_funciones import *
from entrada_de_datos import *
from salida_de_datos import *

from generar_dict_2 import *
from etapa_7 import *
import random

def main():

    #CORRECCION: El main puede modularizarse más
    dicc_constantes=constantes() #esta en configuraciones
    configuraciones=check(dicc_constantes)
    print(configuraciones)
    intento = 1
    puntaje_total = 0
    respuesta = "si" 
    MAX_DESACIERTOS = 2

    #Diccionario
    diccionario=generar_diccionario()
    generar_palaras_csv(diccionario)
    
    while respuesta == "si":

        #instrucciones para el usuario
        if intento == 1: instrucciones()

#         #Elección de palabra
#         mensaje = "Ingrese la longitud de palabra (ente 5 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
#         longitud_palabra_elegida = input(mensaje)
# 
#         #validación de palabra
#         longitud_palabra_elegida = validar_longitud_palabra(longitud_palabra_elegida)
#         palabra_adivinar = eliminar_tildes(elegir_palabra(diccionario, longitud_palabra_elegida))
# 
#         #Inicialización de variables
#         desaciertos = 0
#         aciertos = 0
#         lista_aciertos_desaciertos = [aciertos,desaciertos]
#         cadena_letras_incorrectas = ""
#         cadena_letras_repetidas = ""
#         cadena_secreta = esconder_palabra(palabra_adivinar)
# 
#         lista_secreta = list(cadena_secreta)
#         cadena_secreta = "".join(lista_secreta)
# 
#         #Se le pregunta por 1era vez al usuario que adivine una letra
# 
#         mostrar_mensaje("Palabra a adivinar(sin tildes): ", cadena_secreta, aciertos, desaciertos, cadena_letras_incorrectas)
# 
# 
# 
#         """Se evalua que tipo de condición cumple el ingreso de usuario y se repite hasta 
#         que cumpla algunas de las condiciones de salida"""
#         letra = input("Ingresar letra: ")
#         valida = validar_letra(letra)
#         repetida = verificar_repetido(letra,cadena_letras_repetidas)
#         letra_verificada = devolver_letra_verificada(valida,repetida,cadena_letras_repetidas,letra)

        
       # nombres = validar_nombres()
       # nombres_ordenados = ordenar_nombres_aleatoriamente(nombres)
        nombres_ordenados = ["pepe","pipin","papu"]
        mensaje = "Ingrese la longitud de palabra (ente 5 y 16) con la que desea jugar, o presione enter para que sea aleatoria: "
        longitud_palabra_elegida = input(mensaje)
        cadena_secreta = ""
        #inicializar diccionarios
        dicc_palabra_adivinar_e_secreta = crear_diccionario_palabras(nombres_ordenados,longitud_palabra_elegida,diccionario)
        dicc_aciertos_desaciertos = crear_diccionario_aciertos_desaciertos(nombres_ordenados)
        dicc_repetidas_incorrectas = crear_diccionario_letras_repetidas_e_incorrectas(nombres_ordenados)
        dicc_puntaje = crear_diccionario_puntaje(nombres_ordenados)
        
        palabra_adivinada = False
        i = 0
        while not palabra_adivinada and len(nombres_ordenados) != 0:
                if i >= len(nombres_ordenados) :
                    i = 0
                nombre = nombres_ordenados[i]
                turno_de_un_jugador(nombre,dicc_repetidas_incorrectas,dicc_palabra_adivinar_e_secreta,dicc_aciertos_desaciertos,dicc_puntaje)
                if dicc_aciertos_desaciertos[nombre][1] >= MAX_DESACIERTOS:
                    nombres_ordenados.remove(nombre)
                    i = i - 1
                
                palabra_adivinada = descubrio_palabra(nombre,dicc_palabra_adivinar_e_secreta)
                if palabra_adivinada:
                    ganador = nombre
                    
                
                i += 1
                    
                
                    
                
                
                
            
# sale cuando :
                    #alguien adivino la palabra
                    #todos cometen el  max de desaciertos



#         while letra_verificada not in ("FIN", "0") and lista_aciertos_desaciertos[1] < MAX_DESACIERTOS and cadena_secreta != palabra_adivinar:
# 
#             letra_verificada = letra_verificada.lower()
#             cadena_letras_repetidas += letra_verificada 
#             es_acierto = letra_verificada in palabra_adivinar
# 
#             lista_aciertos_desaciertos = contador_aciertos_desaciertos(es_acierto, lista_aciertos_desaciertos)
# 
#             if es_acierto:
#                 lista_posicion = posicion_letra_en_palabra(letra_verificada, palabra_adivinar) #lista con las posiciones que esta la letra
#                 lista_secreta  = ingresar_letra_en_lista_secreta(letra_verificada, lista_secreta, lista_posicion) #cambia listas de ???? x ?a?a
# 
# 
#             else:
#                 cadena_letras_incorrectas += letra_verificada
# 
#             cadena_secreta = "".join(lista_secreta)
#             if lista_aciertos_desaciertos[1] < MAX_DESACIERTOS and cadena_secreta != palabra_adivinar: # CORRECCION: Usar constantes
#                 mostrar_mensaje(mostrar_mensaje_progreso(es_acierto), cadena_secreta, lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1], cadena_letras_incorrectas) # CORRECCION: Usar constantes
#                 letra = input("Ingresar letra: ")
#                 valida = validar_letra(letra)
#                 repetida = verificar_repetido(letra,cadena_letras_repetidas)
#                 letra_verificada = devolver_letra_verificada(valida,repetida,cadena_letras_repetidas,letra)
# 
# 
#         ultimo_mensaje(cadena_secreta,palabra_adivinar,lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1],cadena_letras_incorrectas)
#         print("\nTu puntaje fue: ",contar_puntajes(lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1]))
# 
#         #Se le pregunta al jugador si quiere volver a jugar, si nó devuelve el puntaje total
#         #puntaje_inicial=0
# 
#         puntaje_total = puntaje_total + contar_puntajes(lista_aciertos_desaciertos[0], lista_aciertos_desaciertos[1])
#         respuesta = input("Queres seguir jugando? si/no: ").lower() #CORRECCION: No hay validaciones
# 
#         intento += 1
# 
#         print("Tu puntaje total fue: ", puntaje_total)


main()

# CORRECCION: MUY IMPORTANTE! Se estan tomando muy en serio lo de que cada función haga una única cosa, se lo estan tomando muy literal. Tienen que hacerte esta pregunta "Que hace esta función?".
# Si la respuesta es de la forma: "la función hace esto Y esto" entonces hay algo mal (por ejemplo: la función pide ingreso al usuario Y valida ese ingreso) (otro ejemplo en base a lo que pusieron
