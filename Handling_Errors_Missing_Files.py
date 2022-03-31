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

# 5. Specidying data types:

# Create dict specifying data types for agi_stub and zipcode
data_types = {"agi_stub": "category",
			  "zipcode": str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

# 6. Setting custon NaN values:

# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode' : 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv", 
                   na_values = null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])
