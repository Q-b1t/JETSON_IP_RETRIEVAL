import subprocess
import socket
import time

def retrieve_ip_address(net_interface = "wlp2s0"):
    ps_1 = subprocess.run(["ip", "a"], check=True, capture_output=True)
    ps_2 = subprocess.run(["grep", net_interface],input=ps_1.stdout, capture_output=True)
    ps_3 = subprocess.run(["tail","-n","1"],input= ps_2.stdout,capture_output=True)
    ip_address = ps_3.stdout.decode('utf-8').strip().split()[1]
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