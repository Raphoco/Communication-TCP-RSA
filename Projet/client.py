#!/usr/bin/python3

import socket

server_address = "127.0.0.1" # IP machine host
server_port = 8790 # Numéro de port demandé

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,socket.IPPROTO_TCP)

my_socket.connect((server_address,server_port))

while 1:
	string_to_be_sent = input("Waiting for you... ")
	if not string_to_be_sent:
		break
	if(bytes(string_to_be_sent, "utf-8").decode("utf-8") == "Exit"):
		break
	my_socket.sendall(bytes(string_to_be_sent, "utf-8"))

my_socket.close()