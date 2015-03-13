'''
Created on 13 Mar,2015

@author: bryan.bywalec
'''
import time
from tkinter import ttk
import socket

import tkinter as tk
import tkinter.scrolledtext as tkst

def update():
    timeStr = time.strftime("%I:%M:%S",time.localtime(time.time()))
    messageStr = timeStr + ": hello\n"
    alarmText.insert(1.0, messageStr)
    alarmText.after(1000,update)

    #send information out on serial address

HOST, PORT = "localhost", 9999

if __name__ == "__main__":


    root = tk.Tk()
    root.grid_rowconfigure(0,weight=1)
    root.grid_columnconfigure(0,weight=1)

    root.title("Sensor Simulator V0.1")

    mainframe = ttk.Frame(root, padding="5 5 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.NSEW))
    mainframe.grid_columnconfigure(0, weight=1)
    mainframe.grid_columnconfigure(1, weight=1)
    mainframe.grid_rowconfigure(0, weight=1)

    alarmFrame = ttk.LabelFrame(mainframe, text="TCP Socket Message Log",padding=(6, 6, 12, 12))
    alarmFrame.grid(column=0, sticky=tk.NSEW, columnspan=2) #no row called out means it will be first unused row
    alarmFrame.grid_columnconfigure(0, weight=1)
    alarmFrame.grid_rowconfigure(0, weight=1)

    alarmText = tkst.ScrolledText(alarmFrame,width=100,height=3)
    alarmText.grid(row=0,column=0,sticky=tk.NSEW)

    update()
    root.mainloop()