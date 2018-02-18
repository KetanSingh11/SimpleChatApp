import socket

SERVER = "127.0.0.1"
PORT = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client", 'UTF-8'))
while True:
    in_data = client.recv(1024)
    print("Response From Server: ", in_data.decode())
    out_data = input()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'q':
        break
client.close()
