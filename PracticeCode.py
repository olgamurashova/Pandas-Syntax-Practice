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
