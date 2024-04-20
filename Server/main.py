import threading
import tkinter
import functions
import socket
from datetime import datetime

window = tkinter.Tk()
window.title("Messenger")

class server:
    def __init__(ip_address, port, self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if str(ip_address).lower() == ("localhost" or "self" or "127.0.0.1"):
            self.server_address = "127.0.0.1"
        else:
            self.server_address = str(ip_address)
        self.port = port
        

    def start_server(self):
        self.server.bind((self.server_ip, self.port))
        server.listen(0)
        print(f"listening on port {self.server_address}:{self.port} for a connection.")
        client_socket, client_address = server.accept()
        print(f"Accepted a connection from {client_address}:{client_socket} at ")