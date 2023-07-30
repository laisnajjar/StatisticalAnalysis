import pandas as pd
import statsmodels.api as sm
import numpy as np


df = pd.read_csv("Data_Sets/dubai_data.csv")

# Select relevant columns
cols_to_keep = ['Place', 'Cultural Site', 'Religious Theme', 'Desert',
                'Wildlife', 'Leisure Activity', 'Orientalism']
df = df[cols_to_keep]

# Make sure data is in correct format (0 or 1)
for col in cols_to_keep:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    assert set(df[col].unique()).issubset({0, 1}), f"Unexpected values in {col}"

# The dependent variable
y = df["Orientalism"]

# The independent variables
X = df.drop(columns=["Orientalism"])
X = sm.add_constant(X)  # Add a constant to represent the intercept
# Check for perfect prediction
for col in X.columns:
    if X[col].unique().size < 3:  # Binary predictor
        if y[X[col]==0].mean() in {0, 1} or y[X[col]==1].mean() in {0, 1}:
            print(f"Perfect prediction with {col}")

# Check for multicollinearity
correlations = X.corr()
for col1 in correlations.columns:
    for col2 in correlations.columns:
        if col1 < col2 and abs(correlations.loc[col1, col2]) > 0.9:
            print(f"High correlation between {col1} and {col2}")

# Calculate the correlation matrix
corr_matrix = X.corr().abs()

# Select upper triangle of correlation matrix
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Find index of feature columns with correlation greater than 0.9
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]

print(to_drop)
# Fit the model
model = sm.Logit(y, X)
result = model.fit()

# Print the summary of the model
print(result.summary())
