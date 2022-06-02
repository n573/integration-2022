from gpiozero import AngularServo
from time import sleep

servo = AngularServo(18)

print(servo.min_angle)
print(servo.max_angle)
print(servo.angle)
servo.angle = 45.0
sleep(1)
print(servo.angle)
servo.angle = -45.0
print(servo.angle)

#servo.min()
#sleep(1)
#servo.max()

#while True:
#    servo.min()
#    sleep(1)
#    servo.mid()
#    sleep(1)
#    servo.max()
#    sleep(1)
