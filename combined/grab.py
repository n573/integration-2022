import RPi.GPIO as GPIO
from time import sleep
import motor_pins as pin

#claw_pwm.ChangeDutyCycle(12.5)
#sleep(1.5)
pin.claw_pwm.ChangeDutyCycle(12.5)
sleep(2)
pin.claw_pwm.ChangeDutyCycle(5)
print("5")
sleep(0.5)
pin.claw_pwm.ChangeDutyCycle(2.5)
print("2.5")
sleep(0.5)

