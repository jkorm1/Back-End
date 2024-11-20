from sqlalchemy import Column, String, JSON
from .database import Base

class Card(Base):
    __tablename__ = "cards"

    user_id = Column(String, primary_key=True, index=True)
    containers = Column(JSON)
    location = Column(String)
    order_type = Column(String)
