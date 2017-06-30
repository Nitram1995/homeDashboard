import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import udp_client as udp
import LEDcontrol

#Sets up client for Project Cars specs
udp.setup_client('', 5606, 1367)

while True:
        data = udp.get_udp_data()
        maxRPM = (ord(data[127]) << 8) + ord(data[126])
        rpm = (ord(data[125]) << 8) + ord(data[124])

        print rpm, maxRPM
        
	if maxRPM != 0:
		rpmPCT = (rpm * 100) / maxRPM

        LEDcontrol.led_control(0, 0, rpmPCT, 0, 0, 0)
