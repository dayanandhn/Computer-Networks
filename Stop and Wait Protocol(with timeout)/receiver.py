import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))



while 2:
	data=s.recv(1024).decode()
	flag = random.randint(0,1)
	t = random.randint(4,8)
	if flag:
		str= "1"
		print("Received --> "+data)
		time.sleep(t)
		s.send(str.encode())
	else:
		str = "0"
		print('error')
		s.send(str.encode())

s.close ()
