import sys
sys.path.append("/home/pi/Git/homeDashboard/modules/")

import LEDcontrol

while True:
	LEDcontrol.led_control(1, 1, 100, False, 100)
