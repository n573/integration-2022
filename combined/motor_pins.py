import RPi.GPIO as GPIO

pins = [{'pin_num': 9, 'name': 'd1'},
        {'pin_num': 8, 'name': 'd2'},
        {'pin_num': 7, 'name': 'd3'},
        {'pin_num': 1, 'name': 'd4'}]

GPIO.setmode(GPIO.BCM)  # use GPIO numbering, not generic
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
p1 = GPIO.PWM(12,1000)
p2 = GPIO.PWM(13,1000)
p1.start(0)
p2.start(0)
servo = 18
GPIO.setup(servo, GPIO.OUT)
s_pwm = GPIO.PWM(servo, 50)
s_pwm.start(0) # Initialization
claw = 19
GPIO.setup(claw, GPIO.OUT)
claw_pwm = GPIO.PWM(claw, 50)
claw_pwm.start(12.5) # Initialization

# setup all logic pins based on above configuration
for pin in pins:
    GPIO.setup(pin['pin_num'], GPIO.OUT, initial=GPIO.LOW)

def set(name, state):
    pin_nums = [pin['pin_num'] for pin in pins if pin['name'] == name]
    for pin_num in pin_nums:
        if state == 'on':
            GPIO.output(pin_num, GPIO.HIGH)
        elif state == 'off':
            GPIO.output(pin_num, GPIO.LOW)

def coast():
    print("coast")
    for pin in pins:
        GPIO.output(pin['pin_num'], GPIO.LOW)
