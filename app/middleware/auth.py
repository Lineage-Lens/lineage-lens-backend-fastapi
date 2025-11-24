import httpx
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, client_id: str):
        super().__init__(app)
        self.client_id = client_id
    
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS":
            return await call_next(request)
    
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return self.create_unauthorized()
        
        auth = auth.replace("Bearer ", "", 1)
        
        async with httpx.AsyncClient() as client:
            r = await client.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={auth}")
            
        if r.status_code != 200:
            return self.create_unauthorized()
        
        try:
            data = r.json()
        except Exception:
            return self.create_unauthorized()

        if data.get("aud") != self.client_id:
            return self.create_unauthorized()

        return await call_next(request)
    
    def create_unauthorized(self) -> JSONResponse:
        return JSONResponse({"detail": "Unauthorized"}, status_code=401)