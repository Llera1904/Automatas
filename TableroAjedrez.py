import time
from graphics import *
from AutomataAjedrez import *

# Funcion que genera la animacion 
def moveOnLine(shape, dx, dy, repetitions, delay):
    for i in range(repetitions):
        shape.move(dx, dy)
        time.sleep(delay)

win = GraphWin("Chessboard", 640, 640)

rectangle1 = Rectangle(Point(20, 20), Point(170, 170))
rectangle2 = Rectangle(Point(170, 20), Point(320, 170))
rectangle3 = Rectangle(Point(320, 20), Point(470, 170))
rectangle4 = Rectangle(Point(470, 20), Point(620, 170))
rectangle5 = Rectangle(Point(20, 170), Point(170, 320))
rectangle6 = Rectangle(Point(170, 170), Point(320, 320))
rectangle7 = Rectangle(Point(320, 170), Point(470, 320))
rectangle8 = Rectangle(Point(470, 170), Point(620, 320))
rectangle9 = Rectangle(Point(20, 320), Point(170, 470))
rectangle10 = Rectangle(Point(170, 320), Point(320, 470))
rectangle11 = Rectangle(Point(320, 320), Point(470, 470))
rectangle12 = Rectangle(Point(470, 320), Point(620, 470))
rectangle13 = Rectangle(Point(20, 470), Point(170, 620))
rectangle14 = Rectangle(Point(170, 470), Point(320, 620))
rectangle15 = Rectangle(Point(320, 470), Point(470, 620))
rectangle16 = Rectangle(Point(470, 470), Point(620, 620))

rectangle1.draw(win)
rectangle1.setFill("black")
rectangle2.draw(win)
rectangle2.setFill("red")
rectangle3.draw(win)
rectangle3.setFill("black")
rectangle4.draw(win)
rectangle4.setFill("red")
rectangle5.draw(win)
rectangle5.setFill("red")
rectangle6.draw(win)
rectangle6.setFill("black")
rectangle7.draw(win)
rectangle7.setFill("red")
rectangle8.draw(win)
rectangle8.setFill("black")
rectangle9.draw(win)
rectangle9.setFill("black")
rectangle10.draw(win)
rectangle10.setFill("red")
rectangle11.draw(win)
rectangle11.setFill("black")
rectangle12.draw(win)
rectangle12.setFill("red")
rectangle13.draw(win)
rectangle13.setFill("red")
rectangle14.draw(win)
rectangle14.setFill("black")
rectangle15.draw(win)
rectangle15.setFill("red")
rectangle16.draw(win)
rectangle16.setFill("black")

# Obtiene los centros de cada cuadro de el tablero
# center = mRectangle.getCenter()
# print("Centro: ", center[0])

if secondPlayer == True: 
    # Dibuja las piezas en sus posiciones iniciales
    pieceT1 = Image(Point(95, 95), "piece.png")
    pieceT1.draw(win)

    pieceT2 = Image(Point(545, 95), "piece.png")
    pieceT2.draw(win)

    # Centro de los rectangulos
    centros = [(95, 95), (245, 95), (395, 95), (545, 95), (95, 245), (245, 245), (395, 245), (545, 245), (95, 395), (245, 395),
    (395, 395), (545, 395), (95, 545), (245, 545), (395, 545), (545, 545)] 
    # print("Lista de centros: ", centros)

    # Asignamos las posiciones iniciales de cada pieza como valores anteriores de indices 
    beforeValuei = centros[0]
    beforeValuej = centros[3]

    # Iteraciones 
    if len(movementsPlayer1) == len(movementsPlayer2):
        iterations = len(movementsPlayer1)
    elif len(movementsPlayer1) > len(movementsPlayer2):
        iterations = len(movementsPlayer1)
    elif len(movementsPlayer1) < len(movementsPlayer2):
        iterations = len(movementsPlayer2)

    # Se hacen los calculos de cada posicion anterior a la siguiente para generar animaciones
    for i in range(iterations):
        if boardFirstPlayer1 == True:
            # Movimiento de la pieza del jugador 1
            indexi = movementsPlayer1[i]
            centroActuali = centros[indexi - 1]
            dx = (centroActuali[0] - beforeValuei[0]) / 30
            dy = (centroActuali[1] - beforeValuei[1]) / 30
            moveOnLine(pieceT1, dx, dy, 30, .05)
            beforeValuei = centroActuali
            
            #Movimiento de la pieza del jugador 2
            indexj = movementsPlayer2[i]
            centroActualj = centros[indexj - 1]
            dx = (centroActualj[0] - beforeValuej[0]) / 30
            dy = (centroActualj[1] - beforeValuej[1]) / 30
            moveOnLine(pieceT2, dx, dy, 30, .05)
            beforeValuej = centroActualj

        if boardFirstPlayer2 == True:
            #Movimiento de la pieza del jugador 2
            indexj = movementsPlayer2[i]
            centroActualj = centros[indexj - 1]
            dx = (centroActualj[0] - beforeValuej[0]) / 30
            dy = (centroActualj[1] - beforeValuej[1]) / 30
            moveOnLine(pieceT2, dx, dy, 30, .05)
            beforeValuej = centroActualj

            #Movimiento de la pieza del jugador 1
            indexi = movementsPlayer1[i]
            centroActuali = centros[indexi - 1]
            dx = (centroActuali[0] - beforeValuei[0]) / 30
            dy = (centroActuali[1] - beforeValuei[1]) / 30
            moveOnLine(pieceT1, dx, dy, 30, .05)
            beforeValuei = centroActuali
else:
    # Dibujamos la pieza en su posicion inicial
    pieceT1 = Image(Point(95, 95), "piece.png")
    pieceT1.draw(win)

    # Centro de los rectangulos
    centros = [(95, 95), (245, 95), (395, 95), (545, 95), (95, 245), (245, 245), (395, 245), (545, 245), (95, 395), (245, 395),
    (395, 395), (545, 395), (95, 545), (245, 545), (395, 545), (545, 545)] 
    # print("Lista de centros: ", centros)

    # Asignamos las posiciones iniciales de cada pieza como valores anteriores de indices 
    beforeValuei = centros[0]

    for i in range(len(movementsPlayer1)): # Movimiento de la pieza del jugador 1
        indexi = movementsPlayer1[i]
        centroActuali = centros[indexi - 1]
        dx = (centroActuali[0] - beforeValuei[0]) / 30
        dy = (centroActuali[1] - beforeValuei[1]) / 30
        moveOnLine(pieceT1, dx, dy, 30, .05)
        beforeValuei = centroActuali

win.getMouse() # Pause for click in window
win.close()