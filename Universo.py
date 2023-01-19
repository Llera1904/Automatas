from matplotlib import pyplot as plt
import math
import random

# Cantidad de unos en la cadena 
def amountOne(bin):
    numOne = 0
    for i in range(len(bin)):
        if bin[i] == "1":
            numOne += 1
    return numOne

def setString(setK, txt):
    alphabet = ['0', '1']
    newSetK = []
    combination = []

    for i in range(len(alphabet)):
        for j in range(len(setK)):
            combination = alphabet[i] + setK[j]
            txt.write(combination)          
            newSetK.append(combination) 

    return newSetK

def setStringBin(m, amountStrings, txt, txt2):
    for i in range(2**m): # Numero de cadenas o combincaiones resultantes 
        binAux = format(i, "0" + str(m) + "b") # Numero binario
        amountStrings += 1 # Cantidad de cadenas
        txt.write(binAux + ", ")
        txt2.write(binAux)
        numOne = amountOne(binAux)
        plt.plot(amountStrings, numOne, markersize=4, marker="o", color="green") # Grafica cantidad de unos por cada cadena

    return amountStrings, numOne         

print("Programa que calcula el universo m de ∑= {0, 1}")

while 1:
    print("Ingresa una opcion")
    print("1. Ingresar m")
    print("2. Generar m aleatoria")
    print("3. Salir")
    op = input("")

    if op == '3':
        break
    elif op != '1' and op != '2':
        print("\nOpcion invalida\n")
    else:
        if op == '1':
            m = int(input("Introduce el valor de m en un rango de [0, 1000]: "))
        elif op == '2':
            m = random.randint(0, 1000)
        print("\nValor de m:", m)

        plt.rcParams["figure.figsize"] = [10, 5]
        plt.rcParams["figure.autolayout"] = True

        with open("cadenaUniverso.txt", "w") as txt:
            txt.write('')

        with open("universo.txt", "w") as txt2:
            txt2.write("{e, ")

        with open("universo.txt", "a") as txt:
            with open("cadenaUniverso.txt", "a") as txt2:
                amountStrings = 0 # Calculo de conjuntos o universo m
                for i in range(m):
                    amountStrings, numOne = setStringBin(i + 1, amountStrings, txt, txt2)
                print("Cantidad de cadenas totales:", amountStrings)

        with open("universo.txt", "a") as txt:
            txt.write("...}") 

        plt.title("Cadenas universo")
        plt.xlim(0, amountStrings)
        plt.ylim(0, numOne)
        plt.xlabel("Cadena")
        plt.ylabel("Cantidad de unos")
        plt.grid()

        fig, ax = plt.subplots(1, 2)
        with open("cadenaUniverso.txt", "r") as txt:
            string = ""
            amountStrings = 0
            while 1: 
                char = txt.read(1)           
                if not char:  
                    break  

                string += char
                if len(string) == 64:
                    # print(string)
                    amountStrings += 1
                    numOne = amountOne(string)
                    ax[0].plot(amountStrings, numOne, markersize=4, marker="o", color="orange") # Grafica cantidad de unos por cada cadena
                    ax[1].plot(amountStrings, math.log10(numOne), markersize=4, marker="o", color="purple") 
                    string = ""
            print("Cantidad de cadenas de 64 bits:", amountStrings)

        ax[0].set_title('Grafica cadenas 64 universo')
        ax[0].set(xlim=(0, amountStrings), ylim=(0, numOne))    
        ax[0].set_xlabel("Cadena")
        ax[0].set_ylabel("Cantidad de unos")      
        ax[0].xaxis.grid(True)
        ax[0].yaxis.grid(True)
        ax[1].set_title('Grafica cadenas 64 log10 universo')
        ax[1].set(xlim=(0, amountStrings), ylim=(0, math.log10(numOne)))     
        ax[1].set_xlabel("Cadena")
        ax[1].set_ylabel("Cantidad de unos")     
        ax[1].xaxis.grid(True)
        ax[1].yaxis.grid(True)
        plt.show()

        print("Universo calculado\n\n")



