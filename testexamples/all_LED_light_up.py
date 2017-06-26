import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

import blinkt16 as blinkt

while True:
	blinkt.set_all(255, 255, 255, 0.1)
	blinkt.show()
