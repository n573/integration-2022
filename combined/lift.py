import RPi.GPIO as GPIO
from time import sleep
import motor_pins as pin

delay = 0.1
pin.s_pwm.ChangeDutyCycle(2.5);
print("2.5")
sleep(delay)
pin.s_pwm.ChangeDutyCycle(5);
print("5")
sleep(delay)
pin.s_pwm.ChangeDutyCycle(7.5);
print("7.5")
sleep(delay)
pin.s_pwm.ChangeDutyCycle(10);
print("10")
sleep(delay)
pin.s_pwm.ChangeDutyCycle(12.5);
print("12.5")
sleep(delay)
pin.s_pwm.ChangeDutyCycle(7.5);
print("7.5")
sleep(delay)
pin.s_pwm.ChangeDutyCycle(0);
print("0")
sleep(1)
