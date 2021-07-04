from os import close

def leer_lineas(archivo, contador):
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        devolucion = linea
    elif not linea and contador < 6:
        devolucion = leer_lineas(archivo, contador + 1)
    else: devolucion = None
    return devolucion

# cuentos = open("archivos_txt/Cuentos.txt", "r")
# araÃ±a_negra = open("archivos_txt/La araÃ±a negra - tomo 1.txt", "r")
# mil_noches = open("archivos_txt/Las 1000 Noches y 1 Noche.txt", "r")
contador = 0
prueba = open("archivos_txt/prueba.txt", 'r', encoding='utf-8-sig')
prueba_escritura = open("archivos_txt/fffff.txt", "w", encoding='utf-8-sig')
linea = leer_lineas(prueba, contador)
while linea:
    prueba_escritura.write(linea + "\n")
    linea = leer_lineas(prueba, contador)
prueba.close()






# close(cuentos)
# close(araÃ±a_negra)
# close(mil_noches)