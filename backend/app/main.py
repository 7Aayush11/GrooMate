from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.rate_limit import limiter
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI(title="GrooMate Backend")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(api_router, prefix="/api/v1")