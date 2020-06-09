from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy import Index
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#Schema for Fuelly Log Data being entered into database.
class fuelog(base):
    __tablename__ = 'fuellog'
    id = Column(Integer, primary_key=True)
    user = Column(String(250))
    year = Column(Integer(4))
    make = Column(String(250))
    model = Column(Float(5))

#Schema for gasprices that are webscraped.
class gasprice(base):
    __tablename__ = 'gasprices'
    id = Column(Integer, primary_key=True)
    current_gas_price = Column(String(250))
	regular_gas(85) = Column(Float(250))
	mid_grade_gas(89) = Column(Float(250))
    premium_grade_gas(93) = Column(Float(250))
    diesel_gas = Column(Float(250))