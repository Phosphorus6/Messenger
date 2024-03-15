#the first section will be the section that you will run for multiple access points. to enable this, please select reset server, select keep logs, then enable multiple access points in there

from _typeshed import Self
import threading
import json
import random
import socket


class Server:
    def __init__(Main_Server, Logs_Server_IP, self, Nodes_Key) -> None:
        #if the  current computer is the Main Node, then we will have different configurations.
        if Main_Server == ("127.0.0.1" or 'localhost' or 'self'):
            self.threaded_Main_Setup = threading.Thread(target=self.__Main_Server_Setup)
            self.threaded_Main_Setup.start()
        #if this is an access node for the data.
        else:
            pass
        #if this is the data storage node, we need to do something different.
        if Logs_Server_IP == ('127.0.0.1' or 'localhost' or 'self'):
            pass
        #if it is not, then configure this as a non-data storage server
        else:
            pass

    def __Main_Server_Setup(self, nodes_key):
        self.nodes_server_list = []
        self.Nodes_Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Nodes_Server.bind("127.0.0.1", 8000)
        while True:
            self.Nodes_Server.listen(1)
            self.connection, self.address = self.Nodes_Server.accept()
            print(f"Connected by node {self.address}.")
            self.nodes_server_list.append(threading.Thread(target=self.__communicate_with_nodes, args=(nodes_key, self.connection, self.address, len(self.nodes_server_list))))
            self.nodes_server_list[-1].start()
            
            
    
    def __communicate_with_nodes(nodes_key, connection, address, index, self):
        key = connection.recv(32)
        if key != bytes(nodes_key):
            print(f"Key Provided by Node {address} is invalid, thus disconnecting to prevent connection to malicious node.")
            self.nodes_server_list[index - 1].exit()



        
        
        




#this code will be run if this is the only access point for the server