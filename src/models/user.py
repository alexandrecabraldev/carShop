import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from models import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    role = Column(String(50), default='customer')