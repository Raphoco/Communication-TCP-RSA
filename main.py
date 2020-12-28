#!/usr/bin/python3

from premier import * # ou * pour tout import

taille = int(input("Indiquer la taille du nombre n souhaité. \n")) #Bros n'aime pas les input
p = creation_nombre_taille(taille)
q = creation_nombre_taille(taille)
p=premier(p)
print("p est " + str(p))
q=premier(q)
print("q est " + str(q))
"""n=int(p)*int(q)
print(n)"""
"""mes = "test de message probablement envoyé sur le réseau"
print(splitBySize(mes, 5))"""