import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import game
import dataParser
import udp_client as UDP
import LEDcontrol as LED

PCARS = game.GameUDP('', 5606, 1367)

def setup_game_mode(currGame):
	UDP.setup_client(currGame.host, currGame.port, currGame.exp_length)



#Main loop
gameModeIsSetup = False
telemetry = game.GameData()

while True:

	#Decide on which game
	if gameModeIsSetup != True:
		setup_game_mode(PCARS) #Should be setup later to take multiple games
		gameModeIsSetup = True

	data = UDP.get_udp_data()
	dataParser.PCars_parser(data, telemetry)

	lowfuel = (telemetry.fuel < 10) #Should be changed later

	#print (telemetry.gear, telemetry.RPM, telemetry.headlightsActive, telemetry.flag)
	if(telemetry.brake > 0):
		print(telemetry.brake, telemetry.FL_tire_rps, telemetry.FL_locking_state(), telemetry.RPM_pct())
	LED.led_control(telemetry)
