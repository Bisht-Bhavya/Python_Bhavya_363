import tkinter as tk
import time

def utime():
    current_time = time.strftime("%H:%M:%S")
    label.config(text = current_time)
    label.after( 1000, utime ) #schedule function 

