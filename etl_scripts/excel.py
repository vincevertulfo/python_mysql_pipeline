import pandas as pd 
import os
import xlrd

from .reference import *

FILE_PATH = '../data'
info_type = 'brand'

def consolidate_excel(FILE_PATH, info_type):
  '''
    Returns the cleaned dataframe for events and brands

    Paremeters
    ----------
    FILE_PATH : str
      The folder path containing the raw Excel files to be consolidated
    info_type : str
      'event' for event data and 'brand' for brand data

    Returns
    ----------
    main_df : dataframe
      Output dataframe with all Excel files consolidated

  '''

  column_mapper = excel_event_columns if info_type == 'event' else excel_brand_columns
  sheet_name = 'Event Info Form' if info_type == 'event' else 'Brand Audit Form'

  i = 1
  dfs = []
  no_brand_audit = []
  for file in os.listdir(FILE_PATH):

    try:
      df = pd.read_excel(f'{FILE_PATH}/{file}', sheet_name = sheet_name)
    except xlrd.biffh.XLRDError as e:
      print(f"No sheet named <Brand Audit Form> for {file}")
      no_brand_audit.append(file)

    if info_type == 'event':
      df = df.transpose().reset_index()
      header = df.iloc[0]
      df = df[1:2]
      df.columns = header
    else:
      df
    df = df.dropna(how='all') 
    df['File Name'] = str(file)
    df['Submission Type'] = 'Excel Template 2020'
    df['Submission Id'] = i
    dfs.append(df)

    i+=1

  main_df = pd.concat(dfs)
  main_df = main_df.rename(columns=column_mapper)
  main_df = main_df[[val for key,val in column_mapper.items()]]
  main_df = main_df.reset_index(drop=True)

  return main_df
