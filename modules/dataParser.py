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

	gData.oilTemp = struct.unpack("<h", data[100:102])
	gData.waterTemp = struct.unpack("<h", data[104:106])

	gData.flag = struct.unpack("<B", data[98])

	gearInt = (struct.unpack("<b", data[128])[0] >> 4) #For highest bits are current gear
		if(gearInt == 15):
			gData.gear = 'R'
		elif(gearInt == 0):
			gData.gear = 'N'
		else:
			gData.gear = struct.pack("=c", gearInt) #Packs the byte (int) as a char

	carFlags = struct.unpack("<B", data[110])

	gData.headlightsActive = 		carFlags & 0x01
	gData.engineWarningActive = 	carFlags & 0x04
	gData.pitLimiterActive = 		carFlags & 0x08
	gData.absOn = 					carFlags & 0x10
	gData.handbrakeActive = 		carFlags & 0x20
	gData.stabilityControlOn = 		carFlags & 0x40
	gData.tractionControlOn = 		carFlags & 0x80