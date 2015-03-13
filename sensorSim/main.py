#!/usr/bin/env python

import socket, os
from time import sleep

import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import ttk

TCP_IP = 'localhost'
TCP_PORT = 9999
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

root = tk.Tk()
root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)
root.title("Sensor Simulator over TCP")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.NSEW))
mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(1, weight=1)
mainframe.grid_rowconfigure(0, weight=1)

alarmFrame = ttk.LabelFrame(mainframe, text="Alarm Summary",padding=(6, 6, 12, 12))
alarmFrame.grid(column=0, sticky=tk.NSEW, columnspan=2) #no row called out means it will be first unused row
alarmFrame.grid_columnconfigure(0, weight=1)
alarmFrame.grid_rowconfigure(0, weight=1)

alarmText = tkst.ScrolledText(alarmFrame,width=100,height=3)
alarmText.grid(row=0,column=0,sticky=tk.NSEW)

root.mainloop()