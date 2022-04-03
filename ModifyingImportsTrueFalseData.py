# 1. Booleans True/False 

# Import the table first

df = pd.read_excel('tablename.xlsx')
# Read data types to determine if boolean values have been recognized:
print(df.dtypes)
# Count booleans values:
print(df.sum())

# Count Nas/Checking how many values are missing in the table
print(df.isna().sum())

# Loading data/ Casting True/False columns as Boolean (Changes all values dtype to Boolean
bool_data = pd.read_excel('tablename.xlsx',
                          dtype = {
                            'columnname':bool,
                            'columnname':bool,
                            'columnname':bool})


# 2. Setting custom true/False values

bool_data = pd.read_excel('tablename.xlsx',
                          dtype = {
                            'columnname':bool,
                            'columnname':bool,
                            'columnname':bool},
                            'true_values' = ['Yes'],
                             'false_values' = ['No'])
To avoid fame Na values being True, we should keep original value type (like float)

# 3. # Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype= {'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())




