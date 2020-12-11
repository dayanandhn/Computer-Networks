import socket
from threading import *
import time
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            r=input("Send data -->")
            clientsocket.send(r.encode())
            ack=-1
            while 1:
                time.sleep(2)
                ack = int(clientsocket.recv(1024).decode())
                #print(ack)
                if ack > -1:
                    if ack == 1:
                        print("msg received")
                        break
                    if ack == 0:
                        print("not received timeout\nRetransmit")
                        clientsocket.send(r.encode())
                        continue
                else:
                    clientsocket.send(r.encode())
                    print("not received\nRetransmit")
                    continue
                    
serversocket.listen(5)
print("STOP AND WAIT ARQ")
print ('Sender ready and is listening')
while (True):

    #to accept all incoming connections
    clientsocket, address = serversocket.accept()
    print("Receiver "+str(address)+" connected")
    #create a different thread for every 
    #incoming connection 
    client(clientsocket, address)
