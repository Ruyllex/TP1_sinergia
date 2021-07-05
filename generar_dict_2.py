from generar_diccionario import eliminar_caracteres_especiales, armar_lista_de_palabras
from salida_de_datos import eliminar_tildes
from os import close
import time
incio=time.time()

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

    def my_function(texto, contador, diccionario):
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


    diccionario = my_function(cuentos, contador, diccionario)
    cuentos.close()

    
    diccionario = my_function(araña_negra, contador, diccionario)
    araña_negra.close()

    
    diccionario = my_function(mil_noches, contador, diccionario)
    mil_noches.close()
    return diccionario

def generar_palaras_csv():
    #almacena las palabras en palabras.csv
    diccionario=generar_diccionario()
    lista_palabras_sin_repetir=list(diccionario.keys())
    lista_palabras_sin_repetir.sort()
    palabras = open("palabras.csv", "w", encoding="utf-8-sig")
    for palabra in lista_palabras_sin_repetir:
        palabras.write(palabra + "," + str(diccionario[palabra][0]) + "," + str(diccionario[palabra][1]) + "," + str(diccionario[palabra][2]) + "\n")
    palabras.close()

    

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


fin=time.time()
print(fin-incio)
# close(cuentos)
# close(araÃ±a_negra)
# close(mil_noches)
