import subprocess
from subprocess import PIPE,Popen
import socket
import time

def retrieve_ip_address(net_interface = "wlp2s0"):
    ps_1 = Popen(["ip", "a"], stdout=PIPE)
    ps_2 = Popen(["grep","-C","2",net_interface],stdin=ps_1.stdout, stdout=PIPE)
    ps_3  = Popen(["grep","inet"],stdin=ps_2.stdout, stdout=PIPE)
    out, err = ps_3.communicate()
    ip_address = out.decode("utf-8").strip().split()[1].split("/")[0]
    return ip_address


if __name__ == "__main__":
    SERVER_ADDRESS = "INPUT_ADDRESS_CHANGE" # cloud server ip goes here
    PORT = INPUT_PORT_CHANGE # cloud server tcp in goes here
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.connect((SERVER_ADDRESS,PORT))
    count = 0
    try:
        while count < 120: # transmition for two minutes
            ip_address = retrieve_ip_address()
            sock.send(ip_address.encode())
            time.sleep(1)
            count += 1
        sock.close()
    except:
        sock.close()