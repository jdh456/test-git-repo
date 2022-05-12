import RPi.GPIO as GPIO
import time

def button_callback(channel):
  print("button pushed")

button_pin=15

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(button_pin, GPIO.RISING,callback=button_callback)

while 1:
  time.sleep(0.1)
  
light_on = False

def button_callback(channel):
   global light_on
   if light_on == False:
     GPIO.output(led_pin, 1)
     print("LED ON!")
     
   else:
     GPIO.output(led_pin,0)
     print("LED OFF!)
     
   light_on  = not light_on



