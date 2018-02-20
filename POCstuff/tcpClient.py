import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Connected to server: ")
    message = input("(q to quit) --> ")

    while message != "q":
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print("Recieved: " + data)
        message = input("(q to quit) --> ")

    print("Closing Client...")
    s.close()


if __name__ == "__main__":
    Main()