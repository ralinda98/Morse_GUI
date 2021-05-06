from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
from time import sleep
import sys

ledOut = LED(14)

## GUI DEFINITIONS ##
win = Tk()
win.title("Text to Morse Code Converter")
win.geometry("500x400")

myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Dot signal
def dit():
    ledOut.on()
    sleep(0.15)
    ledOut.off()
    sleep(0.15)

## Dash Signal
def dah():
    ledOut.on()
    sleep(0.5)
    ledOut.off()
    sleep(0.15)

## Function to convert letter to morse code letter.
def convertToMorse(letter):
    letter = letter.lower()
    if letter == 'a':
        dit()
        dah()
    if letter == 'b':
        dah()
        dit()
        dit()
        dit()
    if letter == 'c':
        dah()
        dit()
        dah()
        dit()
    if letter == 'd':
        dah()
        dit()
        dit()
    if letter == 'e':
        dit()
    if letter == 'f':
        dit()
        dit()
        dah()
        dit()
    if letter == 'g':
        dah()
        dah()
        dit()
    if letter == 'h':
        dit()
        dit()
        dit()
        dit()
    if letter == 'i':
        dit()
        dit()
    if letter == 'j':
        dit()
        dah()
        dah()
        dah()
    if letter == 'k':
        dah()
        dit()
        dah()
    if letter == 'l':
        dit()
        dah()
        dit()
        dit()
    if letter == 'm':
        dah()
        dah()
    if letter == 'n':
        dah()
        dit()
    if letter == 'o':
        dah()
        dah()
        dah()
    if letter == 'p':
        dit()
        dah()
        dah()
        dit()
    if letter == 'q':
        dah()
        dah()
        dit()
        dit()
    if letter == 'r':
        dit()
        dah()
        dit()
    if letter == 's':
        dit()
        dit()
        dit()
    if letter == 't':
        dah()
    if letter == 'u':
        dit()
        dit()
        dah()
    if letter == 'v':
        dit()
        dit()
        dit()
        dah()
    if letter == 'w':
        dit()
        dah()
        dah()
    if letter == 'x':
        dah()
        dit()
        dit()
        dah()
    if letter == 'y':
        dah()
        dit()
        dah()
        dah()
    if letter == 'z':
        dah()
        dah()
        dit()
        dit()

## Function to get the text from the text box        
def getText():
    text = textBox.get(1.0, END)    ## gets letters starting from letter one to end letter.
    for x in text:                  ## goes through each letter and converts each letter to morse code.
        convertToMorse(x)
        sleep(0.5)                  ## 500ms gap between each letter.

def close():
    RPi.GPIO.cleanup()
    win.destroy()

textBox = Text(win, height = 5, width = 33, font=("Helvetica", 20))
textBox.grid(row = 0, column = 1)

morseButton = Button(win, text = 'Morse', font = myFont, command = getText, bg = 'bisque2', height = 5, width = 33)
morseButton.grid(row = 10, column = 1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()