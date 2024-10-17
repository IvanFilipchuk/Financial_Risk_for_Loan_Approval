import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

# Script to create a new dataset with missing values

# original_dataset = pd.read_csv('./Loan.csv')
# print(original_dataset.head())
# print(original_dataset.isnull().sum())
# print(original_dataset.describe())
#
# missing_percentage = np.random.uniform(0.10, 0.15)
# rows, cols = original_dataset.shape
# num_missing_values = int(missing_percentage * rows * cols)
#
# dataset_with_missing = original_dataset.copy()
#
# for _ in range(num_missing_values):
#     row = np.random.randint(0, rows)
#     col = np.random.randint(0, cols)
#     dataset_with_missing.iat[row, col] = np.nan
#
# dataset_with_missing.to_csv('./Loan_with_missing_data.csv', index=False)

dataset = pd.read_csv('./Loan_with_missing_data.csv')
print(dataset.head())
print(dataset.isnull().sum())
print(dataset.describe())
