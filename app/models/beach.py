from sqlalchemy import Column, Integer, String, Float
from app.database.connection import Base

class Beach(Base):
    __tablename__ = "beaches"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    temperature = Column(Float)
    wave_height = Column(Float)
    crowd_level = Column(String)
    safety_flag = Column(String)
    timestamp = Column(String)
    regions = Column(String)  
    image_url = Column(String, nullable=True)  # Optional field for image URL
    
