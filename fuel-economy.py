import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 50
pd.options.display.width = 300

df_08 = pd.read_excel('y08.xlsx')
# print(df_08.head())
df_18 = pd.read_excel('y18.xlsx')
# print(df_18.head())

# drop irrelevant columns
df_08.drop(['Stnd'], ['Underhood ID'], ['FE Calc Appr'], ['Unadj Cmb MPG'])
df_18.drop(['Stnd'], ['Stnd Description'], ['Underhood ID'], ['Comb CO2'])
