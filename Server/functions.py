import socket
import random
import json

#the program will first start with 256 bit encryption, making sure that the initial setup messages for an enigma machine cipher are not readable to any network administrators.
#then, after it has set up the requirements for syncing 2 engima machines, the client and server will first encrypt some me

#so this is how the communication algorithm goes along:

#the client contacts the server on a reserved port asking it for a public key

#the server gives the public key to the client, which uses it to encrypt a private key and send that to the server on the same port with the same connection

#after the server recieves this key and decrypts it, it will send the port number to the client encrypted in it's private key, and will then close the conversation

#then, the client will contact the server using the private key on the specified port. if the client reaches the server within one minute, then the server will reserve that port for that specific client.
#if the client does not contact the server within the one minute, then the serve will open the port up for other clients, and will wipe the private key it has stored inside it.

#now then, let's see how the client obtains the subservers it has.

#the client will check if it has a unique id inside it's local storage. if it does, it will send it to the server, which will then read a json file and return the subservers it is inside of

#if the user clicks on a subserver, they will then send a message to the server asking for the last x number of texts inside the json file. once they recieve it, they will display it inside the client.



#key for what kind of communication the client wants to have:
#0: the client wants to connect to the server for the first time. this will make the server echo the response
#1: the client has previously connected to the server, and will thus need a port to communicate with the server
#2: the client wants to obtain the subserver list, and will provide it's uid in a later connection
#3: the client needs the content inside of a subserver, and will need to obtain the records of the subserver.

def generate_key():
    return random.randbytes(32)


def communicate(connection, address):
    connection_type = connection.recv("1")
    match connection_type:
        case b"0":
            new_key = generate_key()
            connection.send(new_key)
            private_key = connection.recv()

        case b"1":
            pass
        case b"2":
            pass
        case b"3":
            pass
    
