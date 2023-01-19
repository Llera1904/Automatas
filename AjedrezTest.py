import random
import linecache
import re

def Adjacency():
    number = 1
    for i in range(sizeBoard):
        for j in range(sizeBoard):
            if i - 1 >= 0 and j - 1 >= 0:
                if board[i-1][j-1] == 0:
                    adjacency[number][0].append(boardNumbers[i-1][j-1])
                elif  board[i-1][j-1] == 1:
                    adjacency[number][1].append(boardNumbers[i-1][j-1])

            if i - 1 >= 0:
                if board[i-1][j] == 0:
                    adjacency[number][0].append(boardNumbers[i-1][j])
                elif  board[i-1][j] == 1:
                    adjacency[number][1].append(boardNumbers[i-1][j])

            if i - 1 >= 0 and j + 1 < sizeBoard:
                if board[i-1][j+1] == 0:
                    adjacency[number][0].append(boardNumbers[i-1][j+1])
                elif  board[i-1][j+1] == 1:
                    adjacency[number][1].append(boardNumbers[i-1][j+1])

            if j - 1 >= 0:
                if board[i][j-1] == 0:
                    adjacency[number][0].append(boardNumbers[i][j-1])
                elif  board[i][j-1] == 1:
                    adjacency[number][1].append(boardNumbers[i][j-1])

            if j + 1 < sizeBoard:
                if board[i][j+1] == 0:
                    adjacency[number][0].append(boardNumbers[i][j+1])
                elif  board[i][j+1] == 1:
                    adjacency[number][1].append(boardNumbers[i][j+1])

            if i + 1 < sizeBoard and j - 1 >= 0:
                if board[i+1][j-1] == 0:
                    adjacency[number][0].append(boardNumbers[i+1][j-1])
                elif  board[i+1][j-1] == 1:
                    adjacency[number][1].append(boardNumbers[i+1][j-1])

            if i + 1 < sizeBoard:
                if board[i+1][j] == 0:
                    adjacency[number][0].append(boardNumbers[i+1][j])
                elif  board[i+1][j] == 1:
                    adjacency[number][1].append(boardNumbers[i+1][j])

            if i + 1 < sizeBoard and j + 1 < sizeBoard:
                if board[i+1][j+1] == 0:
                    adjacency[number][0].append(boardNumbers[i+1][j+1])
                elif  board[i+1][j+1] == 1:
                    adjacency[number][1].append(boardNumbers[i+1][j+1])

            number += 1

# def AutomataSolutions1(stateInitial):
#     actualMovements = [[stateInitial]] # Estado inicial 
#     previousStates = []
#     winMovements = []
#     loseMovements = []

#     for movement in stringPlayed:
#         previousStates = actualMovements
#         actualStates = []
#         actualMovements = []

#         for move in range(len(previousStates)):

#             lastValue = len(previousStates[move]) - 1
#             if movement == "0":
#                 actualStates = adjacency[previousStates[move][lastValue]][0]
#             elif movement == "1":
#                 actualStates = adjacency[previousStates[move][lastValue]][1]

#             for actualState in actualStates:
#                 actualMovements.append(previousStates[move] + [actualState]) # Guarda todas las cadenas

#                 # Separa las cadenas en ganadoras y perdedoras 
#                 if (len(previousStates[move] + [actualState]) == sizeBoard + 1) and actualState == finalState1:
#                     winMovements.append(previousStates[move] + [actualState])
#                 elif (len(previousStates[move] + [actualState]) == sizeBoard + 1) and actualState != finalState1:
#                     loseMovements.append(previousStates[move] + [actualState])

#     # print(actualMovements)
#     # print("\n")
#     # print(winMovements)
#     # print("\n")
#     # print(loseMovements)

#     with open("jugadasJugador1.txt", "w") as data:
#         for moves in actualMovements:
#             data.write(str(moves) + "\n")

#     with open("jugadasGanadorasJugador1.txt", "w") as data:
#         for moves in winMovements:
#             data.write(str(moves) + "\n")

#     with open("jugadasPerdedorasJugador1.txt", "w") as data:
#         for moves in loseMovements:
#             data.write(str(moves) + "\n")

#     actualMovements = []
#     winMovements = []
#     loseMovements = []

# def AutomataSolutions(initialState, finalState, solutions, win, lose):
#     nextStates = [initialState] # Siguientes nodos por expandir
#     movements = [] # Guardaremos los caminos
#     amountNodes = [] # Cantidad de nodos a expandir
    
