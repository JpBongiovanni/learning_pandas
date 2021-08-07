import pandas as pd
import numpy as np


df = pd.read_csv("data/mcas_csv.csv")



relative_data = ['sasid', 'stugrade', 'eperf2', 'mperf2', 'sperf2', 'escaleds', 'mscaleds', 'sscaleds', 'ecpi', 'mcpi', 'scpi']



df[['eperf2', 'mperf2']] = df[['eperf2','mperf2']].replace({'F': '1-f', 'W': '2-W', 'NI': '3-N1', 'P': '4-P', 'A': '5-A', 'P+': '6-P+'})

rd_df = df[relative_data]

rd_df.rename(columns={'sasid':'StudentTestId', 'stugrade': 'Student Grade Level'}, inplace = True)

rd_df['NCESID'] = 373737
rd_df['StudentLocalID'] = 'missing'
rd_df['TestDate ELA'] = '04/01/2021'
rd_df['TestDate Math'] = '05/01/2021'
rd_df['TestDate Science'] = '06/01/2021'

print(rd_df)
# df = pd.read_csv("data/mcas_csv.csv", index_col='<column lable>') this will change the index to a unique column lable as the csv is bein read

# print(df[['grade', 'firstname']])
# print(df.columns) # gets all columns

# print(df.iloc[0]) #stands for integer location. This will give us the first row

# print(df.iloc[[0, 1]]) #gets first two rows of data. MUST pass in inner list

# print(df.iloc[[0, 1], 3]) #this gets first two rows of data IN the third column

#iloc searches integers, loc finds labels

# print(df.loc[[0,1], ['school', 'bookletnumber']]) #returns rows selected and columns selected in the order you select them

# print(df.columns) #shows columns available

# print(df['lastname'].value_counts()) #grabs lastname column, and counts how many entries

# print(df.loc[[0,1,2], 'lastname']) #grabs first 3 rows and their entry

# print(df.loc[0:2, 'school':'lastname']) # grabs first 3 rows with a slice. Don't need to put brackets around the slice. will also grab all columns from school to last name.

#-----------------------------Indexes_________________________-

#df.set_index('email') would set the index column to the email. Choose a column lable that is unique pandas won't save it unless you tell it too you must add df.set_index('email', inplace=True)

# df.sort_index() - this will sort your index labels if you changed them.

#----------------------------Filtering and Using conditionals to filter rows and columns-----------

# filt = (df['lastname'] == 'Smith') & (df['firstname'] == 'John') 
# filters selected column with selected value, returns booleans in order to see whole dataset you need to put the filter in a variable and then print the variable.

#or, df[df['last']=='Doe']

# print(df[filt]) 
# print(df.loc[filt, 'lastname'])
# print(df.loc[~filt, 'lastname']) #the tilda (~) gives you the opposite of that filter

# grade_level = (df['stugrade'] > 4)

# print(df['stugrade'])
# print(df.loc[grade_level])

#!!!!!!!!-------!!!!!!!------- function to grab columns for ellevation assignment---------
#district and booklet number and test date have defaults


# filt = (df.loc[0:5, ['stugrade', 'eperf2', 'mperf2', 'sperf2', 'escaleds', 'mscaleds', 'sscaleds', 'ecpi', 'mcpi', 'scpi']])

# print(filt)

#filter example -- 
# countries = ['United States', 'India', "united Kingdom"]
# filt = df['Country'].isin(countries)
# df.loc[filt, 'Country']

#OR

#filt = df['LanguageWorkedWith'].str.contains('Python', na=False) - this filter looks in the column and finds strings that contain "Python"
#df.loc[filt, 'LanguagesWorkedWith']

#--------------Altering data-------------------


# df.columns = ['col1', 'col2', 'col3']
#by assigning a name to columns you can overwrite the existing column
# df.columns = [x.upper() for x in df.columns]
# df.columns = df.columns.str.replace('D', 'A')
# df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace = True) 
#Use above to rename values for column titles. the above line uses a dictionary to assign values to one another.

