import random
import numpy as np

while 1:
    print("1. Longitud aleatoria")
    print("2. Ingresar longitud")
    op = input("Ingresa opcion: ")

    if op != '1' and op != '2':
        print("\nOpcion invalida\n")
    elif op == '1':
        numberRandom = random.randint(1, 100000)
        n = numberRandom
        print("\nTamaño cadena:", n)
        break
    elif op == '2':
        n = int(input("Ingresa longitud de cadena: "))
        print("\nTamaño cadena:", n)
        break

s = "P"
values = np.array(["e", "0", "1", "0P0", "1P1"]) # Reglas 
print("\nReglas:")
for i in range(len(values)):
    print("(", str(i+1), ")", "->", values[i])
print("\n")

with open("IDs.txt", "w") as txt:
    for x in range(int(n/2)):
        r = random.randint(3, 4)
        s = s.replace("P", values[r])
        # print("(", r+1, ")", s)
        txt.write("(" + str(r+1) + ")" + str(s) + "\n")

    if (n % 2) == 0:
        r = 0
        s = s.replace("P","")
    else:
        r = random.randint(1, 2)
        s = s.replace("P", values[r])
    # print("\n(", r, ")", s)
    print("longitud ultima cadena:", len(s))
    txt.write("(" + str(r+1) + ")" + str(s) + "\n")