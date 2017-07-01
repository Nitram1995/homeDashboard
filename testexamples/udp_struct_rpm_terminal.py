import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import udp_client as udp
import struct


#Sets up client for Project Cars specs
udp.setup_client('', 5606, 1367)

while True:
	data = udp.get_udp_data()
	'''
	gear = struct.unpack("<b", data[128])[0] & 0xf0 >> 4
	rpm = struct.unpack("<H", data[124] + data[125])
	'''
	speed, rpm, maxRpm = struct.unpack("<fHH", data[120:128])

	print speed, rpm, maxRpm
        

