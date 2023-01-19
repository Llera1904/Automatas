from operator import contains
import random
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import string
import re
import os
from grafoBuscador import * 

def evaluateSring(cadena, state):
    contPosicion=0
    listPositions=[]
    fullStates = ""
    fullCharacters = ""
    contadorGripa=0
    contadorContagio=0
    contadorDistancia=0
    contadorCalentura=0
    contadorCovid=0
    contadorCansancio=0
    contadorCubrebocas=0
    contadorDolor=0
    lastState = ""
    with open("estadosBuscador.txt", "w") as txt:
        for caracter in cadena:
            contPosicion += 1
            if state == 'A':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'r':
                    state = 'A'
                elif caracter == 'a':
                    state = 'A'
                    # print(caracteresTotales[-1])
                    if len(listPositions)>7 and fullCharacters[-1] == "i" and fullCharacters[-2] == "c" and fullCharacters[-3] == "n" and fullCharacters[-4] == "a" and fullCharacters[-5] == "t" and fullCharacters[-6] == "s" and fullCharacters[-7] == "i" and fullCharacters[-8] == "d":
                        contadorDistancia += 1
                        listPositions.append((contPosicion-len("distancia"),"distancia"))
                elif caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 's':
                    state = 'A'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
            elif state == 'B':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'r':
                    state = 'E'
                elif caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
            elif state == 'C':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D' 
                elif caracter == 'a':
                    state = 'F'
                elif caracter == 'o':
                    state = 'G'
                elif caracter == 'u':
                    state = 'A'  
            elif state == 'D':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D' 
                elif caracter == 'r' or caracter == 'p'  or caracter == 'a' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'i':
                    state = 'A'
                elif caracter == 'o':
                    state = 'J'
            elif state == 'E':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'i':
                    state = 'K'
                elif caracter == 'r':
                    state = 'E'
            elif state == 'F':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 't' or caracter == 'e' or caracter == 'u' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 's':
                    state = 'A'
                    if len(listPositions)>8 and fullCharacters[-1] == "a" and fullCharacters[-2] == "c" and fullCharacters[-3] == "o" and fullCharacters[-4] == "b" and fullCharacters[-5] == "e" and fullCharacters[-6] == "r" and fullCharacters[-7] == "b" and fullCharacters[-8] == "u" and fullCharacters[-9] == "c":
                        contadorCubrebocas += 1
                        listPositions.append((contPosicion-len("cubrebocas"),"cubrebocas"))
                elif caracter == 'n':
                    state = 'L'
                elif caracter == 'l':
                    state = 'M'
            elif state == 'G':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'b':
                    state = 'A'
                elif caracter == 'n':
                    state = 'N'
                elif caracter == 'v':
                    state = 'Ñ'
            elif state == 'H':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v':
                    state = 'A'
                elif caracter == 'b':
                    state = 'O'
            elif state == 'I':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 's':
                    state = 'P'
            elif state == 'J':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'l':
                    state = 'Q'
            elif state == 'K':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'p':
                    state = 'R'
            elif state == 'L':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 's':
                    state = 'S'
            elif state == 'M':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'e':
                    state = 'T'
            elif state == 'N':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 't':
                    state = 'U'
            elif state == 'Ñ':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'i':
                    state = 'V'
            elif state == 'O':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'r':
                    state = 'X'
            elif state == 'P':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 't':
                    state = 'Y'
            elif state == 'Q':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'o':
                    state = 'Y'
            elif state == 'R':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'Z'
                    contadorGripa+=1
                    listPositions.append((contPosicion-len("gripa"),"gripa"))
            elif state == 'S':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'A1'
            elif state == 'T':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i'  or caracter == 'a' or caracter == 'p' or caracter == 'o' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'n':
                    state = 'B1'
            elif state == 'U':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'C1'
            elif state == 'V':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D1'
                    contadorCovid +=1
                    listPositions.append((contPosicion-len("covid"),"covid"))
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l'or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'W':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'e':
                    state = 'E1'
            elif state == 'X':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'F1'
            elif state == 'Y':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'a' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'r':
                    state = 'G1'
                    contadorDolor += 1
                    listPositions.append((contPosicion-len("dolor"),"dolor"))
            elif state == 'Z':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'A1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'n':
                    state = 'H1'
            elif state == 'B1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 't':
                    state = 'I1'
            elif state == 'C1':
                if caracter == 'g':
                    state = 'J1'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'D1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'e'  or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'l':
                    state = 'K1'
            elif state == 'E1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p'or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e'  or caracter == 'u' or caracter == 'v':
                    state = 'A'
                elif caracter == 'b':
                    state = 'L1'
            elif state == 'F1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e'  or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'n':
                    state = 'M1'
            elif state == 'G1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e'  or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'H1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'N1'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e'  or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'I1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'u':
                    state = 'Ñ1'
            elif state == 'J1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'r':
                    state = 'E'
                elif caracter == 'i':
                    state = 'O1'
            elif state == 'K1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 's':
                    state = 'P'
            elif state == 'L1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'n':
                    state = 'P1'
            elif state == 'M1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'Q1'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'N1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'p' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'i':
                    state = 'R1'
                elif caracter == 'a':
                    state = 'F'
                elif caracter == 'o':
                    state = 'G'
                elif caracter == 'u':
                    state = 'H'
            elif state == 'Ñ1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'r':
                    state = 'S1'
            elif state == 'O1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'o':
                    state = 'T1'
                    contadorContagio+=1
                    listPositions.append((contPosicion-len("contagio"),"contagio"))
            elif state == 'P1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'U1'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'Q1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'p' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e'  or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'i':
                    state = 'V1'
                elif caracter == 'a':
                    state = 'F'
                elif caracter == 'o':
                    state = 'G'
                elif caracter == 'u':
                    state = 'H'
            elif state == 'R1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'o':
                    state = 'W1'
                    contadorCansancio += 1
                    listPositions.append((contPosicion-len("cansancio"),"cansancio"))
            elif state == 'S1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'X1'
                    contadorCalentura += 1
                    listPositions.append((contPosicion-len("calentura"),"calentura"))
            elif state == 'T1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'U1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'Y1'
                elif caracter == 'o':
                    state = 'G'
                elif caracter == 'u':
                    state = 'H' 
            elif state == 'V1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'a':
                    state = 'Z1'
            elif state == 'W1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'X1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'Y1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 't' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                elif caracter == 'n':
                    state = 'L'
                elif caracter == 's':
                    state = 'A2'
            elif state == 'Z1':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
            elif state == 'A2':
                if caracter == 'g':
                    state = 'B'
                elif caracter == 'c':
                    state = 'C'
                elif caracter == 'd':
                    state = 'D'
                elif caracter == 'r' or caracter == 'i' or caracter == 'p' or caracter == 'a' or caracter == 'o' or caracter == 'n' or caracter == 't' or caracter == 's' or caracter == 'l' or caracter == 'e' or caracter == 'u' or caracter == 'v' or caracter == 'b':
                    state = 'A'
                
            fullStates = fullStates + state
            fullCharacters = fullCharacters + caracter
            # print("Caracter: ",caracter)           
            # print("Estado: ", state) 
            txt.write("Caracter: " + str(caracter) + " ,Estado: " + str(state) + "\n")

    with open("listaPosicionesBuscador.txt", "w") as txt2:
        txt2.write("La fuente de texto ingresada cuenta con: " + str(contPosicion) + " caracteres en total.\n\n")
        contador =0
        for posicion in listPositions:
            txt2.write(str(contador)+": La palabra " + str(posicion[1]) + " fue encontrada en la posicion " + str(posicion[0]) + "\n")
            contador+=1


    print("N veces palabra gripa =",contadorGripa)
    print("N veces palabra contagio =",contadorContagio)
    print("N veces palabra distancia =",contadorDistancia)
    print("N veces palabra calentura =",contadorCalentura)
    print("N veces palabra covid =",contadorCovid)
    print("N veces palabra cansancio =",contadorCansancio)
    print("N veces palabra cubrebocas =",contadorCubrebocas)
    print("N veces palabra dolor =",contadorDolor)
    print("Caracteres en total:",contPosicion)
    print("lista posciones:",listPositions)
     
