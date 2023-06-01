ruta = "datos/"

def leer_csv(archivo):
    """Lee un arcchivo csv con delimitador en , y lo pone en una matriz de n x 2"""
    import csv
    global ruta
    matriz=[]
    with open( ruta + archivo  ) as archivo_:
        datos_archivo=csv.reader(archivo_, delimiter = ",")
        for i in datos_archivo:
            matriz.append([i[0],i[1]])
    return matriz
        

def dif_porcentual(primer_valor , segundo_valor):
    resultado = abs((primer_valor - segundo_valor)/segundo_valor * 100)
    return(resultado)

def agregar_a_lista(matriz,posicion):
    """Agrega a una lista el elemento de la matriz que se le pase"""
    lista_a_agregar=[]
    for i in matriz:
        lista_a_agregar.append(float(i[posicion]))
    return lista_a_agregar

def rematriz(valor_inicial,matriz_datos):
    matriz= [[None, None] for i in range(len(matriz_datos)-1)]
    for i in range(1, len(matriz_datos)):
        matriz[i-1][0] = matriz_datos[i][0]
        matriz[i-1][1] = ((float(matriz_datos[i][1]) - valor_inicial) / valor_inicial) * 100
        
    return matriz

def graficar_plot(eje_x_1,eje_x_2,titulo,referencia,etiqueta_x,etiqueta_y):
    """"eje_x_1 -> LISTA de datos del eje x
        eje_x_2 -> LISTA de datos del eje x
        titulo -> titulo
        referencia -> LISTA de referencias
        etiqueta_x -> nombre de x
        etiqueta_y -> nombre de y"""
    
    import matplotlib.pyplot as plt
    # Crear la figura y los ejes
    fig, ax = plt.subplots()
    ax.plot(eje_x_1)
    ax.plot(eje_x_2)
    plt.xlabel(str(etiqueta_x))
    plt.ylabel(str(etiqueta_y))
    plt.title(str(titulo))
    plt.legend(referencia)
    plt.grid()
    plt.show()
