from gpiozero import Button
from subprocess import check_call
from signal import pause

def cmd():
    #check_call(['cd', '/home/pi/python_scripts'])
    check_call(['python', '/home/pi/python_scripts/motor.py'])

btn = Button(17, hold_time=0.1)
btn.when_held = cmd

pause()
