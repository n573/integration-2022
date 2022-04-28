from bluedot import BlueDot
from time import sleep
import motor_pins as pin

def forward():
    print('f')
    pin.set('d1','on')
    pin.set('d2','off')
    pin.set('d3', 'on')
    pin.set('d4','off')

def backward():
    print('b')
    pin.set('d1','off')
    pin.set('d2','on')
    pin.set('d3', 'off')
    pin.set('d4','on')

def speed_up(i):
    print("speed_up")
    for x in range (i):                          #execute loop for 50 times, x being incremented from 0 to 49.
        pin.p1.ChangeDutyCycle(x)
        pin.p2.ChangeDutyCycle(x)
        #sleep(0.1)                           #sleep for 100m second

def slow_down(i):
    print("slow_down")
    for x in range (i):                         #execute loop for 50 times, x being incremented from 0 to 49.
        pin.p1.ChangeDutyCycle(i-x)
        pin.p2.ChangeDutyCycle(i-x)
        #sleep(0.1)                          #sleep for 100m second

def right(i):
    pin_right()
    print("right")
    print(i)
    for x in range (i):
        pin.p1.ChangeDutyCycle(i-x)
        pin.p2.ChangeDutyCycle(x)
        #sleep(0.1)

def left(i):
    pin_left()
    print("left")
    print(i)
    for x in range (i):
        pin.p1.ChangeDutyCycle(x)
        pin.p2.ChangeDutyCycle(i-x)
        #sleep(0.1)

def pin_left():
    print('L')
    pin.set('d1','on')
    pin.set('d2','off')
    pin.set('d3', 'off')
    pin.set('d4','on')

def pin_right():
    print('R')
    pin.set('d1','off')
    pin.set('d2','on')
    pin.set('d3', 'on')
    pin.set('d4','off')
