#-*- coding: utf-8 -*-
"""
This file contains all human-like events like clicks and keyboard typing (simplified ..)
"""
import win32api, win32con
import time
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."


"""
# MOUSE MOVEMENTS
"""
def mousePos(x_pad,y_pad,cord):
    print("Going to "+str(cord[0])+ ","+str(cord[1]))
    x=cord[0]
    y=cord[1]
    win32api.SetCursorPos((x,y))

 

def get_cords(x_pad,y_pad):
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y