import socket

def Main():
    HOST = "127.0.0.1"
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    print("Client Started.\nStart chatting...\n")
    message = input("--> ")
    while message != "q":
        s.send(message.encode("utf-8"))
        message = input("--> ")

    print("Closing Client...")
    s.close()

if __name__ == "__main__":
    Main()