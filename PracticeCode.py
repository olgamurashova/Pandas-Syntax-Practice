# 1. Creating a new dataframe:

df = pd.DataFrame({
    'name': ['Kate', 'John', 'Travis'], 
    'age': [32, 34, 36], 
    'occupation': ['Physician', 'Engineer', 'Clerk']
    })
print(df)

# 2. Creating a new dataframe sample:

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})
print(df1)

# 3. Adding data using lists:

df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])

# Another sample

df1 = pd.DataFrame([
    ['Uzbekistan', 'Tashkent','3600000'],
    ['Kazakstan', 'Astana', '4900000'], 
    ['Kyrgistan', 'Bishkek', '4500000']
],
    columns = ['Country', 'Capital', 'Population']
                  )
print(df1)

# Another sample

f2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
   'Store ID',
   'Location',
   'Number of Employees'
  ])

print(df2)

# 4. Writing a CSV file:

df.to_csv('data.csv')
df1.to_csv('storedata.csv')

# 5. Loading files with different delimiters:

# Import pandas with the alias pd
import pandas as pd

# Load TSV using the sep keyword argument to set delimiter
data = pd.read_csv('vt_tax_data_2016.tsv',sep="\t")

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()

# 6. Displaying how many rows and columns are in a table:

print(df.shape)

# 7. Limiting columns/Choose columns to load by name and number using usecols:

col_names = ['column_name1', column_name2', 'column_name3']
col_num = [1, 2, 5]

#Choose columns to load by name:
 df = pd.read_csv('tablename.csv', usecols = col_names)
# Choose columns to load by number:
 df_1 = pd.read_csv('tablename.csv', usecols = col_num)
# Checking if two tables contain same columns
print(df.equals(df2))

# 8. Limiting rows using nrows:
  
 df = pd.read_csv('tablename.csv', nrows = 1000)
 print(df.shape)
 
#9. Assigning column names when importing specified number of rows using nrows:
 
 df1 = pd.read_csv('tablename.csv', nrows = 1000)
 col_names = list(df1)
 df2 = pd.read_csv('tablename.csv', 
                   nrows = 500,
                   skiprows = 1000,
                   header = None,
                   names = col_names)
  print(df.header(1))

#10. Importing certain columns:

 # Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())
