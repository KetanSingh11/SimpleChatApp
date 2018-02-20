import socket

def Main():
    host = "127.0.0.1"
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()

    print("Started Server...")
    print("Ready to recieve messages!!")

    # establish the connection
    #c, addr = s.accept()
    #print("Connection from : " + str(addr) + "\n")


    while True:
        c, addr = s.accept()
        data = c.recv(1024).decode('utf-8')
        if not data:
            break

        print("Received: " + data)
        data = data.upper()
        print("Sending:  " + str(data) + "\n")
        c.send(data.encode('utf-8'))


    print("Shutdown Server...")
    c.close()



if __name__ == "__main__":
    Main()