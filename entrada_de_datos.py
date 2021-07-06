#---------------ENTRADA DE DATOS---------------#

def validar_letra(letra):
    
    """Devuelve un booleano que dice si la letra es valida o no. Leonardo Ayuso"""

    if (len(letra) != 1 or not letra.isalpha()) or (letra in ("FIN","0")) :
        valida = False
    else:
        valida = True

    return valida

def verificar_repetido(letra,cadena_letras_repetidas):
    
    """Devuelve un booleano que dice si la letra esta repetida o no. Leonardo Ayuso"""

    
    if letra in cadena_letras_repetidas:
        repetida = True
    else:
        repetida = False
        
    return repetida

def devolver_letra_verificada(nombre, valida, repetida, cadena_letras_repetidas, letra):
    
    """Pide al usuario reingresar la letra hasta que sea valida y no este repetida. Jorge Sedek"""
    
    while not valida or repetida :
        if not valida:
            if letra in ("FIN","0"):
                letra="FIN"
            else:
                print("Ingreso inválido: ingresar solo UNA letra")
                letra = input(f"{nombre} → Ingresar letra: ")
        elif repetida:
            print("Letra ya ingresada")
            letra = input(f"{nombre} → Ingresar letra: ")
        repetida = verificar_repetido(letra,cadena_letras_repetidas)
        if letra == "FIN":
            valida = True
        else: valida = validar_letra(letra)

    return letra


def sumar_partidas(diccionario_puntaje, diccionario_aciertos_desaciertos,diccionario_total, nombres, intento,ganador):
    for nombre in nombres:
        if intento == 1:
            diccionario_total[nombre]=[]
            diccionario_total[nombre].append(diccionario_puntaje[nombre][0])
        else:
            diccionario_total[nombre][0]+=(diccionario_puntaje[nombre][0])
    for nombre in nombres:
        if intento == 1:
            diccionario_total[nombre].append(diccionario_aciertos_desaciertos[nombre][0])
            diccionario_total[nombre].append(diccionario_aciertos_desaciertos[nombre][1])
            diccionario_total[nombre].append(0)
            if nombre==ganador:
                diccionario_total[nombre][3]+=1

        else:
            diccionario_total[nombre][1]+=(diccionario_aciertos_desaciertos[nombre][0])
            diccionario_total[nombre][2]+=(diccionario_aciertos_desaciertos[nombre][1])
            if nombre==ganador:
                diccionario_total[nombre][3]+=1
    return diccionario_total