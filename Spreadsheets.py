# 1. Read the excel file:

df = pd.read_excel('tablename.xlsx')
print(df.head())

# 2. Loading select columns and rows:

excel_df = pd.read_excel('tablename.xlsx',
                         skiprows = 2,
                         ncols = "W:AB, AR")
print(excel_df.head())

# 3. read the excel file:

# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('fcc_survey.xlsx')

# View the head of the dataframe
print(survey_responses.head())

# 4. 
