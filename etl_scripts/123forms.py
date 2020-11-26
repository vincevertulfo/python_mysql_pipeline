import pandas as pd 
import os

from reference import *

FILE_PATH = '../data/123Forms 2020'
info_type = 'event'

def consolidate_123forms(FILE_PATH, info_type):

  column_mapper = online_form_event_columns if info_type == 'event' else online_form_brand_columns
  use_cols = online_form_use_cols
  dfs = []
  for file in os.listdir(FILE_PATH):
    print(file)
    df = pd.read_excel(f"{FILE_PATH}/{file}", usecols = online_form_use_cols)
    df = df.dropna(subset=['Name of Lead'])

    print(df.head())


consolidate_123forms(FILE_PATH, info_type='event' )
