#!/usr/bin/python3

import socket
import premier as function

server_address = socket.gethostbyname("localhost") # IP machine host
server_port = 8790 # Numéro de port demandé

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

my_socket.connect((server_address,server_port))
[n_c, d_c] = function.cleClient()
while 1 :
	toSend = ""
	string_to_be_sent = input("Waiting for you... Type 'Exit' to leave.\n")
	if not string_to_be_sent:
		break
	if(bytes(string_to_be_sent, "utf-8").decode("utf-8") == "Exit"):
		break
	toSend += str(n_c) + "|"
	toSend += string_to_be_sent
	print(toSend)
	my_socket.sendall(bytes(toSend, "utf-8"))

	# Reception du serveur
	dataRcv = my_socket.recv(1024)
	#print(dataRcv)
	#hex = dataRcv.hex()
	#print(hex)
	#final = int(hex, 16)
	#print(final)
	temp = dataRcv.decode("utf-8")
	print(temp)

	if dataRcv :
		#FIXME
		decipher = function.dechiffrementRSA(int(temp), int(d_c), int(n_c))
		print("Reçu : " + str(decipher))
		#print(bytes(str(decipher), "utf-8").decode("utf-8"))