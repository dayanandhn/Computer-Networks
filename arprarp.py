fl =[]
with open("ipmac2.txt", 'r') as file:
	fl = file.readlines()
	file.close()
#print(fl)

table=[]
for line in fl:
	table.append(line.split())

print(table)


def ARP(ip):
	flag = 0
	for it in table[1:]:
		if it[0] == ip:
			print("\t\t".join(table[0]))
			print("\t\t\t".join(it))
			flag = 1
			break
	if flag == 0:
		print("Mac not found for the given Ip",ip)

def RARP(mac):
	flag = 0
	for it in table[1:]:
		if it[1] == mac:
			print("\t\t".join(table[0]))
			print("\t\t\t".join(it))
			flag = 1
			break
	if flag == 0:
		print("IP not found for the given MAC",mac)
			
if __name__ == "__main__":
	ip = input("ARP(Address Resolution Protocol)\nInput the IP ADDRESS to Return the MAC ADDRESS\n")
	ARP(ip)
	mac = input("RARP(Reverse Address Resolution Protocol)\nInput the MAC ADDRESS to Return the IP ADDRESS\n")
	RARP(mac)
