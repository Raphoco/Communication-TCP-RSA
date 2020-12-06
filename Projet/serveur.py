#!/usr/bin/python3

import socket

my_ip = socket.gethostbyname("localhost")
my_server_port = 8790
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

my_socket.bind(("", my_server_port))
my_socket.listen(socket.SOMAXCONN)

while 1:
	(new_connection, tsap_from) = my_socket.accept()
	print("New Connection !\n")
	print("Address , Port : ", tsap_from)
	while 1:
		ligne = new_connection.recv(10000) # Changer le nombre d'octets, voir si on récupère octet par octet, ou plus, sachant que certains caractères sont codés sur plus d'un octet
		if not ligne:
			break
		if "hello" in ligne.decode("utf-8").lower(): #TODO: faire l'interception du message côté client
			new_connection.sendall(bytes("Hello from the Server !", "utf-8")) # new_connection est le client !
		print("Content : " + ligne.decode("utf-8"))
	new_connection.close()
	print("Connection Closed !")

my_socket.close()