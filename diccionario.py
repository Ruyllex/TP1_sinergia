from salida_de_datos import eliminar_tildes
from os import close
import string

def eliminar_caracteres_especiales(texto):

    """Elimina los caracteres no alfabeticos de la cadena
    Ruy Mori"""
    caracteres_especiales=list(string.punctuation + "¡¿«»0123456789")
    LONGITUD1 = len(caracteres_especiales)
    for i in range(LONGITUD1):
            texto = texto.replace(caracteres_especiales[i], " ")
    return texto

def leer_lineas(archivo, contador):
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        devolucion = linea
    elif not linea and contador < 6:
        devolucion = leer_lineas(archivo, contador + 1)
    else: devolucion = ''
    return devolucion

def generar_diccionario():
    #genera el diccionario
    cuentos = open("archivos_txt/Cuentos.txt", "r", encoding='utf-8-sig')
    araña_negra = open("archivos_txt/La araña negra - tomo 1.txt", "r", encoding='utf-8-sig')
    mil_noches = open("archivos_txt/Las 1000 Noches y 1 Noche.txt", "r", encoding='utf-8-sig')
    contador = 0
    diccionario = {}

    def armar_diccionario(texto, contador, diccionario):
        if texto == cuentos: indice_diccionario = 0
        elif texto == araña_negra: indice_diccionario = 1
        elif texto == mil_noches: indice_diccionario = 2

        linea = leer_lineas(texto, contador)

        while linea:
            linea_limpia = eliminar_caracteres_especiales(eliminar_tildes(linea))
            linea_listada = linea_limpia.split(" ")
            for palabra in linea_listada:
                if len(palabra) >= 5:
                    if palabra not in diccionario:
                        diccionario[palabra] = [0, 0, 0]
                        diccionario[palabra][indice_diccionario] += 1
                    else: diccionario[palabra][indice_diccionario] += 1
            linea = leer_lineas(texto, contador)
        return diccionario


    diccionario = armar_diccionario(cuentos, contador, diccionario)
    cuentos.close()

    
    diccionario = armar_diccionario(araña_negra, contador, diccionario)
    araña_negra.close()

    
    diccionario = armar_diccionario(mil_noches, contador, diccionario)
    mil_noches.close()
    return diccionario

def generar_palaras_csv(diccionario):
    #almacena las palabras en palabras.csv
    lista_palabras_sin_repetir = list(diccionario.keys())
    lista_palabras_sin_repetir.sort()
    palabras = open("palabras.csv", "w", encoding="utf-8-sig")
    for palabra in lista_palabras_sin_repetir:
        palabras.write(palabra + "," + str(diccionario[palabra][0]) + "," + str(diccionario[palabra][1]) + "," + str(diccionario[palabra][2]) + "\n")
    palabras.close()