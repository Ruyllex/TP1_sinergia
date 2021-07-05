from texto import obtener_texto
from cuerpo_funciones import *
from entrada_de_datos import *
from salida_de_datos import *
from generar_diccionario import *
from configuraciones import constantes
import random
diccionario_con_constantes=constantes()
PUNTOS_ACIERTOS = diccionario_con_constantes['PUNTOS_ACIERTOS']
PUNTOS_DESACIERTOS = -(diccionario_con_constantes['PUNTOS_DESACIERTOS'])



def turno_de_un_jugador(nombre,dicc_repetidas_incorrectas,dicc_palabra_adivinar_e_secreta,dicc_aciertos_desaciertos,dicc_puntaje):
    es_acierto = True
    cadena_secreta = "".join(dicc_palabra_adivinar_e_secreta[nombre][1])
    while es_acierto and not descubrio_palabra(nombre,dicc_palabra_adivinar_e_secreta):
        if dicc_aciertos_desaciertos[nombre][0] == 0 and dicc_aciertos_desaciertos[nombre][1] == 0:
             print(f"{cadena_secreta}\t\tAciertos: {dicc_aciertos_desaciertos[nombre][0]:1}\t\tDesaciertos: {dicc_aciertos_desaciertos[nombre][1]:1} - {dicc_repetidas_incorrectas[nombre][1]}")
        letra = input(f"{nombre} → Ingresar letra: ")
        valida = validar_letra(letra)
        repetida = verificar_repetido(letra,dicc_repetidas_incorrectas[nombre][0])
        letra_verificada = devolver_letra_verificada(nombre, valida,repetida,dicc_repetidas_incorrectas[nombre][0],letra)
        letra_verificada = letra_verificada.lower()
        if letra_verificada == "fin":
            es_acierto=False
        dicc_repetidas_incorrectas[nombre][0] += letra_verificada
        
        es_acierto = letra_verificada in dicc_palabra_adivinar_e_secreta[nombre][0] 
        
        dicc_aciertos_desaciertos[nombre] = contador_aciertos_desaciertos(es_acierto, dicc_aciertos_desaciertos[nombre])

        if es_acierto:
            lista_posicion = posicion_letra_en_palabra(letra_verificada, dicc_palabra_adivinar_e_secreta[nombre][0]) #lista con las posiciones que esta la letra
            dicc_palabra_adivinar_e_secreta[nombre][1]  = ingresar_letra_en_lista_secreta(letra_verificada, dicc_palabra_adivinar_e_secreta[nombre][1], lista_posicion) #cambia listas de ???? x ?a?a


        else:
            dicc_repetidas_incorrectas[nombre][1] += letra_verificada

        cadena_secreta = "".join(dicc_palabra_adivinar_e_secreta[nombre][1])
        mostrar_mensaje(mostrar_mensaje_progreso(es_acierto), cadena_secreta, dicc_aciertos_desaciertos[nombre][0], dicc_aciertos_desaciertos[nombre][1], dicc_repetidas_incorrectas[nombre][1])
    puntaje_jugador = puntaje(dicc_aciertos_desaciertos[nombre][0],dicc_aciertos_desaciertos[nombre][1],PUNTOS_ACIERTOS,PUNTOS_DESACIERTOS)
    dicc_puntaje[nombre][0] += puntaje_jugador
    return 
# Informacion que deberia guardar: nombre, dicc_letras_repetidas_incorrecctas, dicc_usuario_palabra, dicc_aciertos_desaciertos , puntaje
