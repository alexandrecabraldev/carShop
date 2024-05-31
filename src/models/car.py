import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import URLType
from models import Base

class Car(Base):
    __tablename__= 'cars'
    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name=Column(String(50), nullable=False)
    brand=Column(String(50), nullable=False)
    model=Column(String(50), nullable=False)
    price=Column(String(50), nullable=False)
    image_url=Column(URLType, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "brand": self.brand,
            "model": self.model,
            "price":self.price,
            "image_url": self.image_url
        }
    
    def __repr__(self):
        return f"id={self.id}, name={self.name}, brand={self.brand}, model={self.model},price={self.price} image_url={self.image_url}"