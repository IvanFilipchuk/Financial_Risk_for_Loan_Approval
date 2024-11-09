import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

# original_dataset = pd.read_csv('./Loan.csv')
# print(original_dataset.head())
# print(original_dataset.isnull().sum())
# print(original_dataset.describe())

# Script to create a new dataset with missing values

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
print(dataset.isnull().sum())
print(dataset.describe())

numerical_features = [
    'Age', 'AnnualIncome', 'CreditScore', 'Experience', 'LoanAmount',
    'LoanDuration', 'NumberOfDependents', 'DebtToIncomeRatio',
    'MonthlyDebtPayments', 'CreditCardUtilizationRate', 'NumberOfOpenCreditLines',
    'PreviousLoanDefaults', 'LengthOfCreditHistory', 'SavingsAccountBalance',
    'CheckingAccountBalance', 'TotalAssets', 'TotalLiabilities', 'MonthlyIncome',
    'JobTenure', 'NetWorth', 'BaseInterestRate', 'InterestRate',
    'MonthlyLoanPayment', 'TotalDebtToIncomeRatio'
]

# Wybór kolumn, które nas interesują (w tym zmienna docelowa RiskScore)
selected_columns = numerical_features + ['RiskScore']

# Usuń wiersze z brakującymi wartościami
dataset_clean = dataset[selected_columns].dropna()

# Oblicz macierz korelacji
correlation_matrix = dataset_clean.corr()

# Wyświetl korelacje ze zmienną RiskScore
correlation_with_risk_score = correlation_matrix['RiskScore'].sort_values(ascending=False)
print(correlation_with_risk_score)

# Wizualizacja macierzy korelacji
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()