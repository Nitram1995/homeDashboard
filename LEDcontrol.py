import blinkt16 as blinkt
from math import ceil
import time

currTime = time.time()

SLOW_BLINK = 1.0
MED_BLINK = 0.5
FAST_BLINK = 0.25
PULSE_BLINK = 0.1

lastSlowBlink = currTime
lastMedBlink = currTime
lastFastBlink = currTime
lastPulseBlink = currTime

r = 255
g = 255
b = 255
brightness = 0.05

GREEN = [0, 255, 0]

HYBRID_START_POS = 1
HYBRID_END_POS = 5

def led_control(pit, flag, rpm, lowFuel, hybrid=None):
	newTime = time.time()

	#Udfyld rpm metode

	#Udfyld hybrid metode
	hybrid_led(hybrid)

	#Udfyld flag metode

	#Udfyld warnings metode

	#Udfyld pit metode

	blinkt.show()

def hybrid_led(hybrid):
	if hybrid == 100:
		x = 5
	elif hybrid == 0:
		x = 0
	else:
		x = int(ceil((hybrid / 20.0)))

	print x

	for z in range(HYBRID_START_POS, x + 1):
		blinkt.set_pixel(z, GREEN[0], GREEN[1], GREEN[2], brightness)

	for z in range(x + 1, HYBRID_END_POS + 1):
		blinkt.set_pixel(z, 0, 0, 0, 0)