def webscrapper(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url,headers=hdr)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, features="html.parser")

    # quita elementos de estilo y guion
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    #Obtiene el texto
    text = soup.get_text()

    #divide lineas y elimina el espacio inicial y final de cada linea
    lines = (line.strip() for line in text.splitlines())
    #divide los encabezados en una linea cada uno
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    #elimina espacios en blanco
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text = text.translate({ord(c): None for c in string.whitespace})
    text = text.lower()

    return text


print("1. Leer texto de url")
print("2. Leer texto de archivo txt")
print("3. Escribir manualmente texto a evaluar")
print("4. Ver grafo")
op = input("Ingresa opcion: ")

if op != '1' and op != '2' and op != '3' and op != '4':
    print("\nOpcion invalida\n")
elif op == '1':
    url = str(input("Dime la url a evaluar: "))
    # url = "https://www.redaccionmedica.com/recursos-salud/faqs-covid19/cuanto-dura-el-cansancio-que-provoca-el-covid"
    cadenaEntrada = webscrapper(url)
    print("Texto obtenido de la url ingresada: ",cadenaEntrada)
    
    state='A'
    print(evaluateSring(cadenaEntrada, state))

    
elif op == '2':
    print("Por favor inserta tu archivo txt en la ruta actual:" , os.getcwd())  
    ruta = str(input("Dime el nombre del archivo (ejemplo texto.txt): "))
    textFile = open(ruta, 'r')
    cadenaEntrada = str(textFile.read())

    cadenaEntrada = cadenaEntrada.translate({ord(c): None for c in string.whitespace})
    cadenaEntrada = cadenaEntrada.lower()
    print(cadenaEntrada)

    state='A'
    print(evaluateSring(cadenaEntrada, state))

elif op == '3':
    cadenaEntrada = str(input("¿Dime la cadena a evaluar?"))
    state='A'
    print(evaluateSring(cadenaEntrada, state))

elif op == '4':
    view()