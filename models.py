from sqlalchemy import Column, String, JSON
from database import Base

class Postback(Base):
    __tablename__ = "postbacks"

    hash_id = Column(String, primary_key=True, index=True)
    data = Column(JSON)
