# 1. Selecting spreadsheets to load (by index or by spreadsheet name):

excel_df = pd.read_excel('tablename.xlsx',
                         sheet_name = 1)

excel_df1 = pd.read_excel('tablename.xlsx',
                         sheet_name = '2017')

# 2. Loading all sheets by passing sheet_name = None:

excel_df = pd.read_excel('tablename.xlsx',
                         sheet_name = None)

print(type(excel_df)) # checking the type of data result

# 3. 

