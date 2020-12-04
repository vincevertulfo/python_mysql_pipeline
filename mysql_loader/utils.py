import pandas as pd 
import os,sys
import mysql.connector
sys.path.append('..')

import config


def pd_to_mysql(df, uri_components, table_name, tmpfile='mysql.csv', sep=',', newline='\n'):
    '''
    Load dataframe into a sql table using native mysql LOAD DATA LOCAL INFILE.

    Parameters
    ---------
    df : dataframe 
        pandas dataframe
    uri : list 
        list of mysql mysqlconnector sqlalchemy database uri components
    table_name : str 
        table to store data in
    tmpfile : str 
        filename for temporary file to load from
    sep : str 
        separator for temp file, eg ',' or '\t'

    Returns
    ---------
    bool: boolean
        True if loader finished
    '''
    table_name = table_name.lower()

    connection = mysql.connector.connect(user=uri_components[0],
                                    password=uri_components[1],
                                    host=uri_components[2],
                                    database=uri_components[3],
                                    allow_local_infile=True)
    cursor = connection.cursor()

    
    df.to_csv(tmpfile, na_rep="\\N", index=False)
    print(f'CREATED {tmpfile} SUCCESSFULLY!')

    if table_name == config.EVENT_STAGING_TABLE_NAME:
        sql_load = '''
            LOAD DATA LOCAL INFILE '{}' 
            INTO TABLE {} 
            FIELDS TERMINATED BY '{}' 
            ENCLOSED BY '"' 
            LINES TERMINATED BY '{}' 
            IGNORE 1 LINES;
        '''.format(tmpfile, table_name, sep, newline)
    else:
        sql_load = '''
            LOAD DATA LOCAL INFILE '{}' 
            INTO TABLE {} 
            FIELDS TERMINATED BY '{}' 
            ENCLOSED BY '"' 
            LINES TERMINATED BY '{}' 
            IGNORE 1 LINES
            (submission_type, submission_id, brand_name, parent_company, item_description, type_product, type_material, layer, total_count);
        '''.format(tmpfile, table_name, sep, newline)
    cursor.execute(sql_load)
    connection.commit()
    print(f'LOADING {tmpfile} SUCCESSFULLY!')

    os.remove(tmpfile)

    return True

