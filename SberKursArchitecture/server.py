from http.server import HTTPServer, CGIHTTPRequestHandler


if __name__ == "__main__":
    server_address = ("", 8090)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    print('HTTP server started on localhost:8090')
    httpd.serve_forever()
