#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#port = 12345                # Reserve a port for your service.
s.connect(('127.0.0.1', 1000))


print (s.recv(1024))
s.send(bytes("Thanks from client", "utf-8"))
s.close()                    # Close the socket when done
