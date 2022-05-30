#Example Servo Code
#Control the angle of a 
#Servo Motor with Raspberry Pi

# free for use without warranty
# www.learnrobotics.org

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm1=GPIO.PWM(18, 50)
pwm1.start(0)
pwm2=GPIO.PWM(19, 50)
pwm2.start(0)

def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(18, True)
    pwm1.ChangeDutyCycle(duty)
    GPIO.output(19, True)
    pwm2.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(18, False)
    pwm1.ChangeDutyCycle(duty)
    GPIO.output(19, False)
    pwm2.ChangeDutyCycle(duty)

count = 0
numLoops = 2

while count < numLoops:
    print("set to 0-deg")
    setAngle(0)
    sleep(1)

        
    print("set to 90-deg")
    setAngle(90)
    sleep(1)

    print("set to 135-deg")
    setAngle(135)
    sleep(1)
    
    count=count+1

pwm.stop()
GPIO.cleanup()
