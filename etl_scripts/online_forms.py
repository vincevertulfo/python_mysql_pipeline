import pandas as pd 
import os

from .reference import online_form_event_columns, online_form_use_cols, online_form_brand_columns, online_form_brand_columns_v2 

class OnlineForm():

  def __init__(self, FILE_PATH, info_type):
    self.FILE_PATH = FILE_PATH
    self.info_type = info_type
    
  def consolidate_online_forms(self):
    '''
    Returns the cleaned dataframe for events and brands

    Paremeters
    ----------
    FILE_PATH : str
      The folder path containing the raw 123forms files to be consolidated
    info_type : str
      'event' for event data, 'brand' for brand data, 'brand_v2' for brand data version 2

    Returns
    ----------
    main_df : dataframe
      Output dataframe with 123forms consolidated
    '''

    print(f"Consolidating for 123Form's {self.info_type} data...")
    column_mapper = online_form_event_columns if self.info_type == 'event' else (online_form_brand_columns if
                    self.info_type == 'brand' else online_form_brand_columns_v2)
    dfs = []
    for file in os.listdir(self.FILE_PATH):
      df = pd.read_excel(f"{self.FILE_PATH}/{file}", usecols = online_form_use_cols)
      if self.info_type == 'event':
        df = df.dropna(subset=['Name of Lead'])
        df = self.map_name(df, name_col='Name of Lead')
        df['Continent'] = ''
      else:
        df['Entry ID'] = df['Entry ID'].ffill()
        df['Parent Company'] = ''
      df['File Name'] = str(file)
      df['Submission Type'] = '123Forms 2020'
      dfs.append(df)

    main_df = pd.concat(dfs)
    main_df = main_df.rename(columns=column_mapper)
    main_df = main_df[[val for key,val in column_mapper.items()]]
    main_df = main_df.reset_index(drop=True)

    return main_df

  @staticmethod
  def map_name(df, name_col):
      # map name to first name and last name
      df[name_col] = df[name_col].str.strip()
      df[name_col] = df[name_col].str.title()
      full_name_split = df[name_col].str.rsplit(n=1, expand=True)
      df['First Name'] = full_name_split[0]
      df['Last Name'] = full_name_split[1]

      return df