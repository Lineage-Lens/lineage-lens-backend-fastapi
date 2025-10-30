from wsgiref.simple_server import make_server

from config import settings
from wsgi import wsgi_app


if __name__=="__main__":
    with make_server("localhost", settings.port, wsgi_app) as httpd:
        print(f"Serving on port {settings.port}")
        httpd.serve_forever()