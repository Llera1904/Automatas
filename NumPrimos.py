from matplotlib import pyplot as plt
import math
import random

# Cantidad de unos en la cadena 
def amountOne(bin):
    numOne = 0
    for i in range(len(bin)):
        if numberPrimeBin[i] == "1":
            numOne += 1
    return numOne

# Decimal a binario 
def decimalBin(decimal):
    if decimal <= 0:
        return "0"

    binary = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        binary = str(residuo) + binary

        decimal = int(decimal / 2)
    return binary

# Factorial recursivo 
def factorial(x):
    if x == 1:
        return 1

    return x * factorial(x-1)

print("Programa que calcula numeros primos")
while 1:
    print("Ingresa una opcion")
    print("1. Ingresar hasta que numero primo deseas calcular")
    print("2. Generar numero aleatorio")
    print("3. Salir")
    op = input("")

    if op == '3':
        break
    elif op != '1' and op != '2':
        print("\nOpcion invalida\n")
    else:
        if op == '1':
            primeMax = int(input("Numero primo maximo en un intervalo [2, 10^27]: "))
        elif op == '2':
            primeMax = random.randint(2, 10**27)
        print("\nNumero primo maximo:", primeMax)

        primes = 1
        i = 2

        plt.rcParams["figure.figsize"] = [14, 5]
        plt.rcParams["figure.autolayout"] = True
        fig, ax = plt.subplots(1, 3)

        with open("primosBinario.txt", "w") as txt:
            txt.write('{') 

        with open("primosDecimal.txt", "w") as txt:
            txt.write('{') 

        maxOne = 0
        with open("primosBinario.txt", "a") as txt:
            with open("primosDecimal.txt", "a") as txt2:
                # while  primes <= amountPrimes:
                while  1:
                    fact = math.factorial(i - 1)
                    # Teorema John Wilson (p-1)! mod p = p-1, p >= 2
                    if fact % i == i - 1:
                        numberPrime = i
                        if numberPrime >= primeMax:
                            break
                        numberPrimeBin = decimalBin(numberPrime)
                        primes += 1
                        numOne = amountOne(numberPrimeBin)

                        if numOne > maxOne:
                            maxOne = numOne

                        # Graficamos
                        ax[0].plot(primes - 1, numOne, markersize=2, marker="o", color="green")
                        ax[1].plot(primes - 1, math.log10(numOne), markersize=2, marker="o", color="orange")
                        ax[2].plot(primes - 1, math.log2(numOne), markersize=2, marker="o", color="purple")
                        txt.write(numberPrimeBin + ', ') 
                        txt2.write(str(numberPrime) + ', ') 
                    i += 1

        with open("primosBinario.txt", "a") as txt:
                        txt.write('...}')

        with open("primosDecimal.txt", "a") as txt:
                        txt.write('...}')

        ax[0].set_title('Grafica cadenas primos')
        ax[0].set(xlim=(0, primes - 1), ylim=(0, maxOne))    
        ax[0].set_xlabel("Cadena")
        ax[0].set_ylabel("Cantidad de unos")      
        ax[0].xaxis.grid(True)
        ax[0].yaxis.grid(True)
        ax[1].set_title('Grafica cadenas primos log10')
        ax[1].set(xlim=(0, primes - 1), ylim=(0, math.log10(maxOne)))     
        ax[1].set_xlabel("Cadena")
        ax[1].set_ylabel("Cantidad de unos")     
        ax[1].xaxis.grid(True)
        ax[1].yaxis.grid(True)
        ax[2].set_title('Grafica cadenas primos log2')
        ax[2].set(xlim=(0, primes - 1), ylim=(0, math.log2(maxOne)))     
        ax[2].set_xlabel("Cadena")
        ax[2].set_ylabel("Cantidad de unos")     
        ax[2].xaxis.grid(True)
        ax[2].yaxis.grid(True)
        plt.show()

        print("Numeros primos calculados\n")

    

