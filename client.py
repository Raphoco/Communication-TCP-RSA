#!/usr/bin/python3

import socket
import sys
from premier import cleClient, dechiffrementRSA

server_address = socket.gethostbyname("localhost") # IP machine host
server_port = 8790 # Numéro de port demandé

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

my_socket.connect((server_address,server_port))
[n_c, d_c] = cleClient()

nom_client=input("Entrez votre nom s'il vous plaît. \n")
if(nom_client == "Oscar"):
	print("Oscar est supposé écouter le canal, pas participer à la conversation... \n")
	sys.exit(1)

while 1 :
	toSend = ""
	string_to_be_sent = input("Waiting for you... Type 'Exit' to leave.\n")
	#string_to_be_sent = input(nom_serveur + " attend votre message. Entrez 'Exit' pour quitter.\n")
	if not string_to_be_sent:
		break
	if(string_to_be_sent == "Exit"):
		break
	toSend += str(n_c) + "|"
	toSend += string_to_be_sent
	print(toSend)
	my_socket.sendall(bytes(toSend, "utf-8"))

	# Reception du serveur
	dataRcv = my_socket.recv(1024)
	temp = dataRcv.decode("utf-8")
	print("Reçu : " + temp)
	if dataRcv :
		lst = temp.split("|")
		plaintext = dechiffrementRSA(lst, n_c, d_c)
		reponse = "reponse"
		#while(reponse[0] != "O" or reponse[0] != "o" or reponse[0] != "N" or reponse[0] != "n" ):
		if(reponse[0] != "O"):
			reponse = input("Voulez-vous voir le message déchiffré ? Répondre par Oui ou Non. \n")

		if (reponse[0] == "O" or reponse[0] == "o"):
			print("Après déchiffrement : " + str(plaintext))

#Pour les smileys, il faut avoir installé fonts-emojione depuis son terminal, par la commande sudo apt install fonts-emojione par exemple