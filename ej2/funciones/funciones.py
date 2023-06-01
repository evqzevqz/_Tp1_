def lector_txt(archivo , RUTA):
    """Esta funcion lee un archivo txt y lo almacena en una lista"""
    #global RUTA
    archi = open( RUTA + archivo , "r", encoding="UTF-8")
    datos_archivo = archi.readlines()
    return datos_archivo

def ordenador(matriz):
    """Esta funcion ordena una matriz a partir del elemento 1 de forma alfabetica decreciente"""
    matriz.sort(key=lambda x:x[1],reverse=True)
    return matriz

def sacar_repetidos(lista):
    """esta funcion saca los repetidos de una lista de str"""
    lista=list(set(lista))
    lista.sort()
    return lista

def add_historial(ejercicio):

    import datetime
    with open("historialconsola.txt","a") as hist_1:
        hist_1.write(f"{ejercicio} {str(datetime.datetime.now())}\n")

def eliminar_dato_txt(archivo):
            """esta funcion elimina lo escrito en un txt sobreescribiendolo"""
            
            with open(archivo,"w") as archi_historial:
                archi_historial.write("")