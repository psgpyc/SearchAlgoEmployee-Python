from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler,HTTPServer
from webserver import DictParse


class WebserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        try:
                query = urlparse(self.path).query
                print(query)
                query_components = dict(q.split("=") for q in query.split("&"))
                print(query_components)
                l= DictParse.Dict_parse(query_components)

                print(l)




                self.send_response(200)
                self.send_header("content-type","application/json")
                self.end_headers()
                self.wfile.write(l.encode())

        except IOError:
            print(IOError)
def main():

    try:
        port = 8000
        server = HTTPServer(('', port), WebserverHandler)

        print("Web Server is running on {}.....".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print(f"^C entered! closing the sever")
        server.socket.close()
        print(KeyboardInterrupt)

def fetch(val):
    pass




if __name__ == '__main__':
    main()
