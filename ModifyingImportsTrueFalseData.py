# 1. Booleans True/False 

# Import the table first

df = pd.read_excel('tablename.xlsx')
# Read data types to determine if boolean values have been recognized:
print(df.dtypes)
# Count booleans values:
print(df.sum())

# Count Nas/Checking how many values are missing in the table
print(df.isna().sum())

# Loading data/ Casting True/False columns as Boolean
bool_data = pd.read_excel('tablename.xlsx',
                          dtype = {
                            'columnname':bool,
                            'columnname':bool,
                            'columnname':bool})


# 2. 
