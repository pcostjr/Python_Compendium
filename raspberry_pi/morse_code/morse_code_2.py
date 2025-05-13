# Byron Manuel, Sean Devine, Jordan Arrington
# 03/23/23
import RPi._GPIO as GPIO
from time import sleep
import math

#Defines mode and disables warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Sets up pin
PIN = 21
GPIO.setup(PIN, GPIO.OUT)

#Sets the frequency (pitch) of the buzzer
buzzer = GPIO.PWM(PIN, 700)

#Dictionary of key characters with specific 0,1 values representing morse
morse_code = {
    "a": (0, 1),
    "b": (1, 0, 0, 0),
    "c": (1, 0, 1, 0),
    "d": (1, 0, 0),
    "e": (0,),
    "f": (0, 0, 1, 0),
    "g": (1, 1, 0),
    "h": (0, 0, 0, 0),
    "i": (0, 0),
    "j": (0, 1, 1, 1),
    "k": (1, 0, 1),
    "l": (0, 1, 0, 0),
    "m": (1, 1),
    "n": (1, 0),
    "o": (1, 1, 1),
    "p": (0, 1, 1, 0),
    "q": (1, 1, 0, 1),
    "r": (0, 1, 0),
    "s": (0, 0, 0),
    "t": (1,),
    "u": (0, 0, 1),
    "v": (0, 0, 0, 1),
    "w": (0, 1, 1),
    "x": (1, 0, 0, 1),
    "y": (1, 0, 1, 1),
    "z": (1, 1, 0, 0),
    "0": (1, 1, 1, 1, 1),
    "1": (0, 1, 1, 1, 1),
    "2": (0, 0, 1, 1, 1),
    "3": (0, 0, 0, 1, 1),
    "4": (0, 0, 0, 0, 1),
    "5": (0, 0, 0, 0, 0),
    "6": (1, 0, 0, 0, 0),
    "7": (1, 1, 0, 0, 0),
    "8": (1, 1, 1, 0, 0),
    "9": (1, 1, 1, 1, 0),
    ".": (0, 1, 0, 1, 0, 1),
    ",": (1, 1, 0, 0, 1, 1),
    "?": (0, 0, 1, 1, 0, 0),
    "/": (1, 0, 0, 1, 0),
}

#Sets the speed of the morse code
duration = .2

running = True
while(running):
    #Gets user input to be converted to morse
    msg = input("Enter Input: ").lower()

    #Starts the buzzer
    buzzer.start(0)

    if msg == "-1":
        running = False
        print("Program Ended")
    else:
        #for each word in the sentence
        for word in msg.split(" "):
            #go through each letter
            for char in word:
                #checks to see if character is in morse code dictionary
                if char in morse_code:
                    #go through each dot and dash, play sound
                    for bit in morse_code[char]:
                        #start playing sound
                        buzzer.ChangeDutyCycle(10)
                        #wait for x amount of time
                        sleep(duration if bit == 0 else 3 * duration)
                        #then stop playing sound
                        buzzer.ChangeDutyCycle(0)
                        #pause in between dot and dash
                        sleep(duration)
                #pause in between letters
                sleep(duration * 3)
            #pause in between words
            sleep(duration * 7)
#reset pins
GPIO.cleanup()