#!/usr/bin/python3.7
import time
from adafruit_servokit import ServoKit
ServoKit
kit = ServoKit(channels=16)

def turnRight():
    kit.servo[1].angle = 45
    time.sleep(4)
    kit.servo[1].angle = 0
    time.sleep(4)
def turnLeft(x):
    kit.servo[1].angle = 0
    time.sleep(4)
    kit.servo[1].angle = x
    time.sleep(4)


def shoot():
    kit.servo[0].angle = 180
    time.sleep(.1)
    kit.servo[0].angle = 0
    time.sleep(1)
    kit.servo[0].angle = 180



