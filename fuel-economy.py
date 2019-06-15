import pandas as pd

pd.options.display.max_columns = 50
pd.options.display.width = 300

df_08 = pd.read_excel('y08.xlsx')
# print(df_08.head())
df_18 = pd.read_excel('y18.xlsx')
# print(df_18.head())


def print_heads():
    print(df_08.head())
    print(df_18.head())


def print_info():
    print(df_08.info())
    print(df_18.info())


def print_desc():
    print(df_08.describe())
    print(df_18.describe())


# drop irrelevant columns
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)
# print(df_08.head())
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1, inplace=True)
# print(df_18.head())

# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area': 'Cert Region'}, inplace=True)
# print(df_08.head(2))

# replace spaces with underscores and lowercase labels for 2008 & 2018 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
# print(df_08.head(2))

df_18.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
# print(df_18.head(2))

# check labels for 2008 and 2018 datasets are identical
(df_08.columns == df_18.columns).all()

df_08 = df_08.query('cert_region ==\"CA\"')
# print(df_08)
df_18 = df_18.query('cert_region ==\"CA\"')
# print(df_18)

df_08['cert_region'].unique()
df_18['cert_region'].unique()

# drop certification region columns form both datasets
df_08.drop('cert_region', axis=1, inplace=True)
df_18.drop('cert_region', axis=1, inplace=True)

# missing value count for each feature in 2008
# print(df_08.isnull().sum())
# missing value count for each feature in 2018
# print(df_18.isnull().sum())

# drop null in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)

# checks if any of columns in 2008 have null values - should print False
# print(df_08.isnull().sum().any())
# checks if any of columns in 2018 have null values - should print False
# print(df_18.isnull().sum().any())

# number of duplicates in 2008 and 2018 datasets
# print(df_08.duplicated().sum())
# print(df_18.duplicated().sum())

# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)

df_08['cyl'] = df_08['cyl'].str.extract('(\\d+)').astype(int)
df_08['cyl'] = df_08['cyl'].astype(int)

df_18['cyl'] = df_18['cyl'].astype(int)

# print(df_08[df_08['fuel'].str.contains('/')])
# print(df_18[df_18['fuel'].str.contains('/')])

hb_08 = df_08[df_08['fuel'].str.contains('/')]

df1 = hb_08.copy()
df2 = hb_08.copy()

split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg', 'cmb_mpg', 'greenhouse_gas_score']

for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

new_row = df1.append(df2)

df_08.drop(hb_08.index, inplace=True)
df_08 = df_08.append(new_row, ignore_index=True)


hb_18 = df_18[df_18['fuel'].str.contains('/')]

df3 = hb_18.copy()
df4 = hb_18.copy()

split_columns = ['fuel', 'city_mpg', 'hwy_mpg', 'cmb_mpg']

for b in split_columns:
    df3[b] = df3[b].apply(lambda x: x.split('/')[0])
    df4[b] = df4[b].apply(lambda x: x.split('/')[1])

new_row2 = df3.append(df4)

df_18.drop(hb_18.index, inplace=True)
df_18 = df_18.append(new_row2, ignore_index=True)

split_mpg_columns = ['city_mpg', 'hwy_mpg', 'cmb_mpg']

for j in split_mpg_columns:
    df_08[j] = df_08[j].astype(float)
    df_18[j] = df_18[j].astype(float)

df_08['greenhouse_gas_score'] = df_08['greenhouse_gas_score'].astype(int)
df_08['air_pollution_score'] = df_08['air_pollution_score'].astype(float)
df_18['air_pollution_score'] = df_18['air_pollution_score'].astype(float)

df_08.to_csv('clean_08.csv', index=False)
df_18.to_csv('clean_18.csv', index=False)