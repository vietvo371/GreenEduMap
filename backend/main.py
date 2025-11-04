"""GreenEduMap FastAPI Application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import api_router
from app.db.base import Base, engine

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "GreenEduMap API",
        "version": settings.app_version,
        "docs": "/docs",
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.on_event("startup")
async def startup_event():
    """Startup event handler."""
    print("🚀 GreenEduMap API starting...")
    # Create all database tables
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created/verified")

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler."""
    print("👋 GreenEduMap API shutting down...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )
