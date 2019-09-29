#!/usr/bin/env python3

# This module serves js, css, html, and image files
# This module also accepts a POST request with input text
# and a character name, returning that character's speech

import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
 
from translator import translate

 
class StaticServer(BaseHTTPRequestHandler):
 
    def do_GET(self):
        root = os.getcwd()
        if self.path == '/':
            filename = root + '/index.html'
        else:
            filename = root + self.path
 
        self.send_response(200)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        elif filename[-5:] == '.json':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-3:] == '.js':
            self.send_header('Content-type', 'application/javascript')
        elif filename[-4:] == '.ico':
            self.send_header('Content-type', 'image/x-icon')
        elif filename[-5:] == '.jpeg' or filename[-4:] in ['jpg', 'png']:
            self.send_header('Content-type', 'image/x-icon')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fh:
            data = fh.read()
            self.wfile.write(data)


    def do_POST(self):
        content_len = int(dict(self.headers._headers)['Content-Length'])
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()
        json_obj = json.loads(post_body)
        print("received posted data = character %s, text '%s'" % (json_obj['character'], json_obj['text']))
        updated_txt = translate(json_obj['character'], json_obj['text'])
        print("sending updated text: %s" % updated_txt)
        self.wfile.write(updated_txt.encode())
        return

 
def run(server_class=HTTPServer, handler_class=StaticServer, port=47290):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd on port {}'.format(port))
    httpd.serve_forever()
 

if __name__ == '__main__':
    run()