# df.loc[0] = ['DistrictY']
# df.loc[0, ['district']] = ['DistrctY']
#the above code changes one value but you can add values to 'district' and 'DisstrictY' in order to assign values in a list.
# print(df.loc[0, ['district']])

#change multiple rows at the same time---
#to make change below permenant, write...df['district'] = df['district'].str.lower()
# print(df['district'].str.lower())
#---4 methods of changing rows----
#apply, map, applymap, replace

#apply - used to call a function or value on a series or dataframe
# df['district'].apply(len)
#!!!!!! use to update !!!! 

# def update_distict(district):
#     return district.upper()

#to make change below permenant, write...df['district'] = df['district'].apply(update_district)

# print(df['district'].apply(update_distict)) 
#pass the function itself, not the executed version of it with ()

#lambda functions also work: df['district'] = df['district'].apply(lambda x: x.lower())
#lambda doesn't require you to actually write the function, just write what it returns.

#apply on dataframes runs the function on rows and columns, not just the row in like in a series

# print(df['district'].apply(len))
# print(df.apply(len)) # gets num of rows in each columns
# print(df.apply(len, axis='columns')) # gets num of columns in each row
# print(df.apply(pd.Series.min))

#applymap only works on Data frames. It changes every entry in the dataframe

#Map method only works on a series
# df['first'] = df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})
#the above command will change all entries in the 'first' column with the assigned names but will also change any values not mentioned with NaN.

#replace method
# df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})
# The above command will change all entries in the 'first' column with the assign names and will NOT change any values not mentioned.

# print(df['district'].replace({'DistrictX': "DISTRICTY", 'Woburn Outplacement': 'WOBURN'}))

#!!!!!!!-------------add/remove rows and columns from dataframes

# df['full_name'] = df['first'] + ' ' + df['last'] -- this command concatinates two columns and creates a new column with the output

#df.drop(columns=['first', 'last']) deletes the columns selected
#df[['first', 'last']] = df.['full_name'].str.split(' ', expand = True) separates string on a space, and makes two columns

# df.append({'first' : 'Tony'}, ignore_index=True) adds a single row of data, puts NaN for empty data

#df.drop(index=4) drops a row. You can also add a condition
#df.drop(index = df[df['last']=='Doe'].index) removes values with a filter based on index
#filt = df['last'] == 'Doe'
#df.drop(index=df[filt].index) this is another way using a variable

#------ sorting data ---------

#df.sort_values(by='last', ascending=False) sorts by the provided column

#------- cleaning data - casting datatypes and handling missing values---------

# df.dropna() - drops rows that have any NaN values. 
# df.dropna(axis='index', how='any') - these are default arguments. axis can be set to index or columns. HOW is the criterea. changing it to ALL will only drop rows that have all missing values not just any.
# df.dropna(axis='index', how='any', subset=['email']) - this will return df with rows that have at least their email filled in

#!!!!!! ---- df.replace('NA', np.nan, inplace=True) This goes at the top where the CSV is read. When it encounters a certain string, it replaces it with another value.
#!!!!!! ---- df.replace('Missing', np.nan, inplace=True)
#df.isna() returns a boolean statement 
#df.fillna(0) fills na values with "0"

# casting datatypes----------
# df.dtypes - tells the kind of input is there
#df['age'] = df['age'].astype(float) -- use float if there are NaN values in your column, int if not
#df.astype() converts entire table

#!!!!!! establish a variable for objects you want to replace
# na_vals = ['NA', 'Missing']
#then add that argument into the pd.read_csv function
# df = pd.read_csv('data/mcas_csv.csv', index_col='Repsondent', na_values=na_vals)
# df['YearsCode'].unique() gets all unique values in a df.
# you can then replace unique values 
# df['YearsCode'].replace('Less than 1 year', 0, inplace=True)

#------------------Reading/Writing Data to different Sources--------

#filt = (df['Country'] == "India")
#india_df = df.loc[filt]
#india_dif.head

# to export...
#india_df.to_csv('data/modified.csv')
