class GameUDP:
	def __init__(self, host, port, expectedDataLength):
		self.host = host
		self.port = port
		self.exp_length = expectedDataLength

class GameData:
	
	RPM = -1
	maxRPM = -1
	speed = -1
	gear = -1
	hybrid_pct = -1
	flag = -1
	
	
