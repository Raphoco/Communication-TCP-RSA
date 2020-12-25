#!/usr/bin/python3

import socket

server_address = "localhost" # IP machine host
server_port = 8790 # Numéro de port demandé

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

my_socket.connect((server_address,server_port))
#dataRcv  = ""

while 1 :
	string_to_be_sent = input("Waiting for you... Type 'Exit' to leave.\n")
	if not string_to_be_sent:
		break
	if(bytes(string_to_be_sent, "utf-8").decode("utf-8") == "Exit"):
		break
	my_socket.sendall(bytes(string_to_be_sent, "utf-8"))
	#FIXME: Les données sont bien récoltées côté serveur mais après une "réception" l'input n'est pas pris en compte.
	#dataRcv = my_socket.recv(1024).decode("utf-8")
	#if dataRcv :
	#	print(dataRcv)
print("Good bye !")
my_socket.close()
