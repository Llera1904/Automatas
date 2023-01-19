import random
import linecache
import re
import graphviz as gv

def listInt(string): # Trasforma un string a una lista de enteros 
    patron = re.compile("\d+")
    listString = patron.findall(string)
    listaEntera = []

    for character in listString:
        listaEntera.append(int(character))
    # print(listaEntera)

    return listaEntera.copy()

def binaryString(size): # Crea una cadena binaria aleatoria (Funcional si la cadena es pequeña)
    string = ""
    for _ in range(size):
        number = random.randint(0, 1)
        string += str(number)

    return string 

def findNewPath(solutionsWinPlayer, document, movements, movement): # Encuentra un nuevo camino 
    i = 2
    movePlayer = []
    while i <= solutionsWinPlayer:
        movePlayer = listInt(linecache.getline(document, i))
        if movePlayer[:movement] == movements[:movement] and movePlayer[movement] != movements[movement]:
            return movePlayer.copy(), True
        else:
            i += 1

    return movePlayer.copy(), False

def automataSolutions(actualState, finalState, movements, stringPlayed, allSolutions, win): # Automata que busca todos los caminos
    if stringPlayed ==  "": # Llego a una solucion 
        solutions[0] += 1 # Cuenta cuantas jugadas ha encontrado 
        movements.append(actualState)

        if movements[-1] == finalState: # Separa las jugadas 
            solutionsWin[0] += 1
            win.write(str(movements) + "\n")
        allSolutions.write(str(movements) + "\n")
        # print("Jugada", movements)
        return
    movements.append(actualState)
     
    nextStates = adjacency[actualState][int(stringPlayed[0])] # Determina hacia donde se puede mover
    for state in nextStates:
        automataSolutions(state, finalState, movements.copy(), stringPlayed[1:], allSolutions, win)

def drawPath(path):
    # Crea la ventana
    g = gv.Digraph(format='png', filename='Path1')
    g.graph_attr['rankdir'] = 'LR' # Pinta el grafico de izquierda a derecha 
    g.node("ini", shape="point")

    # Hace el numero de nodos necesarios
    for i in range(len(path)):
        if str(path[i]) == '13' or str(path[i]) == '16':  # Condicion para que haga el doble circulo si llega al estado final
            g.node(str(path[i]), shape="doublecircle")
        g.node(str(path[i]))

    # Hace la conexion entre nodos
    if path[0]:
        g.edge("ini", str(path[0]))
    for i in range(len(path) - 1):
        g.edge(str(path[i]), str(path[i + 1]))
        
    g.view()

adjacency = {} # Diccionario con las adyacencias de las casillas 
red = 0 # r
black = 1 # b
sizeBoard = 4 # Tamaño del tablero 
initialState1 = 1
initialState2 = 4
finalState1 = 16
finalState2 = 13

adjacency = {1: [[2, 5], [6]], 2: [[5, 7], [1, 3, 6]], 3: [[2, 4, 7], [6, 8]], 4: [[7], [3, 8]], 
             5: [[2, 10], [1, 6, 9]], 6: [[2, 5, 7, 10], [1, 3, 9, 11]], 7: [[2, 4, 10, 12], [3, 6, 8, 11]], 8: [[4, 7, 12], [3, 11]], 
             9: [[5, 10, 13], [6, 14]], 10: [[5, 7, 13, 15], [6, 9, 11, 14]], 11: [[7, 10, 12, 15], [6, 8, 14, 16]], 12: [[7, 15], [8, 11, 16]], 
             13: [[10], [9, 14]], 14: [[10, 13, 15], [9, 11]], 15: [[10, 12], [11, 14, 16]], 16: [[12, 15], [11]]}

# Imprime matriz adyacencia             
for i in range(sizeBoard*sizeBoard):
    print(str(i+1) + " " + str(adjacency[i+1]))      
print("\n") 

