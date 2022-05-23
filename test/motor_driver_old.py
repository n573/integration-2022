from bluedot import BlueDot
import motor as mot
from time import sleep
from signal import pause
bd = BlueDot()
import marvelmind_test as ros

import multiprocessing

def comeON():
    ros.main()

autonomous_thread = multiprocessing.Process(target=comeON)


pressed = 0
auto_state = 0


#mot.pin.p1.start(50)
#mot.pin.p2.start(50)
def dpad(pos):
    if pos.top:
        mot.forward(int(pos.y*100))
        #mot.forward()
        #mot.speed_up(int(pos.y*100))
    elif pos.right:
        #print(pos.x)
        #mot.right(int(pos.x*100))
        mot.right(int(pos.x*100))
        #mot.speed_up(int(pos.x*100))
    elif pos.left:
        #print(pos.x)
        mot.left(int(-pos.x*100))
        #mot.speed_up(int(-pos.x*100))
    elif pos.bottom:
        mot.backward(int(-pos.y*100))
        #mot.speed_up(int(-pos.y*100))
    #elif pos.middle:
    #    mot.pin.coast()
    else:
        mot.pin.coast()
        #sleep(1)
bd.when_moved = dpad


def bPress():
    print("")
    #print("fck")

def bRelease():
    #comeON()
    global pressed
    global auto_state

    auto_state = 1

    if pressed == 0:
        pressed = 1
    else:
        pressed = 0


#bd.when_doubled_pressed = bRelease #comeON#ros.main()
#print(pressed)
#if pressed == 1:
#    print("toggled")
#    comeON()

bd.when_released = bRelease
#bd.when_pressed = ros.main()#mot.pin.coast()
#pause()

while(1):

    auto_state = 0

    sleep(.5)
    if auto_state == 1:
        if pressed == 1:
            print("toggled")
            autonomous_thread.terminate()
            #comeON()
        elif pressed == 0:
            print("toggled off")
            autonomous_thread.start()
    elif auto_state == 0:
        print("chillin")
