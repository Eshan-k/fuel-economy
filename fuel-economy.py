import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 50
pd.options.display.width = 300

df_08 = pd.read_excel('y08.xlsx')
# print(df_08.head())
df_18 = pd.read_excel('y18.xlsx')
# print(df_18.head())

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
print(df_08.isnull().sum())
# missing value count for each feature in 2018
print(df_18.isnull().sum())

# drop null in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)

# checks if any of columns in 2008 have null values - should print False
print(df_08.isnull().sum().any())
# checks if any of columns in 2018 have null values - should print False
print(df_18.isnull().sum().any())

# number of duplicates in 2008 and 2018 datasets
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())

# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)

