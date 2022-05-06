from marvelmind import MarvelmindHedge
from time import sleep
import sys
import motor as mot
import math
import array as arr

def main():
    hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=17, debug=False) # create MarvelmindHedge thread
    hedge.start() # start thread
    mot.pin.coast()
    xDest = 0
    yDest = 0
    destination = True
    x_dests = arr.array('d',[2.32, 5.37, 8.35, 5.41])
    y_dests = arr.array('d',[0.5, -3.5, -0.68, 2.8])
    count = 0
    while True:
        try:
            #sleep(1)
            #mot.forward()
            sleep(1)
            print (hedge.position()) # get last position and print
            hedge.print_position()
            #(x, y, z, t) = hedge.position
            if(destination == True or (xDest == 0 and yDest == 0)):
                #print('enter X dest')
                xDest = x_dests[count]#input()
                #print('enter Y dest')
                yDest = y_dests[count]#input()
                count=count+1

            prev = hedge.position_buffer()[0]
            curr = hedge.position_buffer()[2]
            print("prev")
            print(prev)
            print("curr")
            print(curr)
            if((xDest <= (curr[1]+1) and xDest >= (curr[1]-1)) and (yDest <= (curr[2]+1) and yDest >= (curr[2]-1))):
                destination = True
            else:
                destination = False

            vx = xDest - curr[1]#dest
            vy = yDest - curr[2]#dest
            ux = curr[1] - prev[1]#pi
            uy = curr[2] - prev[2]#pi

            #ang1 = math.acos(ux/math.sqrt(math.pow(ux,2) + math.pow(uy,2)))
            #ang2 = math.acos(vx/math.sqrt(math.pow(vx,2) + math.pow(vy,2)))
            #ang = ang2-ang1
            #print(ang)

            print('destination reached?')
            print(destination)
            #if(ang > 0):
                #mot.left()
            #elif(ang < 0):
                #mot.right()
            #else:
                #mot.forward()

            sleep(1)
            if count == 3:
                break #breaks out of while loop if all points are reached
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()
main()
