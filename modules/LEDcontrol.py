import blinkt
import RPi.GPIO as GPIO
from math import ceil
import time

exiting = False #This is a discusting implementation, sorry

currTime = time.time()

SLOW_BLINK = 0.6
MED_BLINK = 0.3
FAST_BLINK = 0.15
PULSE_BLINK = 0.05
NOTICE_BLINK_ON_TIME = 0.10
NOTICE_BLINK_OFF_TIME = 1.95

lastSlowBlink = currTime
lastMedBlink = currTime
lastFastBlink = currTime
lastPulseBlink = currTime
lastNoticeBlinkChange = currTime

NoticeBlinkOn = True
slowBlinkOn = True
medBlinkOn = True
fastBlinkOn = True
pulseBlinkOn = True

r = 255
g = 255
b = 255
brightness = 0.07


RED = [255, 0, 0]
YELLOW = [0, 0, 0]
GREEN = [0, 200, 0]
BLUE = [0, 0, 180]
WHITE = [255, 255, 255]
PURPLE = [200, 0, 128]

RPM_CRITICAL = 97

HYBRID_START_POS = 2
HYBRID_END_POS = 5
HYBRID_LED_COUNT = HYBRID_END_POS - HYBRID_START_POS + 1
FUEL_WARNING_POS = [1, 6]
FLAG_POS = [0, 7]

def setup_gpio():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def test_all_leds():
	for x in range(blinkt.NUM_PIXELS):
		blinkt.set_pixel(x, WHITE[0], WHITE[1], WHITE[2], 0.05)
	blinkt.show()

	time.sleep(2)

	blinkt.clear()
	blinkt.show()

def cleanup_leds():
	blinkt.clear()
	blinkt.show()
	GPIO.cleanup()
	print "LED cleanup finished"

def init_and_run(args):
	setup_gpio()
	test_all_leds()
	led_control(args)


def led_control(gameData):
	'''(pit, flag, rpm_pct, lowFuel, 
				flLock, frLock, hybrid=None):'''
	global currTime
	global NoticeBlinkOn
	global slowBlinkOn
	global medBlinkOn
	global fastBlinkOn
	global pulseBlinkOn
	global lastNoticeBlinkChange
	global lastSlowBlink
	global lastMedBlink
	global lastFastBlink
	global lastPulseBlink

	while True:
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
		
		if NoticeBlinkOn and newTime >= lastNoticeBlinkChange + NOTICE_BLINK_ON_TIME:
			NoticeBlinkOn = False
			lastNoticeBlinkChange = newTime
		elif not NoticeBlinkOn and newTime >= lastNoticeBlinkChange + NOTICE_BLINK_OFF_TIME:
			NoticeBlinkOn = True
			lastNoticeBlinkChange = newTime



		'''
		The sooner an 'led' method is called the lower priority it has.
		The later ones owerwrite the earlier ones.
		'''

		if gameData.hybrid_pct != -1:
			hybrid_led(gameData)

		flag_led(gameData)

		car_warning_led(gameData)

		blinkt.show() #Sends signal to LEDs

		currTime = newTime

		if(exiting):
			cleanup_leds()
			return

		time.sleep(0.016)


def rpm_led(data):
	rpm_pct = data.RPM_pct()

	#Green LEDs
	if(rpm_pct >= (RPM_CRITICAL - 18)):
		blinkt.set_pixel(1, GREEN[0], GREEN[1], GREEN[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 16)):
		blinkt.set_pixel(2, GREEN[0], GREEN[1], GREEN[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 14)):
		blinkt.set_pixel(3, GREEN[0], GREEN[1], GREEN[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 12)):
		blinkt.set_pixel(4, GREEN[0], GREEN[1], GREEN[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 10)):
		blinkt.set_pixel(5, GREEN[0], GREEN[1], GREEN[2], brightness)

	#Red LEDs
	if(rpm_pct >= (RPM_CRITICAL - 8)):
		blinkt.set_pixel(6, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 6)):
		blinkt.set_pixel(7, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 4)):
		blinkt.set_pixel(8, RED[0], RED[1], RED[2], brightness)
	if(rpm_pct >= (RPM_CRITICAL - 2)):
		blinkt.set_pixel(9, RED[0], RED[1], RED[2], brightness)

	#Blue LEDs
	if(rpm_pct >= RPM_CRITICAL):
		for z in range(10, 15):
			blinkt.set_pixel(z, BLUE[0], BLUE[1], BLUE[2], brightness)