#     actualState = initialState # Empezamos en el estado inicial
#     layer = 0 # Capa inicial del arbol 
#     movement = stringPlayed[0] # Agregamos el inicio de la cadena 
#     movements.append(actualState) # Agregamos el movimiento inicial 
#     amountNodes.append(len(adjacency[initialState][int(stringPlayed[0])])) # Agregamos la cantidad de los primeros nodos a expandir 
#     backtracking = True
#     combinations = 0

#     while len(amountNodes) != 0:
#         if movement == "0":
#             nextStates = adjacency[actualState][0]
#         elif movement == "1":
#             nextStates = adjacency[actualState][1]
#         # print("Estados siguientes" , nextStates)

#         if backtracking == False:
#             amountNodes.append(len(nextStates)) 
         
#         if amountNodes[-1] > 0: # Recorre el arbol de soluciones 
#             actualState = nextStates[amountNodes[-1] - 1]
#             # print("Estado actual", actualState)
#             # amountNode = amountNodes[-1] - 1 # Quitamos un nodo a expandir
#             # amountNodes[-1] = amountNode
#             amountNodes[-1] -= 1
#             movements.append(actualState)
#             layer += 1
#             backtracking = False
            
#             if len(movements) == len(stringPlayed) + 1: # Llego a una solucion 
#                 combinations += 1 # Va contando las jugadas posibles

#                 if movements[-1] == finalState: # Separa las jugadas 
#                     win.write(str(movements) + "\n")
#                 else:
#                     lose.write(str(movements) + "\n")
#                 solutions.write(str(movements) + "\n")
#                 print(movements)

#                 # Quita el ultimo nodo porque ya llego a un nodo terminal
#                 movements.pop()
#                 actualState = movements[-1]
#                 layer -= 1
                
#                 # Backtracking
#                 while amountNodes[-1] == 0: # Va quitando los nodos expandidos 
#                     movements.pop()
#                     amountNodes.pop()

#                     if len(movements) == 0:
#                         break

#                     actualState = movements[-1]
#                     layer -= 1
            
#                 backtracking = True

#         movement = stringPlayed[layer]
#     print("\nTotal caminos posibles:", combinations)

stringPlayed = "011" # Cadena entrada 
board = [] # Tablero con los colores
boardNumbers = [] # Tablero con los numeros
adjacency = {} # Diccionario con las adyacencias de las casillas 
white = 1 # b
black = 0 # r
sizeBoard = 4 # Tamaño del tablero 
initialState1 = 1
initialState2 = 3
finalState1 = 9
finalState2 = 7

# print("Inicio juagador1: ", initialState1)
# print("Final jugador1:", finalState1)
# print("Inicio juagador2: ", initialState2)
# print("Final jugador2:", finalState2)
# print("\n")

# Creamos el tablero de forma dinamica 
aux = []
for i in range(sizeBoard):
    aux.append(0)

number = 1 # Numero inicial del tablero 
actualBox = white # Casilla inicial blanca
for i in range(sizeBoard):
    board.append(aux.copy())
    boardNumbers.append([])

    for j in range(sizeBoard):
        previousBox = actualBox

        if i % 2 != 0 and i != 0:
            board[i][(sizeBoard - 1) - j] = actualBox
        else:
            board[i][j] = actualBox

        boardNumbers[i].append(number)
        adjacency[number] = [[], []]

        if previousBox == white:
            actualBox = black
        elif previousBox == black:
            actualBox = white

        number += 1

print("\nTablero")
for i in board:
    print(i)
print("\n")

print("\nTablero numeros")
for i in boardNumbers:
    print(i)
print("\n")

# Crear matriz de adyacencia 
Adjacency()

# Imprime matriz adyacencia             
for i in range(sizeBoard*sizeBoard):
    print(str(i+1) + " " + str(adjacency[i+1]))      
print("\n") 

# Combinaciones jugador 1
# print("Caminos jugador1: ")
# with open("jugadasJugador1.txt", "w") as solutions:
#     with open("jugadasGanadorasJugador1.txt", "w") as win:
#         with open("jugadasPerdedorasJugador1.txt", "w") as lose:
#             AutomataSolutions(initialState1, finalState1, solutions, win, lose)

# Combinaciones jugador 2
# print("Caminos jugador2: ")
# with open("jugadasJugador2.txt", "w") as solutions:
#     with open("jugadasGanadorasJugador2.txt", "w") as win:
#         with open("jugadasPerdedorasJugador2.txt", "w") as lose:
#             AutomataSolutions(initialState2, finalState2, solutions, win, lose)