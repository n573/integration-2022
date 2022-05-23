from time import sleep
from signal import pause
import pins as pin
from bluedot import BlueDot
bd = BlueDot()

def setAngle(phi):
    duty = phi / 18 + 2
    pin.set(18,'on')
    pin.step1.ChangeDutyCycle(duty)
    sleep(1)
    pin.set(18,'off')
    pin.step1.ChangeDutyCycle(0)

def closeOut():
    pin.step1.stop()
    pin.p1.stop()
    pin.p2.stop()
    pin.GPIO.cleanup()

def dpad(pos):
    if pos.top:
        pin.step1.ChangeDutyCycle(50)
    elif pos.bottom:
        pin.step1.ChangeDutyCycle(10)
    else:
        pin.coast()

bd.when_moved = dpad
pause()
#def speed_up(i):
#    print("speed_up")
#    for x in range (i):                          #execute loop for 50 times, x being incremented from 0 to 49.
#        pin.p1.ChangeDutyCycle(x)
#        pin.p2.ChangeDutyCycle(x)
#        #sleep(0.1)                           #sleep for 100m second

#def slow_down(i):
#    print("slow_down")
#    for x in range (i):                         #execute loop for 50 times, x being incremented from 0 to 49.
#        pin.p1.ChangeDutyCycle(i-x)
#        pin.p2.ChangeDutyCycle(i-x)
        #sleep(0.1)                          #sleep for 100m seconds
