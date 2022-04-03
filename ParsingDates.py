# 1. To parse the dates we pass the names of the columns with dates we want to parse:

# List columns of dates to parse
date_cols = ['column1', 'column2']
df = pd.read_excel('tablename.xlsx',
                   parse_dates = date_cols)
