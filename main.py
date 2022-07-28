from typing import Optional

from fastapi import FastAPI
import api

app = FastAPI(title="Video",version="0.1.0")

app.include_router(api.router, prefix="/api", tags=["api"])