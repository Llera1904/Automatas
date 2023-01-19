import numpy as np
import random
from graphics import *

def animate(animation):
    id = GraphWin("Animation", 340, 140)
    for animation in animations:
        textInput = Text(Point(170, 70), animation)
        textInput.draw(id)
        time.sleep(0.5)
        textInput.undraw()
    
def instantPrints(txt):
    id = GraphWin("ID'S", 340, 140)
    textInput = Text(Point(170, 70), txt)
    textInput.draw(id)
    id.getMouse() 
    id.close()

def newString(actualEstate, newCharacter, direction, i, txt): # Mueve el estado 
    string[i + 1] = newCharacter 
    if direction == "R":
        aux = string[i + 1]
        string[i + 1] = actualEstate
        string[i] = aux
        i += 1
    elif direction == "L":
        aux = string[i - 1]
        string[i - 1] = actualEstate
        string[i] = aux
        i -= 1
    txt.write(str(string) + "\n")
    instantPrints(str(string))
    # print(string)

    return i, str(string)

def binaryString(size): # Crea una cadena binaria aleatoria (Funcional si la cadena es pequeña)
    string = ""
    for _ in range(size):
        number = random.randint(0, 1)
        string += str(number)

    return string 

while 1:
    print("1. Generar cadena")
    print("2. Ingresar cadena")
    op = input("Ingresa opcion: ")

    if op != '1' and op != '2':
        print("\nOpcion invalida\n")
    elif op == '1':
        numberRandom = random.randint(1, 100000)
        string = binaryString(numberRandom)
        print("\nTamaño cadena:", len(string))
        break
    elif op == '2':
        string = input("Ingresa la cadena: ")
        print("\nTamaño cadena:", len(string))
        break

# string = "01010101" 
actualEstate = "q0" # Estado
stringAnimate = list(string)
string = list(string + "B")
string = np.array(string)
string = np.append("q0", [string])
print("Cadena en el estado inicial:", string)

animations = []
with open("IDs.txt", "w") as txt:
    txt.write(str(string) + "\n")
    instantPrints(str(string))
    i = 0 # indice del estado en el que se encuentra  
    while 1:
        if actualEstate == "q0":
            if string[i + 1] == "0":
                actualEstate = "q1"
                i, s = newString(actualEstate, "X", "R", i, txt)
                animations.append(s)
            elif string[i + 1] == "1":
                print("Cadena invalida")
                break
            elif string[i + 1] == "X":
                print("Cadena invalida")
                break
            elif string[i + 1] == "Y":
                actualEstate = "q3"
                i, s = newString(actualEstate, "Y", "R", i, txt)
                animations.append(s)
            elif string[i + 1] == "B":
                print("Cadena invalida")
                break

        elif actualEstate == "q1":
            if string[i + 1] == "0":
                actualEstate = "q1"
                i, s= newString(actualEstate, "0", "R", i, txt)
                animations.append(s)
            elif string[i + 1] == "1":
                actualEstate = "q2"
                i, s = newString(actualEstate, "Y", "L", i, txt)
                animations.append(s)
            elif string[i + 1] == "X":
                print("Cadena invalida")
                break
            elif string[i + 1] == "Y":
                actualEstate = "q1"
                i, s = newString(actualEstate, "Y", "R", i, txt)
                animations.append(s)
            elif string[i + 1] == "B":
                print("Cadena invalida")
                break

        elif actualEstate == "q2":
            if string[i + 1] == "0":
                actualEstate = "q2"
                i, s = newString(actualEstate, "0", "L", i, txt)
                animations.append(s)
            elif string[i + 1] == "1":
                print("Cadena invalida")
                break
            elif string[i + 1] == "X":
                actualEstate = "q0"
                i, s = newString(actualEstate, "X", "R", i, txt)
                animations.append(s)
            elif string[i + 1] == "Y":
                actualEstate = "q2"
                i, s = newString(actualEstate, "Y", "L", i, txt)
                animations.append(s)
            elif string[i + 1] == "B":
                print("Cadena invalida")
                break

        elif actualEstate == "q3":
            if string[i + 1] == "0":
                print("Cadena invalida")
                break
            elif string[i + 1] == "1":
                print("Cadena invalida")
                break
            elif string[i + 1] == "X":
                print("Cadena invalida")
                break
            elif string[i + 1] == "Y":
                actualEstate = "q3"
                i, s = newString(actualEstate, "Y", "R", i, txt)
                animations.append(s)
            elif string[i + 1] == "B":
                actualEstate = "q4"
                np.append(string, "B")
                i, s = newString(actualEstate, "B", "R", i, txt)
                animations.append(s)
                print("Cadena valida")
                break

        # elif actualEstate == "q4":
        #     if string[i + 1] == "0":
        #         print("Cadena invalida")
        #         break
        #     elif string[i + 1] == "1":
        #         print("Cadena invalida")
        #         break
        #     elif string[i + 1] == "X":
        #         print("Cadena invalida")
        #         break
        #     elif string[i + 1] == "Y":
        #         print("Cadena invalida")
        #         break
        #     elif string[i + 1] == "B":
        #         print("Cadena invalida")
        #         break

if len(stringAnimate) <= 10:
    animate(animations)





    