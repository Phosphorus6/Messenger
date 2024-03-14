#the first section will be the section that you will run for multiple access points. to enable this, please select reset server, select keep logs, then enable multiple access points in there

import random
import json
import random
import socket

class Server:
    def __init__(Main_Server, Logs_Server_IP) -> None:
        if Main_Server == ("127.0.0.1" or 'localhost' or 'self'):
            pass
        else:
            pass

        if Logs_Server_IP == ('127.0.0.1' or 'localhost' or 'self'):
            pass
        else:
            pass
    def Main_Server_Setup(Access_Port):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM).bind(('localhost', Access_Port))


class Nodes:
    def __init__(Access_Server, Access_Port, Server_Address, self):
        self.Server_Address = Server_Address
        self.Client_Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM).bind("127.0.0.1", Access_Port)
        
        
        




#this code will be run if this is the only access point for the server