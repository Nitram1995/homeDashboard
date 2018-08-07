import RPi.GPIO as GPIO
from LEDcontrol import led_brightness_inc
import time

PRESSED = 0
RELEASED = 1

SHORT_PRESS_LIMIT = 0.5

BTN_BLK = 12
BTN_WHT = 16

app = None

btn_blk_pressed_time = 0
btn_wht_pressed_time = 0

def buttons_init(appReference):
	global app
	app = appReference
	GPIO.setmode(GPIO.BCM)
	GPIO.setup((BTN_BLK, BTN_WHT), GPIO.IN)


def button_interupt_init(btn, func):
	GPIO.add_event_detect(btn, GPIO.BOTH, func)


def btn_blk_changed(btn_id):
	global btn_blk_pressed_time
	if(GPIO.input(btn_id) == PRESSED):
		currentTime = time.time()
		btn_blk_pressed_time = currentTime
	else:
		currentTime = time.time()
		if(currentTime - btn_blk_pressed_time > SHORT_PRESS_LIMIT):
			btn_blk_long_press()
		else:
			btn_blk_short_press()


def btn_wht_changed(btn_id):
	global btn_wht_pressed_time
	if(GPIO.input(btn_id) == PRESSED):
		currentTime = time.time()
		btn_wht_pressed_time = currentTime
	else:
		currentTime = time.time()
		if(currentTime - btn_wht_pressed_time > SHORT_PRESS_LIMIT):
			btn_wht_long_press()
		else:
			btn_wht_short_press()


def btn_blk_short_press():
	print("BTN_BLK short press registered at", btn_blk_pressed_time)
	pass


def btn_blk_long_press():
	print("BTN_BLK long press registered at", btn_blk_pressed_time)
	app.exit_app()


def btn_wht_short_press():
	print("BTN_WHT short press registered at", btn_wht_pressed_time)
	led_brightness_inc()


def btn_wht_long_press():
	print("BTN_WHT long press registered at", btn_wht_pressed_time)
	pass
