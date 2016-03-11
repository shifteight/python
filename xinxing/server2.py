import socketserver as ss

class XinHandler(ss.StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Client address:', addr)
        self.wfile.write(b'This is xinxing')
        msg = self.rfile.read(1024)
        print('Client sending msg:', msg)

host = ''
port = 8088
server = ss.TCPServer((host, port), XinHandler)

server.serve_forever()
