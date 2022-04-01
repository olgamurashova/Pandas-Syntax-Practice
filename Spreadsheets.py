# 1. Read the excel file:

df = pd.read_excel('tablename.xlsx')
print(df.head())

# 2. Loading select columns and rows:

excel_df = pd.read_excel('tablename.xlsx',
                         skiprows = 2,
                         ncols = "W:AB, AR")
print(excel_df.head())

# 3. 
