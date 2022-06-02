import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

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

def changeDuty(val):
    print(val)
    GPIO.output(18, True)
    pwm1.ChangeDutyCycle(val)
    GPIO.output(19, True)
    pwm2.ChangeDutyCycle(val)
    sleep(2)
    GPIO.output(18, False)
    pwm1.ChangeDutyCycle(val)
    GPIO.output(19, False)
    pwm2.ChangeDutyCycle(val)

setAngle(90)
sleep(1)
setAngle(0)
sleep(1)

#changeDuty(50)
#sleep(1)
#changeDuty(0)
#sleep(1)
#count = 0
#numLoops = 5

#while (count < numLoops):
#    changeDuty(count)
#    count = count+1;

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
