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
