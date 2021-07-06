#-----------CONFIGURACIONES----------------
def leer_lineas(archivo):
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        devolucion = linea
    else: devolucion = ''
    return devolucion

diccionario_default={'MAX_USUARIOS': 10, 'LONG_PALABRA_MIN': 5, 'MAX_DESACIERTOS': 7, 'PUNTOS_ACIERTOS': 10, 'PUNTOS_DESACIERTOS': 5, 'PUNTOS_ADIVINA_PALABRA': 100, 'PUNTOS_RESTA_GANA_PROGRAMA': 20}

def constantes():
    '''retorna un diccionario con las constantes del configuracion.csv'''
    configuraciones = open("configuracion.csv","rt")
    linea=leer_lineas(configuraciones)
    diccionario = {}
    while linea != '':
        linea=linea.split(",")
        try:
            diccionario[linea[0]] = int(linea[1])
            linea = leer_lineas(configuraciones)
        except IndexError:
            diccionario = diccionario_default
            linea = ''
        except ValueError:
            diccionario = diccionario_default
            linea = ''
    configuraciones.close()
    if diccionario_default.keys() != diccionario.keys():
        diccionario = diccionario_default
    return diccionario


def check(diccionario):
    '''chequea si el diccionario es distinto al default'''
    if diccionario != diccionario_default:
        mensaje = "Los valores por defecto en el archivo han sido cambiados"
    else:
        mensaje = "Se mantienen los valores por defecto"
    return mensaje