# Menu
secondPlayer = False
while 1:
    print("1. Un jugador")
    print("2. Dos jugadores")
    print("3. Automatico")
    op = input("Ingresa opcion: ")

    if op != '1' and op != '2' and op != '3':
        print("\nOpcion invalida\n")
    elif op == '1':
        print("\n1. Generar cadena")
        print("2. Ingresar cadena")
        op = input("Ingresa opcion: ")

        if op != '1' and op != '2':
            print("\nOpcion invalida\n")
        elif op == '1':
            numberRandom = random.randint(3, 9)
            stringPlayed1 = binaryString(numberRandom) + '1'
            print("\nCadena jugador1:", stringPlayed1)
            break
        elif op == '2':
            stringPlayed1 = input("Ingresa la cadena para el jugador1: ")
            print("\nCadena jugador1:", stringPlayed1)
            break
    elif op == '2':
        print("\n1. Generar cadena")
        print("2. Ingresar cadena")
        op = input("Ingresa opcion: ")

        if op != '1' and op != '2':
            print("\nOpcion invalida\n")
        elif op == '1':
            numberRandom = random.randint(3, 9)
            stringPlayed1 = binaryString(numberRandom) + '1'
            stringPlayed2 = binaryString(numberRandom) + '0'
            print("\nCadena jugador1:", stringPlayed1)
            print("Cadena jugador2:", stringPlayed2)
            secondPlayer = True
            break
        elif op == '2':
            stringPlayed1 = input("Ingresa la cadena para el jugador1: ")
            stringPlayed2 = input("Ingresa la cadena para el jugador2: ")
            print("\nCadena jugador1:", stringPlayed1)
            print("Cadena jugador2:", stringPlayed2)
            secondPlayer = True
            break
    elif op == '3':
        numberRandom = random.randint(0, 1)
        numberRandom2 = random.randint(3, 9)
        if numberRandom == 0: # Un jugador
            stringPlayed1 = binaryString(numberRandom2) + '1'
            print("\nUn jugador")
            print("Cadena jugador1:", stringPlayed1)
            break
        elif numberRandom == 1: # Dos jugadores 
            stringPlayed1 = binaryString(numberRandom2) + '1'
            stringPlayed2 = binaryString(numberRandom2) + '0'
            print("\nDos jugadores")
            print("Cadena jugador1:", stringPlayed1)
            print("Cadena jugador2:", stringPlayed2)
            secondPlayer = True
            break

# stringPlayed1 = "01101" # Cadena entrada 
# stringPlayed2 = "01100" 

# Jugadas jugador 1
movements = []
solutions = [0]
solutionsWin = [0]
with open("jugadasJugador1.txt", "w") as allSolutions:
    with open("jugadasGanadorasJugador1.txt", "w") as win:
        automataSolutions(initialState1, finalState1, movements.copy(), stringPlayed1, allSolutions, win)
solutionsWinPlayer1 = solutionsWin[0]
print("\nTotal jugadas posibles:", solutions[0])
print("Total jugadas ganadoras:", solutionsWin[0])

