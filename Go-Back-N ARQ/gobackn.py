import random

if __name__ == "__main__":
	n = int(input("Window Size: "))
	nf = int(input("Frames: "))
	frames = [x for x in range(0, nf)]
	tr=0
	i=0
	while i<nf:
		x, j = 0, i
		while j<i+n and j<nf:
		    print("sent frame: ",j)
		    tr+=1
		    j=j+1
		j=i
		while j<i+n and j<nf:
			flag = random.randint(0,1)
			if flag:
				print("Acknowledged frame", j)
				x=x+1
			else:
				print("Frame ",j, " not received\nRetransmit")
				break
			j=j+1
		i+=x
	print("No of transmission: ", tr)


