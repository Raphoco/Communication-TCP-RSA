#!/usr/bin/python3

import random
import subprocess
import re
import sys
e=65537


def creation_nombre_taille(n):
	tab_entier = []
	random.seed()
	tab_entier.append(random.choice('1379')) #On ne veut pas de nombre pair, d'où le choix de ces chiffres
	for i in range(1,int(n)-1):
		tab_entier.append(random.choice('0123456789')) #On peut peut-être utiliser random.choices pour ne pas avoir à écrire la boucle mais ici ça marche très bien
	tab_entier.append(random.choice('123456789'))
	tab_entier.reverse()
	nombre1 = ""
	for i in range(len(tab_entier)):
		nombre1 += tab_entier[i]
	return nombre1


def premier(n):
	random.seed()
	impair = random.choice('1379')
	max = random.choice('123456789')
	n_i = impair

	for i in range(1,n-1):
		n_i += random.choice('0123456789')
	
	n_i += max
	print("si on ne retourne pas n_i, le nombre est : "+n_i+" qui est parfois pair")
	n_i = n_i[::-1]#On retourne la liste pour avoir la forme souhaitée
	print("n_i est : "+n_i)

	commande = subprocess.run("openssl prime %d " % int(n_i), shell=True, stdout=subprocess.PIPE)
	exp_reg = re.compile( r"is not prime")
	print(str(commande.stdout))
	resultat=exp_reg.search(str(commande.stdout))
	while(resultat):
		if(n_i[1] == 0):
			n_i[1]=random.choice('123456789') #Si à l'étape précédente on avait n=50421 par exemple, alors le prochain nombre sera 042XX, c'est à dire 42XX et ainsi on n'aura un nombre de la taille souhaitée - 1
		n_i = n_i[1:] + random.choice('1379') #Cette commande évite ce problème
		print(n_i)
		commande = subprocess.run("openssl prime %d "% int(n_i), shell=True, stdout=subprocess.PIPE)
		print(str(commande.stdout))
		resultat = exp_reg.search(str(commande.stdout))
	return int(n_i)

def egcd(a,b):
	x,y,u,v = 0,1,1,0
	while(a != 0):
		q,r = b//a , b%a
		m,n = x-u*q , y-v*q
		b,a,x,y,u,v = a,r,u,v,m,n
	pgcd = b
	return pgcd,x,y

def inverse_modulo(a,m):
	gcd,x,y = egcd(a,m)
	if gcd != 1:
		return None
	return x%m

def powmod(x,y,n): #travailler avec des entiers
	result = 1
	while y > 0:
		if y&1>0:
			result = (result*x)%n
		y >>= 1
		x = (x*x)%n
	return result

def chiffrementRSA(m,e,n): #Fonction inutile
	c = powmod(m,e,n)
	return c

def dechiffrementRSA(c,e,n): #Fonction inutile
	m = powmod(c,e,n)
	return m

def splitParam(str, size): 
	lst = []
	for i in range(0, len(str), size):
		lst.append(str[i : i + size])
	return lst

#n = int(input("Indiquer la taille du nombre n souhaité. \n")) #Bros n'aime pas les input
#n1 = creation_nombre_taille(n)
#premier(n1)



"""Peut-être faire un fichier avec des fonctions pour générer les nombres qu'on veut 
(creation_nombre_taille(n), premier(n), ...).
Ensuite, un fichier avec les fonctions utiles pour RSA, style powmod, etc
Puis les fichiers serveur et client
Ensuite on construit et relie bien tout ça"""
