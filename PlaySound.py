#hehehehhhehehehehhehehehe :)
import pygame
import RPi.GPIO as GPIO
import time

def money():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(7,False)
    GPIO.output(15,False)
    pygame.mixer.init()
    pygame.mixer.music.load("herecomesthemoney.wav")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        GPIO.output(15,False)
        GPIO.output(7,True)
        time.sleep(0.1)
        GPIO.output(7,False)
        GPIO.output(15,True)
        time.sleep(0.1)
    GPIO.cleanup()
