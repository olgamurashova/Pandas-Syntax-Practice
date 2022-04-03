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
   
