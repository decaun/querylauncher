#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 11, 2018 03:57:06 PM CET  platform: Windows NT

import sys
import gui1
import subprocess
import threading, time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global deftext
    deftext='Password'


def ananas():
    input=w.Entry2.get()
    input2=w.Scrolledtext1.get(0.0,"end").encode("ascii")
    input2parsed=input2.splitlines()
    for line in input2parsed:
        thread = threading.Thread(target=procedure,args=(line.splitlines()))
        thread.start()
     

def procedure(dest):
    
    try:
        output2 = subprocess.check_output("ping "+dest+" -n 1", shell=False).decode("utf-8")
        w.Scrolledtext3.insert("end",'\n'+"++++++++++++++++++++++++++++++++++++++++"+'\n'+"--------------------"+"Output from: "+dest+'\n'+output2)
        w.Scrolledtext3.see("end")
    except subprocess.CalledProcessError as e:
        w.Scrolledtext3.insert("end",'\n'+"++++++++++++++++++++++++++++++++++++++++"+'\n'+"--------------------"+"Output from: "+dest+ " (ERROR!)"+'\n'+e.output)
        w.Scrolledtext3.see("end")


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui1.py
    gui1.py.vp_start_gui()




