
# Excel Template Column Mapper -> Events
excel_event_columns = {
  'File Name':                              'file_name',
  'Submission Type':                        'submission_type', 
  'Submission Id':                          'submission_id',
  'First Name':                             'first_name',
  'Last Name':                              'last_name',
  'Name of Lead':                           'name_of_lead',
  'Leader Participated in BFFP Training?':  'is_trained',
  'Organization':                           'organization',
  'Email':                                  'email',
  'Phone':                                  'phone',
  'Number of Volunteers':                   'volunteer',
  'Start Of Audit (dd/mm/yyyy)':            'start_of_audit',
  'End Of Audit (dd/mm/yyyy)':              'end_of_audit',
  'Average Time Spent/day (hrs)':           'time_spent',
  'City':                                   'city',
  'Province/State/Region':                  'province',
  'Country':                                'country',
  'Continent':                              'continent',
  'Type of Audit':                          'type_audit',
  'Specifics of Audit':                     'specifics_audit',
  'Total Count':                            'total_count'
}

# Excel Template Column Mapper -> Brand
excel_brand_columns = {
  'Submission Type':                        'submission_type', 
  'Submission Id':                          'submission_id',
  'BrandName':                              'brand_name',
  'Parent Company':                         'parent_company',
  'ItemDescription':                        'item_description',
  'TypeProduct':                            'type_product',
  'TypeMaterial':                           'type_material',
  'Layers':                                 'layer',     
  'Total Count':                            'total_count'
}

# 123 Forms columns to be used
online_form_use_cols = [
  'Name of Lead',
  'Email',
  'Participated in a BFFP Training?',
  'Phone',
  'Start of Audit',
  'Organization',
  'End of Audit',
  'Number of Volunteers:',
  'Average Time Spent/day (hrs)',
  'City',
  'Province/State/Region',
  'Country-Country',
  'Type of Audit',
  'Specifics of Audit',
  'Short text',
  'Long text',
  'Single choice',
  'Copy of Single choice',
  'Copy of Copy of Single choice',
  'Number',
  'Copy of Short text',
  'Copy of Long text',
  'Copy of Single choice2',
  'Copy of Copy of Single choice3',
  'Copy of Copy of Copy of Single choice',
  'Copy of Number',
  'Entry ID'
]

# 123 Forms Column Mapper -> Event
online_form_event_columns = {
  'File Name':                              'file_name',
  'Submission Type':                        'submission_type',
  'Entry ID':                               'submission_id',
  'First Name':                             'first_name',
  "Last Name":                              'last_name',
  'Name of Lead':                           'name_of_lead',
  'Participated in a BFFP Training?':       'is_trained',
  'Organization':                           'organization',
  'Email':                                  'email',
  'Phone':                                  'phone',
  'Number of Volunteers:':                  'volunteer',
  'Start of Audit':                         'start_of_audit',
  'End of Audit':                           'end_of_audit',
  'Average Time Spent/day (hrs)':           'time_spent',
  'City':                                   'city',
  'Province/State/Region':                  'province',
  'Country-Country':                        'country',
  'Continent':                              'continent',
  'Type of Audit':                          'type_audit',
  'Specifics of Audit':                     'specifics_audit',
  'Number':                                 'total_count'
}


# 123 Form Column Mapper -> Brand
online_form_brand_columns = {
  'Submission Type':                        'submission_type', 
  'Entry ID':                               'submission_id',
  'Short text':                             'brand_name',
  'Parent Company':                         'parent_company',
  'Long text':                              'item_description',
  'Single choice':                          'type_product',
  'Copy of Single choice':                  'type_material',
  'Copy of Copy of Single choice':          'layer',     
  'Number':                                 'total_count'
}

# 123 Form Column Mapper -> Brand v2
online_form_brand_columns_v2 = {
  'Submission Type':                        'submission_type', 
  'Entry ID':                               'submission_id',
  'Copy of Short text':                     'brand_name',
  'Parent Company':                         'parent_company',
  'Copy of Long text':                      'item_description',
  'Copy of Single choice2':                 'type_product',
  'Copy of Copy of Single choice3':         'type_material',
  'Copy of Copy of Copy of Single choice':  'layer',     
  'Copy of Number':                         'total_count'
}


# Trashblitz columns to be used
trashblitz_use_cols = [
  'Session ID',
  'User Name',
  'User Email',
  'User Training Completed',
  'User Phone',
  'When',
  'Organization',
  'Completed At',
  'Group Size',
  'City',
  'State',
  'Country',
  'Is Outdoor?',
  'Where',
  'Brand',
  'Trash Item Description',
  'Trash Category',
  'Pickup Material',
  'Material Layers',
  'Trash Weight'
]

# Trashblitz Column Mapper -> Event
trashblitz_event_columns = {
  'File Name':                              'file_name',
  'Submission Type':                        'submission_type',
  'Session ID':                             'submission_id',
  'First Name':                             'first_name',
  'Last Name':                              'last_name',
  'User Name':                              'name_of_lead',
  'User Training Completed':                'is_trained',
  'Organization':                           'organization',
  'User Email':                             'email',
  'User Phone':                             'phone',
  'Group Size':                             'volunteer',
  'When':                                   'start_of_audit',
  'Completed At':                           'end_of_audit',
  'Time spent':                             'time_spent',
  'City':                                   'city',
  'State':                                  'province',
  'Country':                                'country',
  'Continent':                              'continent',
  'Is Outdoor?':                            'type_audit',
  'Where':                                  'specifics_audit',
  'Trash Weight':                           'total_count'
}


# Trashblitz Column Mapper -> Brand
trashblitz_brand_columns = {
  'Submission Type':                        'submission_type', 
  'Session ID':                             'submission_id',
  'Brand':                                  'brand_name',
  'Parent Company':                         'parent_company',
  'Trash Item Description':                 'item_description',
  'Trash Category':                         'type_product',
  'Pickup Material':                        'type_material',
  'Material Layers':                        'layer',     
  'Trash Weight':                           'total_count'
}
