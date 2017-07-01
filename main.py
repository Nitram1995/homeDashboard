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

    lowfuel = (telemetry.fuel < 100) #Should be changed later

    print telemetry.RPM, telemetry.headlightsActive, telemetry.flag
    LED.led_control(telemetry.pitLimiterActive, telemetry.flag, telemetry.RPM_pct(), lowfuel, 0, 0)