import math

tablero=[]#Nuestro tablero sera un array
TABLERO_COLUMNAS = 3
TABLERO_FILAS = 3
#Inicializamos nuestro tablero con nueve posiciones
for i in range(9):
    tablero.append(" ")


#Funcion para solicitar fila, columna y comprobar que sea numerico
#Argumentos: Lo que va a imprimir para recibir
def Coordenada(literal,inferior,superior):
    #Se ejecuta el whiile mientras no retorne
    while True:
        #Solicita un valor
        valor = input(literal)
        #Comprueba que sea numerico para no volver a solicitar el valor
        while(not valor.isnumeric()):
                print("El valor indicado es incorrecto, introduzca un numero entre {0} y {1}".format(inferior,superior))
                valor=input(literal)
        coor = int(valor)
        #Si el valor esta dentro del rango, retorna
        if (coor>=inferior and coor<=superior):
            return coor
        else:
            print("El valor ingresado es incorrecto, introduzca un numero entre {0} y {1}".format(inferior,superior))

#Funcion: Coloca una ficha en el tablero
#Argumento: Ficha a colocar 'X,O'
def ColocarFicha(ficha):
    print("Dame posiciones para la ficha:")
    #Repite la instruccion hasta introducir un numero correcto
    while True:
        fila=Coordenada("Fila entre [1 y 3]: ",1,3) - 1 #Restamos uno porque nuestro rango esta en [0,2]
        columna=Coordenada("Columna entre [1 y 3]: ",1,3) - 1 #Restamos uno porque nuestro rango esta en [0,2]
        
        #Como mi tablero es de 3x3 hago un calculo para saber donde esta mi dato
        casilla = fila*TABLERO_COLUMNAS+columna
        if(tablero[casilla] != " "):
            #Esa casilla ya esta cubierta
            print("La casilla ya esta ocupada")
        else:
            tablero[casilla]=ficha
            return casilla

#Funcion para pintar el tablero
def PintarTablero():
    print(("-"*18))
    pos=0 #posicion del tablero
    for fila in range (3): #Recorre 3 veces fila
        
        for columna in range (3): #Recorre 3 veces columna para cada fila
            pos=fila*3+columna
            print("| ",tablero[pos], " ", end='')
        print("|\n",("-"*18))


def numeroHermanos(casilla,ficha, v, h):
    f = math.floor(casilla/TABLERO_COLUMNAS) #Obtengo la fila como numero entero
    c = casilla % TABLERO_COLUMNAS #Obtengo la columna como el decimal de un operador
    fila_nueva = f + v
    if (fila_nueva < 0 or fila_nueva >= TABLERO_FILAS):
        return 0    #Estamos en el limite
    columna_nueva = c + h
    if (columna_nueva < 0 or columna_nueva >= TABLERO_COLUMNAS):
        return 0    #Estamos en el limita
    
    #No estamos en el limite asi que
    #Calculamos nueva posicion y vemos si esta la misma ficha
    pos = (fila_nueva * TABLERO_COLUMNAS + columna_nueva)
    if(tablero[pos]!=ficha):
        return 0
    else:
        return 1 + numeroHermanos(pos,ficha,v,h)

#Metodo para comprobar quien es el ganador
#Comprobamos que la ficha colocada en la casilla indicada tiene hermanos iguales que formen 3 en raya
def ComprobarGanador(casilla,ficha):
    hermanos = numeroHermanos(casilla,ficha,-1,-1) + numeroHermanos(casilla,ficha,1,1)
    if (hermanos==2):
        return True
    
    hermanos = numeroHermanos(casilla,ficha,1,-1) + numeroHermanos(casilla,ficha,-1,1)
    if (hermanos==2):
        return True
    
    hermanos = numeroHermanos(casilla,ficha,-1,0) + numeroHermanos(casilla,ficha,1,0)
    if (hermanos==2):
        return True
    
    hermanos = numeroHermanos(casilla,ficha,0,-1) + numeroHermanos(casilla,ficha,0,1)
    if (hermanos==2):
        return True
    

#Funcion principal,(Controla todo el juego y funciones)
def run_game():
    #Pide nombre de jugador 1y2
    jugador1 = input("Ingrese el nombre del jugador 1:  ")
    jugador2 = input("Ingrese el nombre del jugador 2:  ")

    #Inicia el juego
    continuar = True
    fichasEnTablero=0
    while continuar:
        #Pintamos el tablero
        PintarTablero()

        #Pedimos posiciones para la ficha, y mandamos la ficha a colocar
        ficha = ('X' if (fichasEnTablero&1) else 'O')
        casilla = ColocarFicha(ficha)

        #Comprueba ganador enviando la casilla en donde se coloco la ultima ficha
        if (ComprobarGanador(casilla,ficha)):
            continuar = False
            print("Has ganado")


        #Se actualizan las fichas colocadas
        fichasEnTablero+=1
        #Comprueba que el tablero no este lleno
        if(fichasEnTablero == 9):
            #Si el tablero esta lleno termina el juego
            continuar=False
    PintarTablero()
if __name__ == "__main__":
    run_game()




