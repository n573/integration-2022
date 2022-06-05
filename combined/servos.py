import RPi.GPIO as GPIO
from time import sleep
import motor_pins as pin

delay = 0.1
flag1 = 0;
flag2 = 0;

def grab():
    if flag1 == 0:
        release()
        flag1 = 1
    elif flag1 == 1:
        hold()
        flag1 = 0

def arm():
    if flag2 == 0:
        lift()
        flag2 = 1
    elif flag2 == 1:
        down()
        flag2 = 0

def release():
    pin.claw_pwm.ChangeDutyCycle(12.5)
    sleep(1.5)
def hold():
    pin.claw_pwm.ChangeDutyCycle(5)
    print("5")
    sleep(0.5)
    pin.claw_pwm.ChangeDutyCycle(2.5)
    print("2.5")
    sleep(0.5)
def lift():
    pin.s_pwm.ChangeDutyCycle(2.5);
    sleep(delay)
    pin.s_pwm.ChangeDutyCycle(5);
    sleep(delay)
    pin.s_pwm.ChangeDutyCycle(7.5);
    sleep(delay)
    pin.s_pwm.ChangeDutyCycle(10);
    sleep(delay)
    pin.s_pwm.ChangeDutyCycle(12.5);
def down():
    pin.s_pwm.ChangeDutyCycle(7.5);
    sleep(delay)
    pin.s_pwm.ChangeDutyCycle(0);
    sleep(delay)