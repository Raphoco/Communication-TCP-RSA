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
		decipher = ""
		for element in lst:
			decipher += str(function.dechiffrementRSA(int(element), int(d_c), int(n_c))) + "|"
		last_char_index = decipher.rfind("|")
		new_string = decipher[:last_char_index] + decipher[last_char_index+1:]
		lstDecipher = [chr(int(k)) for k in new_string.split("|")]

		final = ''.join(lstDecipher)
		print("Après déchiffrement : " + str(final))