import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/files':
            # Directory containing your HTML files
            directory = 'downloaded_html'
            # List HTML files
            files = [f for f in os.listdir(directory) if f.endswith('.html')]
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
        else:
            super().do_GET()


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
