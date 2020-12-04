import pandas as pd 
import os

from .reference import trashblitz_event_columns, trashblitz_brand_columns, trashblitz_use_cols

class Trashblitz():

    def __init__(self, FILE_PATH, info_type):
        self.FILE_PATH = FILE_PATH
        self.info_type = info_type

    def consolidate_trashblitz(self):
        '''
        Returns the cleaned dataframe for events and brands

        Paremeters
        ----------
        FILE_PATH : str
            The folder path containing the raw Trashblitz files to be consolidated
        info_type : str
            'event' for event data and 'brand' for brand data

        Returns
        ----------
        main_df : dataframe
            Output dataframe with all Trashblitz files consolidated
        '''

        print(f"Consolidating for Trashblitz's {self.info_type} data...")
        column_mapper = trashblitz_event_columns if self.info_type == 'event' else trashblitz_brand_columns
        dfs = []

        for file in os.listdir(self.FILE_PATH):

            df = pd.read_excel(f'{self.FILE_PATH}/{file}', usecols = trashblitz_use_cols)
            if self.info_type == 'event':
                df = df.drop_duplicates(subset=['Session ID'], keep='first')
                df = self.map_date_columns(df, start_date='When', end_date='Completed At')
                df = self.map_name(df, name_col='User Name')
                df = self.map_audit_info(df, audit_info_col="Is Outdoor?")
                df = self.map_training(df, training_col='User Training Completed')
                df['Continent'] = ''  
            else:
                df = self.map_type_material(df, type_material_col='Pickup Material')
                df = self.map_type_product(df, type_product_col='Trash Category')
                df = self.map_layer(df, layer_col='Material Layers')
                df['Parent Company'] = ''
            df['File Name'] = str(file)
            df['Submission Type'] = 'ThirdParty 2020'
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

    @staticmethod
    def map_date_columns(df, start_date, end_date):
        df[[end_date, start_date]] = df[[end_date, start_date]].applymap(lambda x: pd.to_datetime(x))
        df['Time spent'] = round((df[end_date] - df[start_date]).dt.total_seconds()/3600,2)
        df[end_date] = df[end_date].dt.date
        df[start_date] = df[start_date].dt.date

        return df

    @staticmethod
    def map_audit_info(df, audit_info_col):
        # map audit information
        mapper = {
            1:          'Outdoor',
            0:          'Indoor',
            'False':    'Indoor',
            'True':     'Outdoor'
        }
        df[audit_info_col] = df[audit_info_col].map(mapper)

        return df

    @staticmethod
    def map_training(df, training_col):
        # maps training boolean to Yes/No values
        mapper = {
            'False': 'No',
            'True':  'Yes',
            0:       'No',
            1:       'Yes'   
        }
        df[training_col] = df[training_col].map(mapper)

        return df

    @staticmethod
    def map_type_product(df, type_product_col):
        # map type product to acronyms
        mapper = {
            'food packaging':       'FP',
            'household products':   'HP',
            'packaging materials':  'PM',
            'personal care':        'PC',
            'fishing gear':         'FG',
            'smoking materials':    'SM',
            'other':                'O'
        }
        df[type_product_col] = df[type_product_col].map(mapper)

        return df

    @staticmethod
    def map_type_material(df, type_material_col):
        # map type material to acronyms
        def map(string):
            if '#1' in string:
                return 'PET'
            elif '#2' in string:
                return 'HDPE'
            elif '#3' in string:
                return 'PVC'
            elif '#4' in string:
                return 'LDPE'
            elif '#5' in string:
                return 'PP'
            elif '#6' in string:
                return 'PS'
            elif 'Other' in string or '#7' in string or "unknown" in string:
                return 'O'

        df[type_material_col] = df[type_material_col].apply(lambda x: map(x))
        
        return df

    @staticmethod
    def map_layer(df, layer_col):
        # map layer to acronmy
        mapper = {
            'multiple': 'ML',
            'single':   'SL',
            'Unsure':   'Unsure'
        }   
        df[layer_col] = df[layer_col].map(mapper)

        return df
