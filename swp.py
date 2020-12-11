#SLIDING WINDOW PROTOCOL

def receiver(frames):	
	#receiver receives the frames and appends to the received list
	received.append(frames)
	#ACKnowledgement sent by the receiver to the sender
	return "frames received"

def display_received():
	#Displays Received frames of the receiver
	print("Frames received by receiver: ", received)

def main():

	#main function to start the Sliding Window Protocol
	#ws = window size; fr = number of frames to be sent
	ws = int(input("Window Size:"))
	fr = int(input("No of frames:"))	
	#read the frames
	frames = list(map(int, input().split()))
	
	#current frames in the queue
	print("Window queue",frames)
	#send the frames and receive the ACK
	for i in range(0, len(frames), ws):
		crnt_frames = frames[i:i+ws]
		print(crnt_frames)
		print(receiver(crnt_frames))

	#display the frames received by the receiver
	display_received()
	
if __name__ == "__main__":
	#receiver list
	received = []
	#main() function invoking
	main()
	
