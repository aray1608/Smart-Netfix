# from fastapi import FastAPI
# from backend.routers import diagnostics
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Allow requests from Streamlit
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # You can restrict this to ["http://localhost:8501"] if preferred
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(diagnostics.router, prefix="/api/v1/diagnostics")

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