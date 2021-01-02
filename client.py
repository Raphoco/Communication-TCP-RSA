#!/usr/bin/python3

import socket
import sys
import premier as function
#from serveur import *

server_address = socket.gethostbyname("localhost") # IP machine host
server_port = 8790 # Numéro de port demandé

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

my_socket.connect((server_address,server_port))
[n_c, d_c] = function.cleClient()

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
		chaine = ""
		lst = temp.split("|")
		print("lst : "+str(lst))
		decipher = ""
		for element in lst:
			decipher += str(function.dechiffrementRSA(int(element), int(d_c), int(n_c))) + "|"
		last_char_index = decipher.rfind("|")
		new_string = decipher[:last_char_index] + decipher[last_char_index+1:]
		new_string = new_string.split("|")
		decipher = []
		for i in range(0,len(new_string)):
			for j in range(0, len(new_string[i]), 6):
				decipher.append(new_string[i][j] + new_string[i][j+1] + new_string[i][j+2] + new_string[i][j+3] + new_string[i][j+4] + new_string[i][j+5])
		for i in range(0,len(decipher)):
			#temp = new_string[i]
			for j in range(0,len(decipher[i])):
				while(decipher[i][j] == "4"):
					decipher[i] = decipher[i][1:]
				else:
					break
		print(decipher)
		"""temp=[]
		for i in range(0,len(new_string),6):
			temp.append(new_string[i] + new_string[i+1] + new_string[i+2] + new_string[i+3] + new_string[i+4] + new_string[i+5])
		print(temp)"""
		lstDecipher = [chr(int(k)) for k in decipher]
		if(lstDecipher[-1] == "Z"):
			lstDecipher = lstDecipher[:-1]
		if(lstDecipher[-1] == "Z"):
			lstDecipher = lstDecipher[:-1]
		final = ''.join(lstDecipher)
		print("Après déchiffrement : " + str(final))

#Pour les smileys, il faut avoir installé fonts-emojione depuis son terminal, par la commande sudo apt install fonts-emojione par exemple