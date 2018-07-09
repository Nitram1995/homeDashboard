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
	gear = 'E'
	hybrid_pct = -1
	oilTemp = -1
	waterTemp = -1
	fuel = -1

	#Wheel state
	FL_tire_rps = -1
	FR_tire_rps = -1
	RL_tire_rps = -1
	RR_tire_rps = -1
	#FL_tire_grip = -1
	#FL_tire_slip = -1

	#User inputs
	brake = -1

	#Session info
	flag = 'none'

	#Car settings
	headlightsActive = False
	engineWarningActive = False
	pitLimiterActive = False
	absOn = False
	handbrakeActive = False
	stabilityControlOn = False
	tractionControlOn = False


	def RPM_pct(self):
		if(self.maxRPM != 0):
			return (self.RPM * 100) / self.maxRPM
		else:
			return 0

	def lowFuel(self):
		if(self.fuel < 10):
			return True
		else:
			return False

	def FL_locking_state(self):
		return self.front_wheel_lock_state(self.FL_tire_rps)

	def FR_locking_state(self):
		return self.front_wheel_lock_state(self.FR_tire_rps)

	def front_wheel_lock_state(self, front_wheel_rps):
		avr_rear_rps = (self.RL_tire_rps + self.RR_tire_rps) / 2
		if(self.brake <= 0):
			return 0
		elif(avr_rear_rps < 15):
			return 0
		else:
			if(front_wheel_rps < 1):
				return 2
			elif(avr_rear_rps - front_wheel_rps > 20):
				return 1
		return 0

