#!/usr/bin/python3

import random
import subprocess
import re

def creationNombreTaille(n):
	tab_entier = []
	random.seed()
	tab_entier.append(random.choice('1379')) #On ne veut pas de nombre pair, d'où le choix de ces chiffres
	for i in range(1,int(n)-1):
		tab_entier.append(random.choice('0123456789')) #On peut peut-être utiliser random.choices pour ne pas avoir à écrire la boucle mais ici ça marche très bien
	tab_entier.append(random.choice('123456789'))
	tab_entier.reverse() # = tab_entier[::-1]
	nombre1 = ""
	for i in range(len(tab_entier)):
		nombre1 += tab_entier[i]
	return nombre1

def premier(n):
	commande = subprocess.run("openssl prime %d " % int(n), shell=True, stdout=subprocess.PIPE)
	exp_reg = re.compile( r"is not prime")
	resultat=exp_reg.search(str(commande.stdout))
	while(resultat):
		tab = list(str(n)) #On crée un tableau dont les éléments possèdent chacun un caractère de n
		n = ""
		if (tab[1] == '0'): #Si à l'étape précédente on avait n=50421 par exemple, alors le prochain nombre sera 042XX, c'est à dire 42XX et ainsi on n'aura un nombre de la taille souhaitée - 1
			tab[1] = random.choice('123456789') #Cette commande évite ce problème
		for i in range(0,len(tab)-2):
			tab[i] = tab[i+1]
			n += tab[i]
		tab[-2] = random.choice('0123456789')
		n += tab[-2]
		tab[-1] = random.choice('1379') #on ne choisit que des nombres impairs. Les nombres pairs ne pouvant pas être premier
		n += tab[-1]
		commande = subprocess.run("openssl prime %d "% int(n), shell=True, stdout=subprocess.PIPE)
		resultat = exp_reg.search(str(commande.stdout))
	return int(n)

def egcd(a,b):
	x,y,u,v = 0,1,1,0
	while(a != 0):
		q,r = b//a , b%a
		m,n = x-u*q , y-v*q
		b,a,x,y,u,v = a,r,u,v,m,n
	pgcd = b
	return pgcd,x,y

def inverseModulo(a,m):
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

e=65537
#p = premier(creationNombreTaille(3))
#q = premier(creationNombreTaille(3))

def cleServeur():
	#taille_p = input("Entrez la taille souhaitée pour le nombre premier p : ")
	#taille_q = input("Entrez la taille souhaitée pour le nombre premier q : ")
	p_s = premier(creationNombreTaille(15))
	q_s = premier(creationNombreTaille(15))
	d_s = inverseModulo(e, (p_s - 1) * (q_s - 1))
	return [p_s * q_s, d_s]

def cleClient():
	#taille_p = input("Entrez la taille souhaitée pour le nombre premier p : ")
	#taille_q = input("Entrez la taille souhaitée pour le nombre premier q : ")
	p_c = premier(creationNombreTaille(15))
	q_c = premier(creationNombreTaille(15))
	d_c = inverseModulo(e, (p_c - 1) * (q_c - 1))
	return [p_c * q_c, d_c]


