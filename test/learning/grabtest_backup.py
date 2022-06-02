import RPi.GPIO as GPIO
#from time import sleep
import time

claw = 19
#delay = 0.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(claw, GPIO.OUT)

claw_pwm = GPIO.PWM(claw, 50)
claw_pwm.start(0) # Initialization

claw_pwm.ChangeDutyCycle(5)
print("5")
time.sleep(0.5)
#claw_pwm.ChangeDutyCycle(7.5)
#print("7.5")
#time.sleep(0.5)
claw_pwm.ChangeDutyCycle(10)
print("10")
time.sleep(0.5)
claw_pwm.ChangeDutyCycle(12.5)
print("12.5")
time.sleep(0.5)
#claw_pwm.ChangeDutyCycle(10)
#print("10")
#time.sleep(0.5)
#claw_pwm.ChangeDutyCycle(7.5)
#print("7.5")
#time.sleep(0.5)
claw_pwm.ChangeDutyCycle(5)
print("5")
time.sleep(0.5)
#claw_pwm.ChangeDutyCycle(2.5)
#print("2.5")
#time.sleep(0.5)



#try:
#  while True:
#    claw_pwm.ChangeDutyCycle(5)
#    sleep(1.5)
#    claw_pwm.ChangeDutyCycle(10)
#    sleep(1.5)
#    claw_pwm.ChangeDutyCycle(0)
#    sleep(1.5)
#except KeyboardInterrupt:
#  claw_pwm.stop()
#  GPIO.cleanup()
claw_pwm.stop()
GPIO.cleanup()
