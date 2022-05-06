from marvelmind import MarvelmindHedge
from time import sleep
import sys
import motor as mot

def main():
    hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=17, debug=False) # create MarvelmindHedge thread

    if (len(sys.argv)>1):
        hedge.tty= sys.argv[1]

    mot.pin.coast();
    hedge.start() # start thread
    while True:
        try:
            hedge.dataEvent.wait(1)
            hedge.dataEvent.clear()

            if (hedge.positionUpdated):
                hedge.print_position()
                mot.forward();

            if (hedge.distancesUpdated):
                hedge.print_distances()
                #mot.speed_up(30);

            if (hedge.rawImuUpdated):
                hedge.print_raw_imu()

            if (hedge.fusionImuUpdated):
                hedge.print_imu_fusion()

            if (hedge.telemetryUpdated):
                hedge.print_telemetry()

            if (hedge.qualityUpdated):
                hedge.print_quality()

            if (hedge.waypointsUpdated):
                hedge.print_waypoint()
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            mot.pins.coast();
            sys.exit()
main()
