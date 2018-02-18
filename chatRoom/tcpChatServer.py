import socket
import threading

def clientThread(connsock, addr):
    #c, addr = conn.accept()
    client_addr = "{}:{}".format(addr[0], addr[1])
    print("Connection from:- {}::{}".format(threading.currentThread().getName(), client_addr))
    while True:
        data = connsock.recv(1024).decode('utf-8')
        if not data:
            break
        print("{}: {}".format(threading.currentThread().getName(), data))

    print("Client at {}: disconnected.".format(client_addr))
    connsock.close()


def Main(no_of_clients):
    print("Listening...")
    HOST = "127.0.0.1"
    PORT = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()

    client_threads = []
    #do this to auto close server when max client has reached and have disconnected
    for i in range(no_of_clients):
        connsock, addr = s.accept()
        t = threading.Thread(name="##{}".format(i), target=clientThread, args=(connsock, addr))
        t.start()
        client_threads.append(t)

    for x in client_threads:
        x.join()

    print("\nShutting Down Server... Bye!")
    s.close()

if __name__ == "__main__":
    print("Starting tcpChatServer !!")
    Main(list(map(int, input("Enter # of clients: ").split()))[0])