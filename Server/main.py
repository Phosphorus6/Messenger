import tkinter as tk
import socket
import requests
import json
import os
import threading
import functions
import random

#tkinter code is here
window = tk.Tk()
window.geometry()
window.title("Python-Messager Info")
Main_Frame = tk.Frame(window)
Main_Frame.pack()
settings_frame = tk.Frame(window)
subserver_deletion_frame = tk.Frame(window)
Delete_Logs_Sure = tk.Frame()
settings_button = tk.Button(Main_Frame, text="Settings", width=10, height=3, command=lambda: [Main_Frame.pack_forget(), settings_frame.pack()])



#settings frame contents
logging_state = True
log_archiving_state = True

def Logging_Button():
    logging_state != logging_state
    if logging_state:
        Logging = tk.Button(settings_frame, width=20, height=3, text="Logging: ON")
        Logging.pack()
    else:
        Logging = tk.Button(settings_frame, width=20, height=3, text="Logging: OFF")
        Logging.pack()

def log_archiving():
    log_archiving_state != log_archiving_state
    if log_archiving_state:
        Log_Archiving = tk.Button(settings_frame,text="Log Archiving: ON", width=20, height=3,command=log_archiving)
        Log_Archiving.pack()
    else:
        Log_Archiving = tk.Button(settings_frame,text="Log Archiving: OFF", width=20, height=3,command=log_archiving)
        Log_Archiving.pack()
    


Logging = tk.Button(settings_frame, width=20, height=3, text="Logging: ON", command=Logging_Button)
Logging.pack()

Log_Archiving = tk.Button(settings_frame,text="Log Archiving: ON", width=20, height=3,command=log_archiving)
Log_Archiving.pack()

Log_Deletion = tk.Button(settings_frame, height=3, width=20, text="Delete Logs", command=lambda: [settings_frame.pack_forget(), Delete_Logs_Sure.pack()])

Subserver_Limit = tk.Scale(settings_frame, from_=0, to=10)

Subserver_deletion = tk.Button(settings_frame, height=3, width=20, text="Subserver Deletion")

reload = tk.Button(settings_frame, height=3, width=20, text="Reload")

back_settings = tk.Button(settings_frame, width=20,height=3, text="Back", command=lambda: [settings_frame.pack_forget(), Main_Frame.pack()])


#Log Deletion Frame
host = requests.get('https://api.ipify.org').content.decode('utf8')
if f"{range(0, 226)}.{range(0,226)}.{range(0,226)}.{range(0,226)}" in host :
    print("Valid IP Address! we will bedin setting up the server.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, 80))
else:
    print("Error 1:IP address is invalid")
    json.dump(open(f"{os.getcwd()}\\logs\\errors.json", "r"))
    os._exit()


while True:
    window.update()
    server.listen()