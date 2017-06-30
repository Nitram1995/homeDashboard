import socket

#Standard Project CARS specifications
host = ''
port = 5606
exp_length = 1367

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
	return s.recv(exp_length)