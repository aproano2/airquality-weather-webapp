from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Station(Base):
    """Create a database table for stations
    """
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)

class Category(Base):
    """Create a table for the data types received from stations
    """
    ___tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    station_id = Column(Integer, ForeignKey('station.id'))
    station = relationship(Station)

class Point(Base):
    """Create a database for the datapoints
    """
    __tablename__ = 'point'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    data = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, cascade='all, delete-orphan',
                            single_parent=True)
    station_id = Column(Integer, ForeignKey('station.id'))
    station = relationship(Station)


        @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'data': self.data,
            'id': self.id,
            'cat_id': self.category_id,
            'station_id': self.station_id,
        }

engine = create_engine('sqlite:///airweather.db')

Balse.metadata.create_all(engine)
