import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer


class MyHandler(SimpleHTTPRequestHandler):
    """
    A custom HTTP request handler that serves static files and provides a list
    of HTML files from a specific directory.

    Inherits from :class:`http.server.SimpleHTTPRequestHandler`.

    Methods
    -------
    do_GET():
        Handles GET requests. If the path is `/files`, it returns a JSON list of
        HTML files from the `downloaded_html` directory. For all other paths, it
        behaves like a normal HTTP server.
    """

    def do_GET(self):
        """
        Handle GET requests.

        If the requested path is `/files`, it lists all HTML files in the
        `downloaded_html` directory and sends them as a JSON response.
        For other paths, it falls back to the default behavior of 
        :class:`SimpleHTTPRequestHandler`.
        """
        if self.path == '/files':
            directory = 'downloaded_html'
            files = [f for f in os.listdir(directory) if f.endswith('.html')]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode())
        else:
            super().do_GET()


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    """
    Runs the HTTP server on the specified port.

    :param server_class: The class to use for the HTTP server, defaults to `HTTPServer`.
    :type server_class: type, optional
    :param handler_class: The request handler class to use, defaults to `MyHandler`.
    :type handler_class: type, optional
    :param port: The port number on which the server will listen, defaults to 8000.
    :type port: int, optional
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Serving on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
