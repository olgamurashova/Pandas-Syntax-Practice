# 1. Selecting spreadsheets to load (by index or by spreadsheet name):

excel_df = pd.read_excel('tablename.xlsx',
                         sheet_name = 1)

excel_df1 = pd.read_excel('tablename.xlsx',
                         sheet_name = '2017')

# 2. Loading all sheets by passing sheet_name = None:

excel_df = pd.read_excel('tablename.xlsx',
                         sheet_name = None)

print(type(excel_df)) # checking the type of data result

for key, value in excel.df.items():
  print(key, type(value))

# 3. Putting all spreadsheets together:

# Create empty dataframe
all_sheets_df = pd.DataFrame()

# Iterate through dataframes in dictionary(after loaded all sheets they formed a dictionary)

for sheet_name, frame in excel_df.items():
  # Add a column for we know which year the data is from
  frame['Year'] = sheet_name
  
# Add each dataframe to empty dataframe all_sheets_df

all_sheets_df = all_sheets_df.append(frame)

# View years in data:

print(all_sheets_df.Year.unique())



