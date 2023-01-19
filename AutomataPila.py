import random
import numpy as np

# def binaryString(size): # Crea una cadena binaria aleatoria (Funcional si la cadena es pequeña)
#     string = ""
#     for _ in range(size):
#         number = random.randint(0, 1)
#         string += str(number)

#     return string 

def binaryString(size): # Crea una cadena binaria aleatoria (Funcional si la cadena es pequeña)
    string = ""
    numberRandom = random.randint(1, 50000)
    for _ in range(numberRandom):
        string += '0'
 
    # numberRandom2 = random.randint(1, 50000)
    for _ in range(numberRandom):
        string += '1'

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

# string = "00111"

with open("IDs.txt", "w") as txt:
    pila = []
    validString = True
    state = 'q'
    # print("\n")
    # print("(q0,", string + ", " + ''.join(pila) + "z0)")
    txt.write("(q0, " + string + ", " + ''.join(pila) + "z0)" + "\n")
    for i in range(len(string)):
        if string[i] == '0':
            if state == 'q':
                pila.append('x')

            # print("(q,", string[i+1:] + ", " + ''.join(pila) + "z0)")
            txt.write("(q, " + string[i+1:] + ", " + ''.join(pila) + "z0)" + "\n")
        elif string[i] == '1': 
            state = 'p'
            if len(pila) != 0: 
                if state == 'p':
                    pila.pop(-1)
                
                # print("(p,", string[i+1:] + ", " + ''.join(pila) + "z0)")
                txt.write("(p, " + string[i+1:] + ", " + ''.join(pila) + "z0)" + "\n")

                if len(pila) == 0 and (i != len(string) - 1): # Ya vacio la pila y no ha terminado de leer la cadena 
                    validString = False
                    break
            else: # La cadena inicia con 1
                # print("(p,", string[i+1:] + ", " + ''.join(pila) + "z0)")
                txt.write("(p, " + string[i+1:] + ", " + ''.join(pila) + "z0)" + "\n")
                validString = False
                break 
            
    if validString == True and len(pila) == 0:
        # print("(f, E, z0)")
        txt.write("(f, E, z0)")
        print("Cadena aceptada")
    else:
        print("Cadena invalida")






