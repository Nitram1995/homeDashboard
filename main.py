import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import game
import udp_client as UDP

PCARS = game.GameUDP('', 5606, 1367)

def setup_game_mode(currGame):
	UDP.setup_client(currGame.host, currGame.port, currGame.exp_length)



#Main loop
isItSetupYet = False
while True:

	#Decide on which game
	if isItSetupYet != True:
		setup_game_mode(PCARS)
		isItSetupYet = True

	data = UDP.get_udp_data()
    	print (ord(data[125]) << 8) + ord(data[124]) #Prints current rpm to terminal
