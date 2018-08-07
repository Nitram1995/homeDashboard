import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")
#sys.path.append("C:\Git\homeDashboard\modules")

import game
import dataParser
import udp_client as UDP
import LEDcontrol as LED
import button_control as buttons
import GUI
#import testGUI as GUI
import socket
import time
#import _thread as thread
import thread

class App:
	exiting = False

	def setup_game_mode(self, currGame):
		UDP.setup_client(currGame.host, currGame.port, currGame.exp_length)


	def get_and_handle_data(self, args):
		telemetry = args
		while True:
			try:
				data = UDP.get_udp_data()
			except socket.timeout:
				pass #print ("UDP client timed out")
			else:
				dataParser.PCars2_protocol1_parser(data, telemetry)

			#LED.led_control(telemetry)

			#print (telemetry.gear, telemetry.RPM, telemetry.headlightsActive, telemetry.flag)
			#if(telemetry.brake > 0):
				#print(telemetry.brake, telemetry.FL_tire_rps, telemetry.FL_locking_state(), telemetry.RPM_pct())
			#print(telemetry.hybrid_pct, telemetry.gear)
			#time.sleep(0.020)


	def update_gui(self, GUI):
		if(self.exiting == False):
			GUI.update_variables(telemetry)
			GUI.root.after(50, self.update_gui, GUI)

	def exit_app(self):
		print "Exiting via 'exit_app'"
		self.exiting = True
		time.sleep(1) #Look away kids.. This is NOT how its done properly
		sys.exit()

app = App()

PCARS = game.GameUDP('', 5606, 1367)
telemetry = game.GameData()
app.setup_game_mode(PCARS) #Should be setup later to take multiple games

buttons.buttons_init(app)
buttons.button_interupt_init(buttons.BTN_BLK, buttons.btn_blk_changed)
buttons.button_interupt_init(buttons.BTN_WHT, buttons.btn_wht_changed)

thread.start_new_thread(app.get_and_handle_data, (telemetry,))
thread.start_new_thread(LED.init_and_run, (app, telemetry))

GUI.root_setup(GUI.root)
GUI.frame = GUI.screenPCars(GUI.root)
GUI.root.after(1000, app.update_gui, GUI)
GUI.root.mainloop()
