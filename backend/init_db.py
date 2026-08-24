from database import engine, Base
from models import Project

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")