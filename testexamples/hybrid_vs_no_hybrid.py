import sys
sys.path.append("/home/pi/Git/homeDashboard/modules")

from LEDcontrol import led_control
import time

while True:
	led_control(0, 0, 100, False, 100)
	time.sleep(1)
	led_control(0, 0, 100, True, 0)
	time.sleep(1)
	led_control(0, 0, 92, False)
	time.sleep(1)
