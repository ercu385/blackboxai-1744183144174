from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Farmer(Base):
    __tablename__ = 'farmers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True)
    email = Column(String(100), unique=True)
    password_hash = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    fields = relationship("Field", back_populates="farmer")

class Field(Base):
    __tablename__ = 'fields'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255))
    area = Column(Float)  # dönüm/hektar
    soil_type = Column(String(50))
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    
    farmer = relationship("Farmer", back_populates="fields")
    crops = relationship("Crop", back_populates="field")

class Crop(Base):
    __tablename__ = 'crops'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(50))  # buğday, mısır vb.
    planting_date = Column(DateTime)
    harvest_date = Column(DateTime)
    field_id = Column(Integer, ForeignKey('fields.id'))
    
    field = relationship("Field", back_populates="crops")
    irrigations = relationship("Irrigation", back_populates="crop")

class Irrigation(Base):
    __tablename__ = 'irrigations'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    amount = Column(Float)  # m3
    method = Column(String(50))  # damla, yağmurlama vb.
    crop_id = Column(Integer, ForeignKey('crops.id'))
    
    crop = relationship("Crop", back_populates="irrigations")
