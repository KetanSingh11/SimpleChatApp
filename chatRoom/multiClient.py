import socket
import select
import sys

HOST = "127.0.0.1"
PORT = 5000


def sock_send(sock):
    while True:
        message = sys.stdin.readline()
        sock.sendall(message.encode("utf-8"))

def sock_recv(sock):
    pass


def Main():
    clientName = input("Enter your name: ")
    print("Hello {}! Welcome to Chat Room.".format(clientName))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    message = input("{}: ".format(clientName)).encode("utf-8")
    while message != "q":
        # socket_list = [sys.stdin, s]
        # read_socket, write_socket, error_socket = select.select(socket_list, [], [], 0)
        # print(read_socket)
        # for socks in read_socket:
        #     if socks == s:
        #         reply = s.recv(1024).decode("utf-8")
        #         print(reply)
        #     else:
        #         print("{}: ".format(clientName))
        #         message = sys.stdin.readline()
        #         s.sendall(message.encode("utf-8"))

        s.sendall(message)
        data = s.recv(1024).decode('utf-8')
        print("Recieved: " + data)
        message = input("{}: ".format(clientName)).encode("utf-8")

    print("Closing Client...BYE!")
    s.close()


if __name__ == "__main__":
    Main()