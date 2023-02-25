from sqlalchemy import Column, Integer, String
from ..config import Base
 
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    image = Column(String)
