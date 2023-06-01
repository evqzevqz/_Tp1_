#from datos import frases_de_peliculas
from funciones import funciones

ruta = "datos/" 
 
listapeli=funciones.lector_txt("frases_de_peliculas.txt" , ruta)
#ruta = "/datos/" 

frasespeliculas = []
peliculas = []
for i in listapeli:
    i = i.rstrip()
    i = i.split(";")
    frasespeliculas.append(i)
    peliculas.append(i[1])
    
    
frasespeliculas=funciones.ordenador(frasespeliculas)
peliculas= funciones.sacar_repetidos(peliculas)

#%% EJ 2
def ej_2():
    import random
    pelis=[]
    for i in frasespeliculas:
        pelis.append(i[1])
        
        
    peli_1,peli_2,peli_3=random.sample(pelis,3)

    lista_pelis=[peli_1,peli_2,peli_3]
    a=random.choice(lista_pelis)


    for i in range(len(frasespeliculas)):
        if frasespeliculas[i][1]==a:
            frase=frasespeliculas[i][0]
            peli_frase=frasespeliculas[i][1]
        
    opciones=int(input(f'La Frase:\n"{frase}"\n A que pelicula pertenece?\n1) {peli_1}\n2) {peli_2}\n3) {peli_3}\n--> '))

    if lista_pelis[opciones-1]==peli_frase:
        return print("Correcto :)")
    else:
        return print("Incorrecto :(")


#%% Interfaz
historial=[]

try: 
    with open("historialconsola.txt","r"):
        print("se leyo archivo anterior")
        
    
except:
    with open("historialconsola.txt","w"):
        print("se creo archivo de almacenamiento")

while True:
    op=int(input("""#######################################
    #  Películas: Preguntas y respuestas  #
    #######################################
    Elige una opción
    1 - Mostrar lista de películas.
    2 - ¡Trivia de película!
    3 - Mostrar secuencia de opciones seleccionadas previamente.
    4 - Borrar historial de opciones.
    5 - Salir
    ->  """
    ))

    if op==1:
        print()
        print("La lista de peliculas es:\n")
        for i in peliculas:
            x = (peliculas.index(i)+1)
            print( x , i )
        print()
        funciones.add_historial(1)
        
    elif op==2:
        print()
        ej_2()
        funciones.add_historial(2)
        
    elif op==3:
        """ver secuencia de opciones seleccionadas """
        funciones.add_historial(3)
       
        with open("historialconsola.txt","r") as archi_historial_leer:
            datos=archi_historial_leer.readlines()
            for i in datos:
                print(i)
        print()
    
        
    elif op==4:
        """"borrar historial"""
        print()
        funciones.eliminar_dato_txt("historialconsola.txt")
        print()
       
    elif op==5:
        """Salir"""
        print()
        print("fin del programa")
        break


