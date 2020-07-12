import pandas as pd
#Read the input file which is delimited by ::
df = pd.read_csv("D:\\Delme\\Movie\\movies.csv", sep = "::")
#Movie name and year are inside the same column. Separate the two into different columns
df[['name','year']] = df["name"].str.split("(", n = 1, expand = True) 
# Replace the ) from the year column
df['year'] = df['year'].str.replace(')','')
# Replace Newline characters and carriage returns from the data frame
df.replace('\r',' ', regex=True, inplace = True)
df.replace('\n',' ', regex=True, inplace = True)

# Replace the comma "," from inside each of the columns so that clean file could be saved as csv
CHARS_TO_REPLACE = '\,'
for col in df.columns: 
    for char in CHARS_TO_REPLACE:
        col = col.replace(char,"")

#Convert the datatype of year to integer
df['year'] = pd.to_numeric(df['year'])

#Apply the filter for last decade and export the data set as .csv file. 		
df[(df['year']>=2001) & (df['year']<=2010)].to_csv("D:\\Delme\\Movie\\movies_clean.csv", encoding='utf-8', index=False)		