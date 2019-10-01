#!/usr/bin/env python
# coding: utf-8

import RPi.GPIO as IO
import time

def countdown(a):
    for i in range(a, 0, -1):
        fan.ChangeDutyCycle(i)
        time.sleep(0.06)

IO.setmode(IO.BCM)
IO.setup(21,IO.OUT)
fan = IO.PWM(21,1000)

fan.start(0) # για να προλάβω να πάω μέσα
time.sleep(10) # για να προλάβω να πάω μέσα
countdown(89)
time.sleep(2)
#fan.ChangeDutyCycle(0) # 7 Volt
#time.sleep(5)
fan.ChangeDutyCycle(70) # 7 Volt
time.sleep(2)
fan.ChangeDutyCycle(37) # 7 Volt
input("PRESS anything to stop")

#while True:
#    start = int(input("Insert speed or 0 to stop: "))
#    if start != 0:
#        fan.ChangeDutyCycle(start)
#        time.sleep(10)
#        continue
#    if start == 0:
#        break

IO.cleanup()

