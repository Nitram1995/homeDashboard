import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import game
import struct

def PCars_parser(data, gData):
	'''See: 'https://docs.python.org/2/library/struct.html' for info on the struct usage'''

	'''
	gData.fuel = struct.unpack("<f", data[116:120])
	gData.RPM = struct.unpack("<H", data[124] + data[125])
	gData.maxRPM = struct.unpack("<H", data[126] + data[127])
	gData.speed = struct.unpack("<f", data[120])
	'''
	gData.fuel, msSpeed, gData.RPM, gData.maxRPM = struct.unpack("<ffHH", data[116:128]) #Equvilent to the  lines above
	gData.lowfuel = (gData.fuel < 10) #Should be changed later


	gData.oilTemp = struct.unpack("<h", data[100:102])
	gData.waterTemp = struct.unpack("<h", data[104:106])
	
	flagInt = struct.unpack("<B", data[98])[0]
	if flagInt == 1:
		gData.flag = 'green'
	elif flagInt == 2:
		gData.flag = 'blue'
	elif flagInt == 6:
		gData.flag = 'black'
	else:
		gData.flag = 'none'

	gearInt = (struct.unpack("<b", data[128])[0] & 0x0f) #For highest bits are current gear
	if(gearInt == 15):
		gData.gear = 'R'
	elif(gearInt == 0):
		gData.gear = 'N'
	else:
		gData.gear = str(gearInt) #Packs the byte (int) as a char

	carFlags = struct.unpack("<B", data[110])[0]
	gData.headlightsActive = 		carFlags & 0x01
	gData.engineWarningActive = 	carFlags & 0x04
	gData.pitLimiterActive = 		carFlags & 0x08
	gData.absOn = 					carFlags & 0x10
	gData.handbrakeActive = 		carFlags & 0x20
	gData.stabilityControlOn = 		carFlags & 0x40
	gData.tractionControlOn = 		carFlags & 0x80

	gData.FL_tire_rps, gData.FR_tire_rps, gData.RL_tire_rps, gData.RR_tire_rps = -struct.unpack("<ffff", data[244:260])
	#gData.FR_tire_rps = -(struct.unpack("<f", data[248:252])[0])
	#gData.RL_tire_rps = -(struct.unpack("<f", data[252:256])[0])
	#gData.RR_tire_rps = -(struct.unpack("<f", data[256:260])[0])
	#gData.FL_tire_grip = struct.unpack("<B", data[280])[0]
	#gData.FL_tire_slip = struct.unpack("<f", data[260:264])
	gData.brake = struct.unpack("<B", data[7])[0]
	gData.FL_tire_temp, gData.FR_tire_temp, gData.RL_tire_temp, gData.RR_tire_temp = struct.unpack('<HHHH', data[344:352])
	gData.aero_damage, gData.engine_damage = struct.unpack('<BB', data[456:458])
