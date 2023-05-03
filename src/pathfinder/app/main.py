from fastapi import FastAPI, Depends

from .routers import api_tokens
from app.dependencies.lease_manager import get_lease_manager

lease_manager = get_lease_manager

app = FastAPI()

app.include_router(api_tokens.router, dependencies=[Depends(lease_manager)])
