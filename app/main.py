from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import beach_routes
from app.database.connection import engine, Base

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(
    beach_routes.router, 
    prefix="/beaches",
    tags=["Beaches"]
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Beach Monitoring API"}
