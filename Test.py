import numpy as np
import linecache
import re
import math

# def RemoveState(adjacencyTree, i, j):
#     list = []
#     listAux = adjacencyTree[i].copy()

#     list.append(listAux[0].copy())
#     list.append(listAux[1].copy())

#     list[j].pop(0)
 
#     adjacencyTree[i] = list.copy()

# def valorMasProximo(listTest, x):
#     diferencias = []

#     for valor in listTest:
#         diferencias.append(abs(valor - x))

#     print(diferencias)
#     indiceMinimo = diferencias.index(min(diferencias))

#     return listTest[indiceMinimo]


# listTest = [2, 3, 5]
# print(listTest)

# amountNode = listTest[-1] - 1
# listTest[-1] = amountNode
# print(listTest)

# listTest.pop()
# print(listTest)

# listTest = [2, 3, 5, 8, 9, 10, 10, 14, 16]
# valorMasCercano = valorMasProximo(listTest, 11)
# print(listTest)
# print(valorMasCercano)

# newList = []
# listTest = np.array(listTest, int)
# x = np.array([0, 1, 2, 3], int)
# listTest = listTest[x]
# print(listTest)

# print("\n")
# print(linecache.getline("jugadasGanadorasJugador1.txt", 2))

# patron = re.compile("\d+")
# lista = patron.findall(linecache.getline("jugadasGanadorasJugador1.txt", 2))
# print(lista)
# listaEntera = []
# for i in lista:
#     listaEntera.append(int(i))
# print(listaEntera)

pointsX = [1, 2, 3, 4, 5]
# pointsY = [6, 7, 8, 9, 10]

# result = (x + y for x, y in zip(pointsX, pointsY))
# print(*result)
# sum = math.fsum(result)
# print(sum)

print(pointsX[:3])




