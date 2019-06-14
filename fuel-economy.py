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
print(df_08.head())
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1, inplace=True)
print(df_18.head())

# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area': 'Cert Region'}, inplace=True)
df_08.head(2)

# replace spaces with underscores and lowercase labels for 2008 & 2018 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
df_08.head(2)

df_18.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
df_18.head(2)

# check labels for 2008 and 2018 datasets are identical
(df_08.columns == df_18.columns).all()

# save the datasets
df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
