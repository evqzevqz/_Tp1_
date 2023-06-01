from flask import * 
from funciones import funciones 
app = Flask(__name__)

RUTA = "datos/"
ARCHIVO = RUTA + "historial.txt"

import time
import random
import datetime

pelis=[]
frasespeliculas = []
peliculas = []
listapeli=funciones.lector_txt("frases_de_peliculas.txt" , RUTA)

peli_frase = ""  
frase = ""
cont2 = 0
puntos = 0


for i in listapeli:
    i = i.rstrip()
    i = i.split(";")
    frasespeliculas.append(i)
    peliculas.append(i[1])


frasespeliculas=funciones.ordenador(frasespeliculas)
peliculas= funciones.sacar_repetidos(peliculas)


for i in frasespeliculas:
    pelis.append(i[1])


@app.route("/", methods=['GET', 'POST'])
def index():  
    global frase 
    global peli_frase
    global puntos
    global cont2
    cont2 = 0
    puntos = 0 
    return render_template("indexxx.html")

lista_pelis=[]

@app.route("/juego", methods=['GET', 'POST'])
def juego():
    global frase 
    global peli_frase
    global cont2
    global puntos 
    global nombre
    peli_1,peli_2,peli_3=random.sample(pelis,3)

    lista_pelis=[peli_1,peli_2,peli_3]
    a=random.choice(lista_pelis)
    for i in range(len(frasespeliculas)):
        if frasespeliculas[i][1]==a:
            lista_pelis.append(a)
            frase=frasespeliculas[i][0]
            peli_frase=frasespeliculas[i][1]
    
    for i in frasespeliculas:
        if i[0] == peli_frase:
            frasespeliculas.remove(i)


    if cont2 == 0:
        nombre =  request.form["nombre"]
    if cont2 <5:   
            return render_template("juego.html" , cont2 = cont2 , frase=frase , peli_frase=peli_frase, lista_pelis=lista_pelis)
    if cont2 == 5:
        global RUTA
        global ARCHIVO 
        with open( ARCHIVO ,"a") as hist_1:
         hist_1.write(f"{nombre} {puntos} {datetime.datetime.now().strftime('%x %H:%M:%S')} \n")  
        return render_template("resultados.html", puntos=puntos)
    

@app.route('/guardar_boton', methods=['GET', 'POST'])
def guardar_boton():
    global peli_frase
    global frase 
    global cont2
    global puntos
    boton_oprimido = request.form["boton"]
    cont2 += 1
    # aquí puedes hacer lo que necesites con el botón oprimido por el usuario
    while cont2 <= 5:
        if boton_oprimido == peli_frase:
            puntos += 1
            return render_template("correcto.html" , peli_frase=peli_frase , frase=frase )
        else:
            return render_template("incorrecto.html", peli_frase=peli_frase , frase=frase )
         
@app.route("/historial", methods=['GET', 'POST'])
def historial():  
    global ARCHIVO
    historialeditado = []
    with open( ARCHIVO ,"r") as hist_1:
        lectura = hist_1.readlines()
        for i in lectura:
            i = i.rstrip()
            i = i.split(",")
            historialeditado.append(i)

        return render_template("historial.html" , historialeditado=historialeditado)

if __name__ == "__main__":
    app.run(debug = True)


#repetidos
