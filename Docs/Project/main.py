import socket
import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # print(dict(self.headers.items()))
        a = json.dumps({
            'method': self.command,
            'path': self.path,
            'headers': dict(self.headers.items())
        })
        # print('----------------------------------------------')
        # print(a)
        # print('----------------------------------------------')

        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(a, 'utf-8'))

    def do_POST(self):
        try:
            content_lenght = int(self.headers['content-length'])
            body = self.rfile.read(content_lenght).decode("utf-8")
            print(body)
            a = json.dumps({
                'method': self.command,
                'path': self.path,
                'headers': dict(self.headers.items()),
                'body': json.loads(body)
            })
            # print('----------------------------------------------')
            # print(a)
            # print('----------------------------------------------')

            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(a, 'utf-8'))
        except json.decoder.JSONDecodeError:
            print('JSON error')

    def do_PUT(self):
        # print('----------------------------------------------')
        print(self.path)
        # print('----------------------------------------------')
        self.send_response(200)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_adress = (socket.gethostbyname(socket.gethostname()), 8888)
    httpd = server_class(server_adress, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


run()
