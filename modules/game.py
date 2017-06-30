class GameUDP:
	def __init__(self, host, port, expectedDataLength):
		self.host = host
		self.port = port
		self.exp_length = expectedDataLength
