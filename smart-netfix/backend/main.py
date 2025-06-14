from fastapi import FastAPI
from backend.routers import diagnostics, auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for Streamlit or CLI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include router with full prefix path
app.include_router(diagnostics.router, prefix="/api/v1/diagnostics")
app.include_router(auth_router.router) 
