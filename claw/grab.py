import RPi.GPIO as GPIO
from time import sleep

claw = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(claw, GPIO.OUT)

claw_pwm = GPIO.PWM(claw, 50)
claw_pwm.start(12.5) # Initialization

#claw_pwm.ChangeDutyCycle(12.5)
#sleep(1.5)
claw_pwm.ChangeDutyCycle(12.5)
sleep(2)
try:
  while True:
    claw_pwm.ChangeDutyCycle(5)
    print("5")
    sleep(0.5)
    claw_pwm.ChangeDutyCycle(2.5)
    print("2.5")
    sleep(0.5)

except KeyboardInterrupt:
  claw_pwm.ChangeDutyCycle(12.5)
  claw_pwm.stop()
  GPIO.cleanup()
claw_pwm.ChangeDutyCycle(12.5)
