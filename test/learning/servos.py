import RPi.GPIO as GPIO
import time

claw = 19
servo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(claw, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

claw_pwm = GPIO.PWM(claw, 50)
s_pwm = GPIO.PWM(servo, 50)
s_pwm.start(0) # Initialization
claw_pwm.start(0) # Initialization
try:
  while True:
    s_pwm.ChangeDutyCycle(5)
    claw_pwm.ChangeDutyCycle(5)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(7.5)
    claw_pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(10)
    claw_pwm.ChangeDutyCycle(10)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(12.5)
    claw_pwm.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(10)
    claw_pwm.ChangeDutyCycle(10)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(7.5)
    claw_pwm.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(5)
    claw_pwm.ChangeDutyCycle(5)
    time.sleep(0.5)
    s_pwm.ChangeDutyCycle(2.5)
    claw_pwm.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  s_pwm.stop()
  GPIO.cleanup()