def hybrid_led(data):
	hybrid = data.hybrid_pct

	if hybrid == 100:
		hybrid_brightness = brightness if NoticeBlinkOn else brightness / 2.0
		for x in range(HYBRID_START_POS, HYBRID_END_POS + 1):
			blinkt.set_pixel(x, GREEN[0], GREEN[1], GREEN[2], hybrid_brightness)
		return

	if hybrid == 0:
		x = 0
	else:
		x = int(ceil(hybrid / (100 / float(HYBRID_LED_COUNT))))

	for z in range(HYBRID_START_POS, HYBRID_START_POS + x):
		blinkt.set_pixel(z, GREEN[0], GREEN[1], GREEN[2], brightness / 2.0)

	for z in range(HYBRID_START_POS + x + 1, (HYBRID_END_POS + 1)):
		blinkt.set_pixel(z, 0, 0, 0, 0)




def flag_led(data):
	flag = data.flag

	if flag != "none":
		
		if flag == "green":
			color = GREEN
		elif flag == "yellow":
			color = YELLOW
		elif flag == "blue":
			color = BLUE
		elif flag == "red":
			color = RED
		else:
			color = WHITE

		if fastBlinkOn:
			for x in FLAG_POS:
				blinkt.set_pixel(x, color[0], color[1], color[2], brightness)
		else:
			for x in FLAG_POS:
				blinkt.set_pixel(x, color[0], color[1], color[2], 0)



def car_warning_led(data):
	lowFuelCritical = data.low_Fuel_Critical()
	lowFuel = data.lowFuel()
	flLock = data.FL_locking_state()
	frLock = data.FR_locking_state()

	#FUEL
	if lowFuelCritical:
		if slowBlinkOn:
			for x in FUEL_WARNING_POS:
				blinkt.set_pixel(x, RED[0], RED[1], RED[2], brightness)
		else:
			for x in FUEL_WARNING_POS:
				blinkt.set_pixel(x, RED[0], RED[1], RED[2], 0)
	elif lowFuel:
		for x in FUEL_WARNING_POS:
			blinkt.set_pixel(x, RED[0], RED[1], RED[2], brightness)

	
	#Tire locking
	''' 
		1 = almost locked
		2 = fully locked
	'''
	
	
	if flLock == 1:
		blinkt.set_pixel(FLAG_POS[0], PURPLE[0], PURPLE[1], PURPLE[2], brightness * 2.5)
	elif flLock == 2:
		if pulseBlinkOn:
			blinkt.set_pixel(FLAG_POS[0], PURPLE[0], PURPLE[1], PURPLE[2], brightness * 2.5)
		else:
			blinkt.set_pixel(FLAG_POS[0], 0, 0, 0, 0)

	if frLock == 1:
		blinkt.set_pixel(FLAG_POS[1], PURPLE[0], PURPLE[1], PURPLE[2], brightness * 2.5)
	elif frLock == 2:
		if pulseBlinkOn:
			blinkt.set_pixel(FLAG_POS[1], PURPLE[0], PURPLE[1], PURPLE[2], brightness * 2.5)
		else:
			blinkt.set_pixel(FLAG_POS[1], 0, 0, 0, 0)
	


def pit_lim_led(data):
	pitLimiterOn = data.pitLimiterActive

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