movementsPlayer1 = []
movementsPlayer2 = []
if secondPlayer == True: # Si es de dos jugadores 
    # Jugadas jugador 2 
    movements = []
    solutions = [0]
    solutionsWin = [0]
    with open("jugadasJugador2.txt", "w") as allSolutions:
        with open("jugadasGanadorasJugador2.txt", "w") as win:
            automataSolutions(initialState2, finalState2, movements.copy(), stringPlayed2, allSolutions, win)
    solutionsWinPlayer2 = solutionsWin[0]
    print("\nTotal jugadas posibles:", solutions[0])
    print("Total jugadas ganadoras:", solutionsWin[0])

    # Empieza a mover piezas 
    print("\nMovimientos")

    player1 = initialState1 # Casilla inicial del jugador
    player2 = initialState2
    i = 1 # Numero de movimiento
    j = 1
    k = 1 # Jugada ganadora actual 
    l = 1
    movePlayer1 = listInt(linecache.getline("jugadasGanadorasJugador1.txt", k)) # Accede al txt y extrae una jugada ganadora
    movePlayer2 = listInt(linecache.getline("jugadasGanadorasJugador2.txt", l))

    # Determina que jugador empieza 
    numberRandom = random.randint(0, 1)
    firstPlayer1 = False
    boardFirstPlayer1 = False
    boardFirstPlayer2 = False
    firstPlayer2 = False
    if numberRandom == 0:
        firstPlayer1 = True
        boardFirstPlayer1 = True # Para el tablero 
        print("Inicia juagador1")
    elif numberRandom == 1:
        firstPlayer2 = True
        boardFirstPlayer2 = True
        print("Inicia juagador2")

    while 1:
        # Movimiento de los jugadores por el tablero
        if firstPlayer1 == True:
            firstPlayer2 = True

            player1 = movePlayer1[i] 
            if player1 == player2:
                newMovePlayer1, newPathPlayer1 = findNewPath(solutionsWinPlayer1, "jugadasGanadorasJugador1.txt", movePlayer1, i) # Busca un nuevo camino 
                if newPathPlayer1 == True:
                    movePlayer1 = newMovePlayer1
                    player1 = movePlayer1[i] 
                    print("Jugador1 en:", player1)
                    beforePlayer1 = player1 # Respalda el movimineto anterior
                    movementsPlayer1.append(player1) # Lista para la amimacion
                    i += 1
                else:
                    print("Jugador1 pasa, se mantiene en :", beforePlayer1)
                    movementsPlayer1.append(beforePlayer1) # Lista para la amimacion
            else:
                print("Jugador1 en:", player1)
                beforePlayer1 = player1 # Respalda el movimineto anterior 
                movementsPlayer1.append(player1) # Lista para la amimacion
                i += 1

            if player1 == finalState1:
                print("GANO JUGADOR 1")
                if len(movementsPlayer1) <= 10:
                    drawPath(movementsPlayer1)
                break

        if firstPlayer2 == True:
            firstPlayer1 = True

            player2 = movePlayer2[j] 
            if player2 == player1:
                newMovePlayer2, newPathPlayer2 = findNewPath(solutionsWinPlayer2, "jugadasGanadorasJugador2.txt", movePlayer2, j) # Busca un nuevo camino 
                if newPathPlayer2 == True:
                    movePlayer2 = newMovePlayer2
                    player2 = movePlayer2[j]
                    print("Jugador2 en:", player2)
                    beforePlayer2 = player2 # Respalda el movimineto anterior
                    movementsPlayer2.append(player2) # Lista para la amimacion
                    j += 1
                elif newPathPlayer2 == False:
                    print("Jugador2 pasa, se mantiene en :", beforePlayer2)
                    movementsPlayer2.append(beforePlayer2) # Lista para la amimacion
            else:
                print("Jugador2 en:", player2)
                beforePlayer2 = player2 # Respalda el movimineto anterior 
                movementsPlayer2.append(player2) # Lista para la amimacion
                j += 1

            if player2 == finalState2:
                print("GANO JUGADOR 2")
                if len(movementsPlayer2) <= 10:
                    drawPath(movementsPlayer2)
                break
elif secondPlayer == False:
    # Empieza a mover piezas 
    print("\nMovimientos")

    movementsPlayer1 = []
    numberRandom = random.randint(1, solutionsWin[0])
    movePlayer1 = listInt(linecache.getline("jugadasGanadorasJugador1.txt", numberRandom)) # Accede al txt y extrae una jugada ganadora
    for move in movePlayer1:
        player1 = move
        movementsPlayer1.append(player1) # Lista para la amimacion
        print("Jugador1 en:", player1)

    if len(movementsPlayer1) <= 10: # Grafica grafo
        drawPath(movementsPlayer1)

print("\nMoviminetos tablero player1: ", movementsPlayer1)
print("Moviminetos tablero player2: ", movementsPlayer2)