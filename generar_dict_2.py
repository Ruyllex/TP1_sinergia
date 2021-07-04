from generar_diccionario_copia import eliminar_caracteres_especiales, armar_lista_de_palabras
from salida_de_datos import eliminar_tildes
from os import close

def leer_lineas(archivo, contador):
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        devolucion = linea
    elif not linea and contador < 6:
        devolucion = leer_lineas(archivo, contador + 1)
    else: devolucion = ''
    return devolucion

def my_function(texto, contador, diccionario, lista_palabras):
    if texto == cuentos: indice_diccionario = 0
    elif texto == araña_negra: indice_diccionario = 1
    else: indice_diccionario = 2

    linea = leer_lineas(texto, contador)

    while linea:
        linea_limpia = eliminar_tildes(eliminar_caracteres_especiales(linea))
        linea_listada = linea_limpia.split(" ")
        for palabra in linea_listada:
            if len(palabra) >= 5:
                if palabra not in diccionario:
                    diccionario[palabra] = [0, 0, 0]
                    diccionario[palabra][indice_diccionario] += 1
                else: diccionario[palabra][indice_diccionario] += 1
        lista_palabras = armar_lista_de_palabras(linea_listada, lista_palabras)
        linea = leer_lineas(texto, contador)
    lista_palabras.sort()
    return [lista_palabras, diccionario]




contador = 0
diccionario = {}
lista_palabras = []
lista_palabras_sin_repetir = []

cuentos = open("archivos_txt/Cuentos.txt", "r", encoding='utf-8-sig')
lista_y_dic_lineal = my_function(cuentos, contador, diccionario, lista_palabras)
for palabra in lista_y_dic_lineal[0]:
    lista_palabras_sin_repetir.append(palabra)
diccionario = {**diccionario, **lista_y_dic_lineal[1]}
cuentos.close()

araña_negra = open("archivos_txt/La araña negra - tomo 1.txt", "r", encoding='utf-8-sig')
lista_y_dic_lineal = my_function(araña_negra, contador, diccionario, lista_palabras)
for palabra in lista_y_dic_lineal[0]:
    lista_palabras_sin_repetir.append(palabra)
diccionario = {**diccionario, **lista_y_dic_lineal[1]}
araña_negra.close()

mil_noches = open("archivos_txt/Las 1000 Noches y 1 Noche.txt", "r", encoding='utf-8-sig')
lista_y_dic_lineal = my_function(mil_noches, contador, diccionario, lista_palabras)
for palabra in lista_y_dic_lineal[0]:
    lista_palabras_sin_repetir.append(palabra)
diccionario = {**diccionario, **lista_y_dic_lineal[1]}
mil_noches.close()

# prueba = open("archivos_txt/prueba.txt", 'r', encoding='utf-8-sig')
# lista_y_dic_lineal = my_function(prueba, contador, diccionario, lista_palabras)
# for palabra in lista_y_dic_lineal[0]:
#     lista_palabras_sin_repetir.append(palabra)
# diccionario = {**diccionario, **lista_y_dic_lineal[1]}
# prueba.close()

# prueba2 = open("archivos_txt/prueba2.txt", "r", encoding='utf-8-sig')
# lista_palabras = []
# lista_y_dic_lineal = my_function(prueba2, contador, diccionario, lista_palabras)
# for palabra in lista_y_dic_lineal[0]:
#     lista_palabras_sin_repetir.append(palabra)
# diccionario = {**diccionario, **lista_y_dic_lineal[1]}
# prueba2.close()

print(lista_palabras_sin_repetir, "\n", "\n", diccionario)
# close(cuentos)
# close(araÃ±a_negra)
# close(mil_noches)