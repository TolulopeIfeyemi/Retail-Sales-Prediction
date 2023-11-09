def clean_data(data):
    data.columns = data.columns.str.lower()
    data.item_fat_content.replace({'LF': 'Low', 'Low Fat': 'Low', 
                                   'low fat': 'Low', 'reg': 'Regular' }, inplace=True)
    data.drop(['item_identifier', 'outlet_establishment_year', 'outlet_identifier'], 
              axis=1, inplace=True, errors='ignore')
    return data