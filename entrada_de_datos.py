#---------------ENTRADA DE DATOS---------------#

def validar_letra(letra):
    
    """Devuelve un booleano que dice si la letra es valida o no. Leonardo Ayuso"""

    # CORRECCIÓN: Mala modularización, ya tienen una función que pide el ingreso. Lo que debería hacer esta función es indicar si la letra es válida o no, y eso lo debe agarrar la función externa y decidir que hacer
    if (len(letra) != 1 or not letra.isalpha()) and (letra not in ("FIN","0")) :
        valida = False
    else:
        valida = True

    return valida

def verificar_repetido(letra,cadena_letras_repetidas):
    
    """Devuelve un booleano que dice si la letra esta repetida o no. Leonardo Ayuso"""

    #CORRECCION: Misma corrección que la función anterior
    
    if letra in cadena_letras_repetidas:
        repetida = True
    else:
        repetida = False
        
    return repetida

def devolver_letra_verificada(valida,repetida,cadena_letras_repetidas,letra):
    
    """Pide al usuario reingresar la letra hasta que sea valida y no este repetida. Jorge Sedek"""
    
    while not valida or repetida :
        if not valida:
            print("Ingreso inválido: ingresar solo UNA letra")
            letra = input("Ingresar letra: ")
        elif repetida:
            print("Letra ya ingresada")
            letra = input("Ingresar letra: ")
        repetida = verificar_repetido(letra,cadena_letras_repetidas)
        valida = validar_letra(letra)

    return letra

