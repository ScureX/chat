import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('0.0.0.0', 10000))

sock.listen(1)

connections = []

def handler(c, a):
    while True:
        global connections
        data = c.recv(1024)
        for connectiom in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

while True:
    c, a = sock.accept()
    cTread = threading.Thread(targethandler, args=(c, a))
    cTread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)
