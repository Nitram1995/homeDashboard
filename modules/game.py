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
	maxFuel = -1
	avr_fuel = -1
	aero_damage = -1
	engine_damage = -1

	#Wheel state
	FL_tire_rps = -1
	FR_tire_rps = -1
	RL_tire_rps = -1
	RR_tire_rps = -1
	FL_tire_temp = -1
	FR_tire_temp = -1
	RL_tire_temp = -1
	RR_tire_temp = -1
	FL_brake_damage = -1
	FR_brake_damage = -1
	RL_brake_damage = -1
	RR_brake_damage = -1

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

	def curr_fuel(self):
		return self.maxFuel * self.fuel

	def FL_tire_temp_c(self):
		return self.kelvin_to_celsius_int(self.FL_tire_temp)
	def FR_tire_temp_c(self):
		return self.kelvin_to_celsius_int(self.FR_tire_temp)
	def RL_tire_temp_c(self):
		return self.kelvin_to_celsius_int(self.RL_tire_temp)
	def RR_tire_temp_c(self):
		return self.kelvin_to_celsius_int(self.RR_tire_temp)

	def kelvin_to_celsius_int(self, temp):
		return temp - 273

	def fuel_laps_remaining(self):
		return self.fuel / self.avr_fuel

	def lowFuel(self):
		'''
		if(self.fuel_laps_remaining() < 2):
			return True
		else:
			return False
		'''
		print(self.fuel)
		return (self.curr_fuel() < 10)


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

