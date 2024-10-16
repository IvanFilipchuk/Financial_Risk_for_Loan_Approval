import pandas as pd

pd.set_option('display.max_columns', None)
dataset = pd.read_csv('./Loan.csv')
print(dataset.head())