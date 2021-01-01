#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import premier as function

#from main import *

server_address = socket.gethostbyname("localhost")
server_port = 8790
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

my_socket.bind((server_address, server_port))
my_socket.listen(socket.SOMAXCONN)
(new_connection, tsap_from) = my_socket.accept()
print("New Connection !\n")
print("Address , Port : ", tsap_from)

[n_s, d_s] = function.cleServeur()

while 1 :
	ligne = new_connection.recv(1024)
	if not ligne:
		break
	key_client = ligne.decode("utf-8").split("|")[0]
	msg = ligne.decode("utf-8").split("|")[1]
	lst = [str(ord(k)) for k in msg]
	cipher = ""
	for element in lst:
		cipher += str(function.chiffrementRSA(int(element), 65337, int(key_client)))
		if lst[-1] != element:
			cipher += "|"

	#cipher = function.chiffrementRSA(intCipher, 65337, int(key_client))
	#print("Chiffré : " + str(cipher))
	print("Chiffré : " + cipher)
	
	new_connection.sendall(bytes(cipher, "utf-8"))

new_connection.close()
