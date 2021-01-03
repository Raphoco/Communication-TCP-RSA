#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
from premier import cleServeur, chiffrementRSA

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

while 1 :
	string_to_be_sent = input("Ecrire ici : (tapez 'Exit' pour quitter le programme).\n")
	ligne = new_connection.recv(4096)
	if not ligne:
		break
	key_client = ligne.decode("utf-8").split("|")[0]
	new_string = chiffrementRSA(string_to_be_sent, key_client)
	print("Chiffré : " + new_string)
	
	new_connection.sendall(bytes(new_string, "utf-8"))

new_connection.close()
