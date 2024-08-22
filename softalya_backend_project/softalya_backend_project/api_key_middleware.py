from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class APIKeyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, api_key: str):
        super().__init__(app)
        self.api_key = api_key

    async def dispatch(self, request: Request, call_next):
        if 'Authorization' not in request.headers:
            raise HTTPException(status_code=403, detail="No API Key provided")

        auth_header = request.headers['Authorization']
        if auth_header != f"Bearer {self.api_key}":
            raise HTTPException(status_code=403, detail="Invalid API Key")

        response = await call_next(request)
        return response
