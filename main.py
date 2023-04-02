
tablero=[]#Nuestro tablero sera un array
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
        casilla = fila*3+columna
        if(tablero[casilla] != " "):
            #Esa casilla ya esta cubierta
            print("La casilla ya esta ocupada")
        else:
            tablero[casilla]=ficha
            return

#Funcion para pintar el tablero
def PintarTablero():
    print(("-"*18))
    pos=0 #posicion del tablero
    for fila in range (3): #Recorre 3 veces fila
        
        for columna in range (3): #Recorre 3 veces columna para cada fila
            pos=fila*3+columna
            print("| ",tablero[pos], " ", end='')
        print("|\n",("-"*18))


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

        #Pedimos posiciones para la ficha
        ColocarFicha('X' if (fichasEnTablero&1) else 'O')
        
        fichasEnTablero+=1
        #Comprueba que el tablero no este lleno
        if(fichasEnTablero == 9):
            #Si el tablero esta lleno termina el juego
            continuar=False
        


    
if __name__ == "__main__":
    run_game()




