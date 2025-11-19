from fastapi import FastAPI
from pydantic import BaseModel

from starlette.middleware.base import BaseHTTPMiddleware

import logging
app = FastAPI(
    title="MBC AI Study",
    description="MBC AI Study",
    version="0.0.1",
    docs_url=None, # http://localhost:8001/docs # 보안상 none 처리
    redoc_url=None, # http://localhost:8001/docs

)   # java -> new FastAPI();

class LoggingMiddleware(BaseHTTPMiddleware):
    logging.basicConfig(level=logging.INFO)
    async def dispatch(self, request, call_next):
        logging.info(f"Req: {request.method}{request.url}")
        response = await call_next(request)
        logging.info(f"Status Code : {response.status_code}")
        return response
    app.add_middleware(LoggingMiddleware)

    class Item(BaseModel):