import pandas as pd 
from dotenv import load_dotenv

from etl_scripts.excel import *

host, user, password, db, port = get_db_credentials()

engine = create_engine(f'mysql+mysqlconnector://{host}:{password}@{host}:{port}/{db}',
                pool_recycle=3306, echo=True) # echo=True is to show the SQL statements

_EXCEL_FILE_PATH = 'data/Excel 2020'
_123Forms_FILE_PATH = 'data/123Forms 2020'
_TRASHBLITZ_FILE_PATH = 'data/TrashBlitz 2020'

def load_excel_to_db():

  event_df = consolidate_excel(_EXCEL_FILE_PATH, info_type='event')
  brand_df = consolidate_excel(_EXCEL_FILE_PATH, info_type='brand')

  event_df.to_sql(con=engine, name=EventStaging.__tablename__, if_exists='append', index=False)
  brand_df.to_sql(con=engine, name=BrandStaging.__tablename__, if_exists='append', index=False)

def load_123_forms_to_db():

  pass

def load_trashblitz_to_db():
  pass


if __name__ == '__main__':

  load_excel_to_db()
  load_123_forms_to_db()
  load_trashblitz_to_db()


