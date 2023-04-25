#!/bin/python3

#Syntaxe python3 scanner.py <IP>

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of argument.")
	print("Syntax: python3 scanner.py <ip>")

#Banner

print("-" * 50)
print("Scanner done by Tr1h4rd3r for TCM CyberSecurity Certification")
print("Scanning target " + target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try:
	for port in range(20,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open")
		s.close() 
		
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	#python3 scanner.py kkk (does not resolve)
	sys.exit()

except socket.error:
	print("Server not reachable...")
