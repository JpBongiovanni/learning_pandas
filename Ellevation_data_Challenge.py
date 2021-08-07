#Psuedo Code explanation below python script

#1. 
import pandas as pd


#2.
df = pd.read_csv("data/mcas_csv.csv")

#3.
relative_data = ['sasid', 'stugrade', 'eperf2', 'mperf2', 'sperf2', 'escaleds', 'mscaleds', 'sscaleds', 'ecpi', 'mcpi', 'scpi']


#4.
df[['eperf2', 'mperf2', 'sperf2']] = df[['eperf2','mperf2', 'sperf2']].replace({'F': '1-f', 'W': '2-W', 'NI': '3-N1', 'P': '4-P', 'A': '5-A', 'P+': '6-P+'})

#5.
rd_df = df[relative_data]

#6.
rd_df.rename(columns={'sasid':'StudentTestID', 'stugrade': 'StudentGradeLevel', 'eperf2': 'ELA Perf. Lvl', 'mperf2': 'Math Perf. Lvl', 'sperf2': 'Sci Perf. Lvl', 'escaleds': 'ELA scaled', 'mscaleds': 'Math scaled', 'sscaleds': 'Sci scaled', 'ecpi': 'ELA cpi', 'mcpi': 'Math cpi', 'scpi': 'Sci cpi'}, inplace = True)

#7.
rd_df['NCESID'] = 373737
rd_df['StudentLocalID'] = 'missing'
rd_df['TestDateELA'] = '04/01/2021'
rd_df['TestDateMath'] = '05/01/2021'
rd_df['TestDateScience'] = '06/01/2021'
rd_df['ScoreLabel1'] = 'Performance Level'
rd_df['ScoreLabel2'] = 'Scaled Scores'
rd_df['ScoreLabel3'] = 'CPI'
rd_df['ScoreType1'] = 'Level'
rd_df['ScoreType2'] = 'Scale'
rd_df['ScoreType3'] = 'Scale'
rd_df['TestName'] = 'MCAS'
rd_df['TestTypeName1'] = 'MCAS ELA'
rd_df['TestTypeName2'] = 'MCAS Math'
rd_df['TestTypeName3'] = 'MCAS Sci'
rd_df['TestSubjectName1'] = 'ELA'
rd_df['TestSubjectName2'] = 'Math'
rd_df['TestSubjectName3'] = 'Sci'
rd_df['Test1GradeLevel'] = rd_df['StudentGradeLevel']
rd_df['Test2GradeLevel'] = rd_df['StudentGradeLevel']
rd_df['Test3GradeLevel'] = rd_df['StudentGradeLevel']

#8.
rd_df = rd_df[['NCESID', 'StudentTestID', 'StudentGradeLevel', 'TestName', 'TestDateELA', 'TestTypeName1', 'TestSubjectName1', 'Test1GradeLevel', 'ELA Perf. Lvl', 'ELA scaled', 'ELA cpi', 'TestDateMath', 'TestTypeName2', 'TestSubjectName2', 'Test2GradeLevel', 'Math Perf. Lvl', 'Math scaled', 'Math cpi', 'TestDateScience', 'TestTypeName3', 'TestSubjectName3', 'Test3GradeLevel', 'Sci Perf. Lvl', 'Sci scaled', 'Sci cpi']]

# print(rd_df)

#9.
rd_df.to_csv('data/mcas_processed.csv')


#Pseudo Explanation:
# 1. Import Pandas 
# 2. Create dataframe using provided csv file. -- here is where I could have optimised a lot. I'm confident that given time I could have figured out how to process the next step, as the csv was being written.
# 3. Pull the relative data columns from the dataframe. 
# 4. Convert data into the necessary Ellevation format
# 5. create new dataframe with pulled data
# 6. Rename columns from pulled data columns
# 7. Create necessary columns and populate them with information. Here is another area where I know that things could be more optimized. Rather than a long list of column entries, I could have figured out how to make it one line of code, and add all necessary columns in the same command.
# 7. Put the columns in the desired order
# 8. Process rd_df dataframe into a new .csv file. 

