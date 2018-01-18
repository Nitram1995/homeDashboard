import sys
#sys.path.append("/home/pi/Git/homeDashboard/modules")
sys.path.append("C:\Git\homeDashboard\modules")

import game
import dataParser
import udp_client as UDP
#import LEDcontrol as LED
import GUI
import socket

PCARS = game.GameUDP('', 5606, 1367)

def setup_game_mode(currGame):
	UDP.setup_client(currGame.host, currGame.port, currGame.exp_length)



#Main loop
gameModeIsSetup = False
telemetry = game.GameData()
setup_game_mode(PCARS) #Should be setup later to take multiple games


def get_and_handle_data():
	#LED.led_control(telemetry)
	GUI.update_variables(telemetry)
	
	try:
		data = UDP.get_udp_data()
		dataParser.PCars2_protocol1_parser(data, telemetry)
	except socket.timeout:
		print ("UDP client timed out\n")


	#print (telemetry.gear, telemetry.RPM, telemetry.headlightsActive, telemetry.flag)
	#if(telemetry.brake > 0):
		#print(telemetry.brake, telemetry.FL_tire_rps, telemetry.FL_locking_state(), telemetry.RPM_pct())
	GUI.root.after(1, get_and_handle_data)

GUI.root_setup(GUI.root)
GUI.frame = GUI.screenPCars(GUI.root)
GUI.root.after(1000, get_and_handle_data)
GUI.root.mainloop()