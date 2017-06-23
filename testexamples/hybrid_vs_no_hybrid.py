import sys
sys.path.append("/home/pi/Git/homeDashboard")
from LEDcontrol import led_control
import time

while True:
	led_control(0, 1, 100, False, 100)
	time.sleep(1)
	led_control(0, 1, 100, True, 0)
	time.sleep(1)
	led_control(0, 1, 88, False)
	time.sleep(1)