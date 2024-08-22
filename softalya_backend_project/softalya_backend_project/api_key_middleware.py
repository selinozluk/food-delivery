from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class APIKeyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI, api_key: str):
        super().__init__(app)
        self.api_key = api_key

    async def dispatch(self, request: Request, call_next):
        if 'x-softalya-api-key' not in request.headers:
            raise HTTPException(status_code=403, detail="No API Key provided")

        api_key_header = request.headers['x-softalya-api-key']
        if api_key_header != self.api_key:
            raise HTTPException(status_code=403, detail="Invalid API Key")

        response = await call_next(request)
        return response
