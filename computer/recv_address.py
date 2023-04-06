import socket
import os

if __name__ == "__main__":
    SERVER_ADDRESS = "INPUT_ADDRESS_CHANGE" # computer ip goes here
    PORT = INPUT_PORT_CHANGE # cloud server tcp out goes here
    NUM_CONNECTIONS = 1
    BUFF_SIZE = 100
    DIRECTORY = "ip_address"
    FILENAME = "jetson_address.txt"
    FILE_PATH = os.path.join(DIRECTORY,FILENAME)
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    sock.bind((SERVER_ADDRESS,PORT))
    sock.listen(NUM_CONNECTIONS)
    
    client_socket,client_address = sock.accept()
    print(f"Connected to {client_socket} on address {client_address}.")
    address = client_socket.recv(BUFF_SIZE)
    
    with open(FILE_PATH,"wb") as f:
        f.write(address)
        print(f"Receibed {address.decode()} was written to {FILE_PATH}")
    client_socket.close()
    sock.close()
