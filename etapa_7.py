from texto import obtener_texto
from cuerpo_funciones import *
from entrada_de_datos import *
from salida_de_datos import *
from generar_diccionario import *
import random

PTOS_ACIERTOS = 2
PTOS_DESACIERTOS = -1



def turno_de_un_jugador(nombre,dicc_repetidas_incorrectas,dicc_palabra_adivinar_e_secreta,dicc_aciertos_desaciertos):
    es_acierto = True
    while es_acierto:
        letra = input("Ingresar letra: ")
        valida = validar_letra(letra)
        repetida = verificar_repetido(letra,dicc_repetidas_incorrectas[nombre][0])
        letra_verificada = devolver_letra_verificada(valida,repetida,dicc_repetidas_incorrectas[nombre][0],letra)
        letra_verificada = letra_verificada.lower()
        dicc_repetidas_incorrectas[nombre][0] += letra_verificada
        
        es_acierto = letra_verificada in dicc_palabra_adivinar_e_secreta[nombre][0] 
        dicc_aciertos_desaciertos[nombre] = contador_aciertos_desaciertos(es_acierto, dicc_aciertos_desaciertos[nombre])

        if es_acierto:
            lista_posicion = posicion_letra_en_palabra(letra_verificada, dicc_palabra_adivinar_e_secreta[nombre][0]) #lista con las posiciones que esta la letra
            dicc_palabra_adivinar_e_secreta[nombre][1]  = ingresar_letra_en_lista_secreta(letra_verificada, dicc_palabra_adivinar_e_secreta[nombre][1], lista_posicion) #cambia listas de ???? x ?a?a


        else:
            dicc_repetidas_incorrectas[nombre][1] += letra_verificada

        cadena_secreta = "".join(dicc_palabra_adivinar_e_secreta[nombre][1])
    puntaje_jugador = puntaje(dicc_aciertos_desaciertos[nombre][0],dicc_aciertos_desaciertos[nombre][1],PTOS_ACIERTOS,PTOS_DESACIERTOS)
    dicc_aciertos_desaciertos[nombre][2] += puntaje_jugador
# Informacion que deberia guardar: nombre, dicc_letras_repetidas_incorrecctas, dicc_usuario_palabra, dicc_aciertos_desaciertos , puntaje

