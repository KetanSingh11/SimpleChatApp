"""
Multithreading + broadcast
"""

import threading
import socket
import sys

HOST = "127.0.0.1"
PORT = 5000

list_of_clients = []


def clientThread(conn, addr):
    # clientName = input("Enter your name: ")
    # print("Hello {}! Welcome to Chat Room.".format(clientName))

    client_addr = "{}:{}".format(addr[0], addr[1])
    print("Connection from client:- {}:{}".format(threading.currentThread().getName(), client_addr))

    while True:
        message = conn.recv(1024).decode('utf-8')
        if not message:
            print("No Message from {}. CLOSING...".format(client_addr))
            # remove the client from list
            if conn in list_of_clients:
                list_of_clients.remove(conn)
            conn.close()
            break
        else:
            print("<{}> {}".format(client_addr, message))
            # Call broadcast to send message to all other clients, except this one
            broadcast(conn, message)


def broadcast(conn, message):
    # broadcasts message to all-but-present client
    for client in list_of_clients:
        if client != conn:
            try:
                client.send(message.decode("utf-8"))
            except:
                # if the link is broken, remove the client from list
                if conn in list_of_clients:
                    list_of_clients.remove(conn)


def Main():
    try:
        # create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print("Error creating socket: %s" % e)
        sys.exit(1)

    # Enable reuse address/port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(300)

    try:
        # Bind the socket to the port
        s.bind((HOST, PORT))
        s.listen()
    except socket.error as e:
        print("Connecton error: %s" % e)
        sys.exit(1)

    while True:
        try:
            conn, addr = s.accept()
            t = threading.Thread(target=clientThread, args=(conn, addr))
            t.start()
            t.join()
            list_of_clients.append(conn)

        except KeyboardInterrupt:
            print("Interrupted !!")
            break
        except socket.error as e:
            print("Error: %s" %e)

    print("Shutting Down Server... Bye")



if __name__ == "__main__":
    print("Starting tcpChatServer !!")
    print("Listening...")
    Main()