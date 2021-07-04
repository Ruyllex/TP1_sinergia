dicc_jugadores = crear_diccionario_asignacion_palabras(nombres_ordenados,longitud_palabra_elegida,diccionario)

def turno_de_un_jugador(nombre,cadena_letras_repetidas,dicc_usuario_palabra,lista_aciertos_desaciertos):

    while not es_acierto:
        letra = input("Ingresar letra: ")
        valida = validar_letra(letra)
        repetida = verificar_repetido(letra,cadena_letras_repetidas)
        letra_verificada = devolver_letra_verificada(valida,repetida,cadena_letras_repetidas,letra)
        letra_verificada = letra_verificada.lower()
        cadena_letras_repetidas += letra_verificada 
        es_acierto = letra_verificada in palabra_adivinar
        lista_aciertos_desaciertos = contador_aciertos_desaciertos(es_acierto, lista_aciertos_desaciertos)

        if es_acierto:
            lista_posicion = posicion_letra_en_palabra(letra_verificada, palabra_adivinar) #lista con las posiciones que esta la letra
            lista_secreta  = ingresar_letra_en_lista_secreta(letra_verificada, lista_secreta, lista_posicion) #cambia listas de ???? x ?a?a


        else:
            cadena_letras_incorrectas += letra_verificada

        cadena_secreta = "".join(lista_secreta)
    

