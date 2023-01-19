from graphics import *
import time
import re 
from AutomataPila import *

# Funcion que genera la animacion 
def moveOnLine(shape, dx, dy, repetitions, delay):
    for i in range(repetitions):
        shape.move(dx, dy)
        time.sleep(delay)

# Crea la pila
def createStack(cadena):
    # Numero de 0's y 1's de la cadena
    var0 = len(re.findall("0", str(cadena)))
    var1 = len(re.findall("1", str(cadena)))

    rectangles = []
    rectangles2 = []
    # Crea el numero de rectangulos de a acuerdo al numero de 0's en la cadena
    for i in range(var0):
        rec = Rectangle(Point(210, 137), Point(410, 167))
        rectangles.append(rec)

    # Mete los rectangulos a la pila
    beforeDy = 366
    for i in range(len(rectangles)):
        rectangles[i].draw(win)
        rectangles[i].setFill("red")
        dy1 = beforeDy - 33
        # print("dy: ", dy1)
        dy = dy1 / 30
        moveOnLine(rectangles[i], 0, dy, 30, 0.05)
        rectangles2.append(rectangles[i])
        beforeDy = dy1

    time.sleep(1)
    index = len(rectangles2) - 1
    coordenatesY = [458, 452, 419, 386, 353, 320, 287, 254, 221, 188]

    # Saca los rectangulos de la pila
    for _ in range(var1):
        center = coordenatesY[index]
        dy1 = center - 152           # 152 es la coordenada y del centro del rectangulo de hasta arriba 
        dy = dy1 / -30
        moveOnLine(rectangles2[index], 0, dy, 30, 0.05)
        rectangles2[index].undraw()
        index -= 1


# Main
win = GraphWin("Stack", 640, 640)
win.setBackground("black")
# point = win.getMouse()
# print(point)

# Hacemos las lineas para la pila
leftLine = Line(Point(207, 170), Point(207, 503))
leftLine.draw(win)
leftLine.setFill("white")

downLine = Line(Point(207, 503), Point(413, 503))
downLine.draw(win)
downLine.setFill("white")

rightLine = Line(Point(413, 170), Point(413, 503))
rightLine.draw(win)
rightLine.setFill("white")

# cadena = "00000000001111"
if len(string) <= 10:
    createStack(string)
else:
    print("Cadena no aceptada para animacion")

# rectangles = [Rectangle(Point(210, 470), Point(410, 500)), Rectangle(Point(210, 437), Point(410, 467)), Rectangle(Point(210, 404), Point(410, 434)),
# Rectangle(Point(210, 371), Point(410, 401)), Rectangle(Point(210, 338), Point(410, 368)), Rectangle(Point(210, 305), Point(410, 335)),
# Rectangle(Point(210, 272), Point(410, 302)), Rectangle(Point(210, 239), Point(410, 269)), Rectangle(Point(210, 206), Point(410, 236)),
# Rectangle(Point(210, 173), Point(410, 203))]

# rec = Rectangle(Point(210, 338), Point(410, 368))
# rec.draw(win)
# rec.setFill("Red")
# print("Centro: ", rec.getCenter())

win.getMouse() # pause for click in window
win.close()





