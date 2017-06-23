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

slowBlinkOn = True
medBlinkOn = True
fastBlinkOn = True
pulseBlinkOn = True



r = 255
g = 255
b = 255
brightness = 0.1


RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

RPM_CRITICAL = 95

HYBRID_START_POS = 1
HYBRID_END_POS = 5
FUEL_WARNING_POS = 6
FLAG_POS = [0, 15]

def led_control(pit, flag, rpm_pct, lowFuel, hybrid=None):
	global currTime
	global slowBlinkOn
	global medBlinkOn
	global fastBlinkOn
	global pulseBlinkOn
	global lastSlowBlink
	global lastMedBlink
	global lastFastBlink
	global lastPulseBlink


	newTime = time.time()
	blinkt.clear() #Clears LED buffer

	if newTime >= (lastSlowBlink + SLOW_BLINK):
		slowBlinkOn = not slowBlinkOn
		lastSlowBlink = newTime
	if newTime >= (lastMedBlink + MED_BLINK):
		medBlinkOn = not medBlinkOn
		lastMedBlink = newTime
	if newTime >= (lastFastBlink + FAST_BLINK):
		fastBlinkOn = not fastBlinkOn
		lastFastBlink = newTime
	if newTime >= (lastPulseBlink + PULSE_BLINK):
		pulseBlinkOn = not pulseBlinkOn
		lastPulseBlink = newTime


	'''
	The sooner an 'led' method is called the lower priority it has.
	The later ones owerwrite the earlier ones.
	'''

	#Udfyld rpm metode
	rpm_led(rpm_pct)

	#Udfyld hybrid metode
	hybrid_led(hybrid)

	#Udfyld flag metode
	flag_led(flag)

	#Udfyld warnings metode
	car_warning_led(lowFuel)

	#Udfyld pit metode
	pit_lim_led(pit)

	blinkt.show() #Sends signal to LEDs
	
	currTime = newTime

def rpm_led(rpm_pct):
	if(rpm_pct >= (RPM_CRITICAL - 8)):
		blinkt.set_pixel(6, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 6)):
		blinkt.set_pixel(7, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 4)):
		blinkt.set_pixel(8, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 2)):
		blinkt.set_pixel(9, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= RPM_CRITICAL):
		for z in range(10, 15):
			blinkt.set_pixel(z, BLUE[0], BLUE[1], BLUE[2], brightness)


def hybrid_led(hybrid):
	if hybrid == 100:
		x = 5
	elif hybrid == 0:
		x = 0
	else:
		x = int(ceil((hybrid / 20.0)))

	for z in range(HYBRID_START_POS, x + 1):
		blinkt.set_pixel(z, GREEN[0], GREEN[1], GREEN[2], brightness)

	for z in range(x + 1, (HYBRID_END_POS + 1)):
		blinkt.set_pixel(z, 0, 0, 0, 0)



def flag_led(flag):
	if flag == 1:
		if fastBlinkOn:
			for x in FLAG_POS:
				blinkt.set_pixel(x, RED[0], RED[1], RED[2], brightness)
		else:
			for x in FLAG_POS:
				blinkt.set_pixel(x, RED[0], RED[1], RED[2], 0)



def car_warning_led(lowFuel):
	if lowFuel == True:
		blinkt.set_pixel(FUEL_WARNING_POS, RED[0], RED[1], RED[2], brightness)


def pit_lim_led(pitLimiterOn):
	if pitLimiterOn:
		for z in range(blinkt.NUM_PIXELS):
			if (z % 2) == 0:
				if slowBlinkOn:
					blinkt.set_pixel(z, RED[0], RED[1], RED[2], brightness)
				else:
					blinkt.set_pixel(z, 0, 0, 0, 0)
			else:
				if not slowBlinkOn:
					blinkt.set_pixel(z, RED[0], RED[1], RED[2], brightness)
				else:
					blinkt.set_pixel(z, 0, 0, 0, 0)