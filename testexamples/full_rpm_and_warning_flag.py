import sys
sys.path.append("..")

import LEDcontrol.py

while True:
	LEDcontrol.led_control(0, 1, 100, False, 100)