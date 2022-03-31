# 1. Cheking data types:

print('tablename.csv'.dtypes)

# 2. Specifying data types:

df = pd.read_csv('tablename.csv', dtype = {'zipcode' : str})

# 3. Setting custom missing values using na_values keyword:

df = pd.read_csv('tablename.csv',
                 na_values = {'zipcode': 0})

#Filterining NaN values in a column by using .isna() function:

print(df[df.zipcode.isna()])

# 4. Handling lines with errors using error_bad_lines and warn_bad_lines:

df = pd.read_csv('tablename.csv',
                 error_bad_lines = False,
                 warn_bad_lines = True)
