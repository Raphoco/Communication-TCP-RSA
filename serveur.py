#!/usr/bin/python3

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
	ligne = new_connection.recv(1000)
	if not ligne:
		break
	key_client = ligne.decode("utf-8").split("|")[0]
	#print(key_client)
	#print(ligne.decode("utf-8").split("|")[1])
	tempHex = bytes(ligne.decode("utf-8").split("|")[1], "utf-8").hex()
	#print(tempHex)
	intCipher = int(tempHex, 16)
	#print(intCipher)
	cipher = function.chiffrementRSA(intCipher, 65337, int(key_client))
	print("Chiffré : " + str(cipher))
	# print("Chiffré : " + str(bytes(str(cipher), "utf-8")))

	new_connection.sendall(bytes(str(cipher), "utf-8"))

new_connection.close()
