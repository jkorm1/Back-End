from .database import Base, engine
from .models import Card

Base.metadata.create_all(bind=engine)
