class GameUDP:
	def __init__(host, port, expectedDataLength):
		self.host = host
		self.port = port
		self.exp_length = expectedDataLength