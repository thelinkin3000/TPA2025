"""Example for Pico. Turns on the built-in LED."""
import board
import time
import digitalio

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)