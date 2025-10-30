from a2wsgi import ASGIMiddleware

from app.main import app


wsgi_app = ASGIMiddleware(app)