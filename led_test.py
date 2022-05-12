import RPi.GPI0 as GPI0
import time

led_pin = 4

GPI0.setwarnings(False)

GPI0.setmode(GPI0.BCM)

GPI0.setup(led_pin, GPI0.OUT)

for i in range(10):
   GPI0.output(led_pin, 1)
   time.sleep(1)
   GPI0.output(led_pin, 0)
   time.sleep(1)
GPI0.cleanup()
