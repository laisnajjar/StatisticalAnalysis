import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Load the two dataframes
df1 = pd.read_csv('MasaDubaiFull.csv')
df2 = pd.read_csv('MasaSaudiFull.csv')

# Ensure that 'orientalism' in both dataframes is a categorical variable
df1['Orientalism'] = df1['Orientalism'].astype('category')
df2['Orientalism'] = df2['Orientalism'].astype('category')

# Concatenate the 'orientalism' series from both dataframes
combined_orientalism = pd.concat([df1['Orientalism'], df2['Orientalism']])

# Perform a Chi-square test of independence.
crosstab = pd.crosstab(index=combined_orientalism, columns="count")
chi2, p, dof, expected = chi2_contingency(crosstab)

# Print the chi2 statistic and p-value
print(f"chi2 statistic: {chi2}")
print(f"p-value: {p}")
