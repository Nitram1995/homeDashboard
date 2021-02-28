import sys
import argparse
import thread
import signal
import socket
import time
#import button_control as buttons

parser = argparse.ArgumentParser()

led_thread = None
game_trhead =  None

def set_system(system):
	if system == 'pi':
		sys.path.append("/home/pi/Desktop/homeDashboard/modules")
	elif system == 'desktop':
		sys.path.append("/home/martin/Programming/homeDashboard/modules")


def exit_app(sig, frame):
	print("Exiting via 'exit_app'")
	if led_thread: LED.exiting = True
	time.sleep(1)
	sys.exit()


def setup_game_modules():
	global telemetry, dataParser
	import game
	import dataParser
	import udp_client as UDP

	PCARS = game.GameUDP('', 5606, 1367)

	def setup_game_mode(currGame):
		UDP.setup_client(currGame.host, currGame.port, currGame.exp_length)

	telemetry = game.GameData()
	setup_game_mode(PCARS)

	return (telemetry, dataParser, UDP)


def get_and_handle_data(UDP, dataParser, telemetry):
	while True:
		try:
			data = UDP.get_udp_data()
		except socket.timeout:
			print ("UDP client timed out")
		else:
			dataParser.PCars2_protocol1_parser(data, telemetry)


def run_gui():
	def update_gui():
		GUI.update_variables(telemetry)
	
	GUI.root.after(50, update_gui)
	GUI.root_setup(GUI.root)
	GUI.screenPCars(GUI.root)
	GUI.root.after(1000, update_gui)
	GUI.root.mainloop()


if __name__ == '__main__':
	parser.add_argument("--gui", action='store_true', help="Run tkinter GUI feature")
	parser.add_argument("--led", action='store_true', help="Run LED features. Requires GPIO functionality")
	parser.add_argument("-s", "--system", choices=['pi', 'desktop'], default="pi", help="The system that the program is run on")

	args = parser.parse_args()

	set_system(args.system)
	
	telemetry, dataParser, UDP = setup_game_modules()
	game_trhead = thread.start_new_thread(get_and_handle_data, (UDP, dataParser, telemetry))

	if args.led:
		import LEDcontrol as LED
		led_thread = thread.start_new_thread(LED.init_and_run, (telemetry,))

	#buttons.buttons_init()
	#buttons.button_interupt_init(buttons.BTN_BLK, exit_app)

	if args.gui:
		import GUI
		run_gui()
	else:
		# Sleeping until interrupted
		signal.signal(signal.SIGINT, exit_app)
		signal.pause()
