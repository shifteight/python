import socket

s = socket.socket()
serverhost = socket.gethostname()
port = 8088
s.connect((serverhost, port))

print("Connecting...")
msg = s.recv(1024)
print("Data from server:", msg)

text = bytes("I am xinxing", "UTF-8")
s.send(text)

s.close()
