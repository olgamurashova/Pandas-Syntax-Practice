# 1. Booleans True/False 

# Import the table first

df = pd.read_excel('tablename.xlsx')
# Read data types to determine if boolean values have been recognized:
print(df.dtypes)
# Count booleans values:
print(df.sum())

