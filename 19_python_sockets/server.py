#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
#port = 12345                # Reserve a port for your service.
s.bind(('127.0.0.1', 1000))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(bytes('Thank you for connecting', 'utf-8'))
   print(c.recv(1024))
   c.close()                # Close the connection
