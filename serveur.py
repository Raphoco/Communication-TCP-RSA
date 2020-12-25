#!/usr/bin/python3

import socket

server_address = "localhost"
server_port = 8790
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

my_socket.bind((server_address, server_port))
my_socket.listen(socket.SOMAXCONN)
(new_connection, tsap_from) = my_socket.accept()
print("New Connection !\n")
print("Address , Port : ", tsap_from)

finalStr = ""
while 1 :
	ligne = new_connection.recv(4)
	if not ligne:
		break

	# REVERSING RSA STUFF HERE
	#
	# # # # # # 

	# On recompose le message
	finalStr += ligne.decode("utf-8")

	if "hello" in finalStr.lower():
		new_connection.sendall("Server : Hello !".encode("utf-8")) # new_connection est le client !

# On envoie le message à la fin de la reconstruction
print("Content : " + finalStr) # FIXME: Pourquoi il n'est pas toujours print ?
new_connection.close()