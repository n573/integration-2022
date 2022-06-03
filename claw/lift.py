import RPi.GPIO as GPIO
from time import sleep

servo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)

s_pwm = GPIO.PWM(servo, 50)
s_pwm.start(0) # Initialization

delay = 0.1
#count = 0
try:
    #s_pwm.ChangeDutyCycle(5);
    #sleep(2)
    
#  while count<5:
   while True:
       s_pwm.ChangeDutyCycle(2.5);
       print("2.5")
       sleep(delay)
       s_pwm.ChangeDutyCycle(5);
       print("5")
       sleep(delay)
       s_pwm.ChangeDutyCycle(7.5);
       print("7.5")
       sleep(delay)
       s_pwm.ChangeDutyCycle(10);
       print("10")
       sleep(delay)
       s_pwm.ChangeDutyCycle(12.5);
       print("12.5")
       sleep(delay)
       s_pwm.ChangeDutyCycle(7.5);
       print("7.5")
       sleep(delay)
       s_pwm.ChangeDutyCycle(0);
       print("0")
       sleep(1)
       
       #count = count+1
except KeyboardInterrupt:
    s_pwm.ChangeDutyCycle(0);
    s_pwm.stop()
    GPIO.cleanup()

