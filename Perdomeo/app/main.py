from fastapi import FastAPI
from app.api import conference_routes, speaker_routes
from app.db.database import Base, engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create database tables
Base.metadata.create_all(bind=engine)

# Application metadata
APP_NAME = os.getenv("APP_NAME", "Conference API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "development")

# Initialize FastAPI app
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="API for managing conferences and speakers.",
    contact={
        "name": "Developer Team",
        "url": "https://github.com/your-repository",
    },
    root_path="/api",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,
        "persistAuthorization": True,
    },
)

# Include API routers
app.include_router(conference_routes.router, prefix="/v1/conferences")
app.include_router(speaker_routes.router, prefix="/v1/speakers")
