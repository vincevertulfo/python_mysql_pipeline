import pandas as pd 
from dotenv import load_dotenv

from etl_scripts.excel import *
from etl_scripts.online_forms import *
from etl_scripts.thirdparty import *
from utilities.utils import get_db_credentials
from mysql_loader.utils import pd_to_mysql
import config

host, user, password, db, port = get_db_credentials()
uri_comp = [user, password, host, db, port]

_EXCEL_FILE_PATH = config._EXCEL_FILE_PATH
_123Forms_FILE_PATH = config._123Forms_FILE_PATH
_THIRDPARTY_FILE_PATH = config._THIRDPARTY_FILE_PATH

def load_excel_to_db():

  event_df = consolidate_excel(_EXCEL_FILE_PATH, info_type='event')
  brand_df = consolidate_excel(_EXCEL_FILE_PATH, info_type='brand')

  pd_to_mysql(event_df, uri_components=uri_comp, table_name=config.EVENT_STAGING_TABLE_NAME)
  pd_to_mysql(brand_df, uri_components=uri_comp, table_name=config.BRAND_STAGING_TABLE_NAME)

def load_online_forms_to_db():

  event_df = OnlineForm(_123Forms_FILE_PATH, info_type='event').consolidate_online_forms()
  brand_df = OnlineForm(_123Forms_FILE_PATH, info_type='brand').consolidate_online_forms()
  brand_df_v2 = OnlineForm(_123Forms_FILE_PATH, info_type='brand').consolidate_online_forms()

  pd_to_mysql(event_df, uri_components=uri_comp, table_name=config.EVENT_STAGING_TABLE_NAME)
  pd_to_mysql(brand_df, uri_components=uri_comp, table_name=config.BRAND_STAGING_TABLE_NAME)
  pd_to_mysql(brand_df_v2, uri_components=uri_comp, table_name=config.BRAND_STAGING_TABLE_NAME)

def load_trashblitz_to_db():
  
  event_df = Trashblitz(_THIRDPARTY_FILE_PATH, info_type = 'event').consolidate_trashblitz()
  brand_df = Trashblitz(_THIRDPARTY_FILE_PATH, info_type = 'brand').consolidate_trashblitz()

  pd_to_mysql(event_df, uri_components=uri_comp, table_name=config.EVENT_STAGING_TABLE_NAME)
  pd_to_mysql(brand_df, uri_components=uri_comp, table_name=config.BRAND_STAGING_TABLE_NAME)

if __name__ == '__main__':

  os.system('python create_tables.py')
  load_excel_to_db()
  load_online_forms_to_db()
  load_trashblitz_to_db()


