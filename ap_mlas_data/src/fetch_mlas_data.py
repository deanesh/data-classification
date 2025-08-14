import pandas as pd
import utils
# Load the table
url = "https://www.elections.in/andhra-pradesh/assembly-constituencies/mlas-list.html"
tables = pd.read_html(url)
df = tables[0]
print(df.columns)

# Rename columns (assuming side-by-side layout)
df.columns = [
    'AC_No_L', 'AC_Name_L', 'MLA_Name_L', 'Party_L',
    'AC_No_R', 'AC_Name_R', 'MLA_Name_R', 'Party_R'
]

# Extract left and right parts
left = df[['AC_No_L', 'AC_Name_L', 'MLA_Name_L', 'Party_L']].copy()
left.columns = ['AC_No', 'Constituency_Name', 'MLA_Name', 'Party']

right = df[['AC_No_R', 'AC_Name_R', 'MLA_Name_R', 'Party_R']].copy()
right.columns = ['AC_No', 'Constituency_Name', 'MLA_Name', 'Party']

# Combine
mlas = pd.concat([left, right], ignore_index=True)

# Clean: Drop rows where Constituency Name is missing or AC_No is not numeric
mlas = mlas.dropna(subset=['Constituency_Name', 'AC_No'])
mlas = mlas[mlas['AC_No'].astype(str).str.isnumeric()]

# Convert AC_No to integer safely
mlas['AC_No'] = mlas['AC_No'].astype(int)

# Reset index
mlas.reset_index(drop=True, inplace=True)

print(f"✅ Total MLAs Extracted: {len(mlas)}")
mlas_df = mlas


# Assuming 'mlas' DataFrame has 'Constituency_Name'
mlas['District'] = mlas['Constituency_Name'].map(utils.constituency_to_district)

# Identify any unmatched names
missing = mlas[mlas['District'].isna()]['Constituency_Name'].unique()
if len(missing):
    print("These constituencies were not mapped to any district:", missing)
else:
    print("All constituencies mapped successfully!")

# print(mlas[['Constituency_Name', 'District']].head())


