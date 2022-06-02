import RPi.GPIO as GPIO
import time

claw = 19
servo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(claw, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

claw_pwm = GPIO.PWM(claw, 50)
s_pwm = GPIO.PWM(servo, 50)
s_pwm.start(2.5) # Initialization
claw_pwm.start(2.5) # Initialization

