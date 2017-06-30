import socket

#Standard Project CARS specifications
host = '' #Symbolic value (will figure it out by itself)
port = 5606
exp_length = 1367 #Expected amount of bytes per package

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Setting up object with UDP protocol
s.bind((host, port))

def setup_client(newHost, newPort, newExpectedLength):
	global s	
	global host
	global port 
	global exp_length 

	host  = newHost
	port = newPort
	exp_length = newExpectedLength

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	
	s.bind((host, port))


def get_udp_data():
	'''
	Getting data on the network.
	Currently no time-out, 
		so it waits here until something is recieved
	'''
	return s.recv(exp_length) 