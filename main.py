#!/usr/bin/python3

from premier import * # ou * pour tout import

n = int(input("Indiquer la taille du nombre n souhaité. \n")) 
p = premier(n)
q = premier(n)
print(p)
print(q)

n = p * q
euler = (p-1) * (q-1)
print(n)
print(euler)
mes = "test de message probablement envoyé sur le réseau"
#print(cipher_rsa(mes))
# On envoie ensuite le msg au serveur qui decipher_rsa(msg) paquet par paquet
