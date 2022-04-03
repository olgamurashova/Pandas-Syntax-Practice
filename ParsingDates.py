# 1. To parse the dates we pass the names of the columns with dates we want to parse:

# List columns of dates to parse
date_cols = ['column1', 'column2']
df = pd.read_excel('tablename.xlsx',
                   parse_dates = date_cols)

# 2.Splitting datetime columns:

# List columns of dates to parse:

date_cols = ['column1',
             'column2',
             [['column3,
              'column4]]]

# Loading file, parsing standard and split datetime columns:
               
df = pd.read_excel('tablename.xlsx',
                   parse_dates = date_cols)
               
# 4. To control the column names before parsing the datetime columns, we create a dictionary:
              
 date_cols = { "Part1Start": "Part1StartTime",
              "Part1End": "Part1EndTime",
              "Part2Start":["Part2StartDate, "Part2StartTtime"]}
                            
 df = pd.read_excel('tablename.xlsx',
                    parse_dates = date_cols)
 print(df.head(3))
   
 # 5. Parsing non standard dates:
 # We build the string format first/ Month/Day/Year and Hour/Minute/Second format:
string_format = '%m%d%Y %H:%M:%S'                            
# then, we convert to datetime and assign conversiton to our column and pass string_format to format:
 df['column_name'] = pd.to_datetime(df['column_name'], 
                                    format = string_format)

# 6. # Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())
                            
# 7. # Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates = datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())                            
