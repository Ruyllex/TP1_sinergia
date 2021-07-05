#-----------CONFIGURACIONES----------------
def leer_lineas(archivo):
    linea = archivo.readline()
    linea = linea.rstrip('\n')
    if linea:
        devolucion = linea
    else: devolucion = ''
    return devolucion

def constantes():
    '''returna diccionario con las constantes del configuracion.csv'''
    configuraciones=open("configuracion.csv","rt")
    linea=leer_lineas(configuraciones)
    dicc={}
    while linea!='':
        linea=linea.split(",")
        dicc[linea[0]]=int(linea[1])
        linea=leer_lineas(configuraciones)
    configuraciones.close()
    return dicc


