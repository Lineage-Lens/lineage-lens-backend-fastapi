from a2wsgi import ASGIMiddleware

from app import app


wsgi_app = ASGIMiddleware(app)