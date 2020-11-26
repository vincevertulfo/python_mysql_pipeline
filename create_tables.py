import pandas as pd 
from sqlalchemy import Column, Float, Integer, String, DateTime, Boolean, Text, ForeignKeyConstraint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

from utilities import *

host, user, password, db, port = get_db_credentials()

engine = create_engine(f'mysql+mysqlconnector://{host}:{password}@{host}:{port}/{db}',
                      pool_recycle=int(port), echo=True) # echo=True is to show the SQL statements

Base = declarative_base()

class EventStaging(Base):
  __tablename__ = 'events_staging'
  __table_args__ = {'schema': 'bffp_practice'}

  file_name = Column(Text)
  submission_type = Column(String(200), primary_key=True)
  submission_id = Column(Integer, primary_key=True)
  first_name = Column(Text)
  last_name = Column(Text)
  name_of_lead = Column(Text)
  is_trained = Column(Text)
  organization = Column(Text)
  email = Column(Text)
  phone = Column(Text)
  volunteer = Column(Text)
  start_of_audit = Column(Text)
  end_of_audit = Column(Text)
  time_spent = Column(Text)
  city = Column(Text)
  province = Column(Text)
  country = Column(Text)
  continent = Column(Text)
  type_audit = Column(Text)
  specifics_audit = Column(Text)
  total_count = Column(Text)

  brands_staging = relationship('BrandStaging', backref='eventstaging')

  def __repr__(self):
    return f'''<EventStaging(file_name={self.file_name}, submission_type={self.submission_type},
        submission_id={self.submission_id}, first_name={self.first_name}, last_name={self.last_name},
        name_of_lead={self.name_of_lead}, is_trained={self.is_trained}, organization={self.organization},
        email={self.email}, phone={self.phone}, volunteer={self.volunteer}, start_of_audit={self.start_of_audit},
        end_of_audit={self.end_of_audit}, time_spent={self.time_spent}, city={self.city}, province={self.province},
        country={self.country}, continent={self.continent}, type_audit={self.type_audit}, specifics_audit={self.specifics_audit},
        total_count={self.total_count})>
    '''

class BrandStaging(Base):
  __tablename__ = 'brands_staging'

  row_id = Column(Integer, primary_key=True)
  submission_type = Column(String(200))
  submission_id = Column(Integer)
  brand_name = Column(Text)
  parent_company = Column(Text)
  item_description = Column(Text)
  type_product = Column(Text)
  type_material = Column(Text)
  layer = Column(Text)
  total_count = Column(Text)

  event = relationship('EventStaging')

  __table_args__ = (
      ForeignKeyConstraint([submission_type, submission_id],
                          [EventStaging.submission_type, EventStaging.submission_id]),
      {'schema' : 'bffp_practice'}
  )

  def __repr__(self):
    return f'''<BrandStaging(submission_type={self.submission_type}, submission_id={self.submission_id}, 
        brand_name={self.brand_name}, parent_company={self.parent_company}, 
        item_description={self.item_description}, type_product={self.type_product}, 
        type_material={self.type_material}, layer={self.layer}, total_count={self.total_count})>
    '''

Base.metadata.drop_all(bind=engine)   #Drops all the tables in the database
Base.metadata.create_all(bind=engine) #Creates all the tables in the database


# session = sessionmaker()
# session.configure(bind=engine)
# s = session()
