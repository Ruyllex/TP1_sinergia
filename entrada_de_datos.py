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
