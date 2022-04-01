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

# 4. Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel("fcc_survey.xlsx",
                               sheet_name = 1)

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# 5. # Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel("fcc_survey.xlsx",
sheet_name = '2017')

# Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# 6. 
# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Append df to all_responses, assign result
  all_responses = all_responses.append(df)

  # Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()
