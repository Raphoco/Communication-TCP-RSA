#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from premier import cleServeur, chiffrementRSA
import math as math

server_address = socket.gethostbyname("localhost")
server_port = 8790
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

my_socket.bind((server_address, server_port))
my_socket.listen(socket.SOMAXCONN)
(new_connection, tsap_from) = my_socket.accept()
print("New Connection !\n")
print("Address , Port : ", tsap_from)

[n_s, d_s] = cleServeur()

"""nom_serveur=input("Entrez votre nom s'il vous plaît. \n")
print("Vous pouvez désormais communiquer avec " + nom_client)"""
while 1 :
	ligne = new_connection.recv(1024)
	if not ligne:
		break
	key_client = ligne.decode("utf-8").split("|")[0]
	msg = ligne.decode("utf-8").split("|")[1]
	
	new_string = chiffrementRSA(msg, key_client)
	print("Chiffré : " + new_string)
	
	new_connection.sendall(bytes(new_string, "utf-8"))

new_connection.close()
