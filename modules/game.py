class GameUDP:
	def __init__(self, host, port, expectedDataLength):
		self.host = host
		self.port = port
		self.exp_length = expectedDataLength

class GameData:
	#Car state
	RPM = -1
	maxRPM = -1
	speed = -1
	gear = 'Z'
	hybrid_pct = -1
	oilTemp = -1
	waterTemp = -1
	fuel = -1

	flag = -1

	#Car settings
	headlightsActive = False
	engineWarningActive = False
	pitLimiterActive = False
	absOn = False
	handbrakeActive = False
	stabilityControlOn = False
	tractionControlOn = False

	
	def RPM_pct(self):
		if self.maxRPM != 0:
			return (self.RPM * 100) / self.maxRPM
		else:
			return 0
