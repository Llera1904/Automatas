import random
import time
import DibujoProtocolo

def paridadCadena(cadena):
    cadenaAceptada = False
    state = 0

    for caracter in cadena:
        if state == 0:
            if caracter == '0':
                state = 2
            elif caracter == '1':
                state = 1

        elif state == 1:
            if caracter == '0':
                state = 3
            elif caracter == '1':
                state = 0

        elif state == 2:
            if caracter == '0':
                state = 0
            elif caracter == '1':
                state = 3

        elif state == 3:
            if caracter == '0':
                state = 1
            elif caracter == '1':
                state = 2

    if state == 0:
        cadenaAceptada = True # Cadena con paridad

    return cadenaAceptada

def cadenaBinaria():
    cadena = ""
    entero = random.randint(0, 2**10)
    cadena = "{0:010b}".format(entero)
    
    return cadena 

def creaData(tamaño, data):  
    for i in range(tamaño):
        data.write(cadenaBinaria() + "\n")

# def cadenaBinaria(tamaño):
#     cadena = ""

#     for i in range(0, tamaño):
#         numero = random.randint(0, 1)
#         cadena += str(numero)

#     return cadena 

i = 0
amountPares = 0
ampuntImpares = 0
state = random.randint(0, 1) # Protocolo encendido o apagado 

with open("cadenasPares.txt", "w") as dataPares:
    with open("cadenasImpares.txt", "w") as dataImpares:
        dataPares.write("")
        dataImpares.write("")
        while state != 0:
            i += 1

            # Hacemos la peticion 
            with open("data.txt", "w") as data: # Crea el data de tamaño n
                creaData(10, data)

            dataPares.write("\n\nPeticion: " + str(i) + "\n")
            dataImpares.write("\n\nPeticion: " + str(i) + "\n")

            time.sleep(1) # Esperamos 1 segundo 

            # Leemos las cadenas y las separamos
            with open('data.txt', encoding="utf8") as dataIn:
                for cadena in dataIn:
                    if paridadCadena(cadena) == True:
                        amountPares += 1
                        dataPares.write(cadena) 
                    else:
                        ampuntImpares += 1
                        dataImpares.write(cadena)         

            state = random.randint(0, 1) # Protocolo encendido o apagado

print("Fuera: " + str(state) + "\n")
print("Peticiones totales: " + str(i))
print("Cadenas aceptadas: " + str(amountPares))
print("Cadenas no aceptadas: " + str(ampuntImpares))
print("Total cadenas:" + str(amountPares + ampuntImpares))    

print("\n¿Quieres graficar automata?")
print("Si", end="/")
print("No")
op = input("")

while 1:
    if op == "No":
        break
    elif op != "Si" and op != "No":
        print("Opcion Invalida")
    elif op == "Si":
        DibujoProtocolo.dibujoProtocolo()
        break


