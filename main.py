import sys
sys.path.append("/home/pi/Desktop/homeDashboard/modules")
#sys.path.append("/home/martin/Programming/homeDashboard/modules")

import game
import dataParser
import udp_client as UDP
import LEDcontrol as LED
#import button_control as buttons
#import GUI
#import testGUI as GUI
import socket
import time
#import _thread as thread
import thread
import signal

PCARS = game.GameUDP('', 5606, 1367)

def setup_game_mode(currGame):
	UDP.setup_client(currGame.host, currGame.port, currGame.exp_length)


gameModeIsSetup = False
telemetry = game.GameData()
setup_game_mode(PCARS) #Should be setup later to take multiple games


def get_and_handle_data(args):
	telemetry = args
	while True:
		try:
			data = UDP.get_udp_data()
		except socket.timeout:
			print ("UDP client timed out")
		else:
			dataParser.PCars2_protocol1_parser(data, telemetry)

		#print (telemetry.gear, telemetry.RPM, telemetry.headlightsActive, telemetry.flag)
		#if(telemetry.brake > 0):
			#print(telemetry.brake, telemetry.FL_tire_rps, telemetry.FL_locking_state(), telemetry.RPM_pct())
		#print(telemetry.hybrid_pct, telemetry.gear)
		#time.sleep(0.020)


def update_gui():
	GUI.update_variables(telemetry)
	GUI.root.after(50, update_gui)

def exit_app(sig, frame):
	print("Exiting via 'exit_app'")
	LED.exiting = True
	time.sleep(1) #Look away kids.. This is NOT how its done properly
	sys.exit()

#buttons.buttons_init()
#buttons.button_interupt_init(buttons.BTN_BLK, exit_app)

thread.start_new_thread(get_and_handle_data, (telemetry,))
thread.start_new_thread(LED.init_and_run, (telemetry,))

#GUI.root_setup(GUI.root)
#GUI.frame = GUI.screenGeneralMessage(GUI.root, "testy", 123.5, "red", "white") 
#GUI.screenPCars(GUI.root)
#GUI.root.after(1000, update_gui)
#GUI.root.mainloop()

signal.signal(signal.SIGINT, exit_app)

# Sleeping until interrupted
signal.pause()
