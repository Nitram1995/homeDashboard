import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import udp_client as udp

#Sets up client for Project Cars specs
udp.setup_client('', 5606, 1367)

while True:
        data = udp.get_udp_data()
        print (ord(data[125]) << 8) + ord(data[124]) #Prints current rpm to terminal
