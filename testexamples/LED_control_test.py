import sys
sys.path.append("/home/pi/Desktop/homeDashboard/modules")

import game
import LEDcontrol as LED
import argparse
import signal
import time
import threading

parser = argparse.ArgumentParser()


def exit_app(sig, frame):
	print("Exiting via 'exit_app'")
	LED.exiting = True
	time.sleep(0.5)
	sys.exit()


if __name__ == '__main__':
    parser.add_argument("--fuel", type=float, default=50, help="Fuel level in liters")
    parser.add_argument("--hybrid", type=float, default=0, help="Hybrid level in percent")

    args = parser.parse_args()

    gameData = game.GameData()
    gameData.maxFuel = 100
    gameData.fuel       = args.fuel / 100.0
    gameData.hybrid_pct = args.hybrid

    LED_thread = threading.Thread(target=LED.init_and_run, args=(gameData,))
    LED_thread.run()

    signal.signal(signal.SIGINT, exit_app)