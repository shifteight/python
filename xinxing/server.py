import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8088

s.bind((host, port))

s.listen(12)

while True:
    c, addr = s.accept()
    print(c)
    print(".........")
    print(addr)
    print("Connected.")
    cmd = bytes("I am the server", 'UTF-8')
    c.send(cmd)
    msg = c.recv(1024)
    print(msg)
