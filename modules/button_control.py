import RPi.GPIO as GPIO

BTN_BLK = 12
BTN_WHT = 16

def buttons_init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((BTN_BLK, BTN_WHT), GPIO.IN)


def button_interupt_init(btn, func):
	GPIO.add_event_detect(btn, GPIO.BOTH, func)
