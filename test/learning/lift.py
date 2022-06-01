import RPi.GPIO as GPIO
from time import sleep

claw = 19
servo = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(claw, GPIO.OUT)
GPIO.setup(servo, GPIO.OUT)

claw_pwm = GPIO.PWM(claw, 50)
s_pwm = GPIO.PWM(servo, 50)
s_pwm.start(0) # Initialization
claw_pwm.start(0) # Initialization

count = 0
try:
    #s_pwm.ChangeDutyCycle(5);
    #sleep(2)
    
  while count<4:
      s_pwm.ChangeDutyCycle(count*2.5);
      sleep(2)
      #s_pwm.ChangeDutyCycle(5);
      #sleep(2)
      #s_pwm.ChangeDutyCycle();
      #s_pwm.ChangeDutyCycle(count)
      #claw_pwm.ChangeDutyCycle(10)
      #sleep(1.5)
      s_pwm.ChangeDutyCycle(0);
      sleep(2)
      count = count+1
except KeyboardInterrupt:
    s_pwm.ChangeDutyCycle(0);
    s_pwm.stop()
    claw_pwm.stop()
    GPIO.cleanup()

