from icmplib import ping, traceroute

#ping(address, count, interval, timeout, id)
#using ping to send ICMP_ECHO packets to a network host
#return host object with address, min_rtt, avg_rtt, max_rtt, packets_sent, packets_received, packet_loss, is_alive.

def ping_ip():
    ip = input("Enter website or IP: ")
    count = int(input("No. times to ping: "))
    intvl = float(input("Time interval for each packet: "))
    host = ping(ip, count, intvl)
    return host #host object with RTTs packet details are sent
#traceroute(address, count=3, interval=0.05, timeout=2, id=PID, traffic_class=0, max_hops=30, fast_mode=False, **kwargs)

def traceroute_ip(timeout=1,fast_mode=True):
    ip = input("Enter website or IP: ")
    hops = traceroute(ip, timeout=1)
    print('Distance(ttl)\t\tAddress\t\tAverage round-trip time')
    last_distance = 0
    for hop in hops:
        if last_distance + 1 != hop.distance:
            print(f'servers not responding')

        print(f'{hop.distance}\t\t{hop.address}\t\t{hop.avg_rtt} ms')
        last_distance = hop.distance
    
if __name__ == "__main__":
    ch = 0
    while ch<=3:
        ch = int(input("1. Ping\n2. Traceroute\n"))
        if ch == 1:
            host = ping_ip()
            print(f'Address: {host.address} min_rtt: {host.min_rtt} max_rtt:{host.max_rtt} avg_rtt:{host.avg_rtt}')
            print(f'packets: sent={host.packets_sent} received={host.packets_received} loss={host.packet_loss}')
        elif ch == 2:
            traceroute_ip()
        else:
            break
    
    print("exit")
