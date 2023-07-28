import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv('Data_Sets/saudi_data.csv')

# Define the regional variables
regional_variables = ['Cultural Site', 'Religious Theme', 'Desert', 'Attire']

# Create an empty DataFrame to store the results
results = pd.DataFrame(columns=['Variable', 'Chi-Square Statistic', 'p-value', 'Degrees of Freedom'])

# Perform the Chi-Square test for each regional variable
for variable in regional_variables:
    contingency_table = pd.crosstab(df[variable], df['Orientalism'])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

 # Append the results to the DataFrame
    results.loc[len(results)] = [variable, chi2, p, dof]

# # Save the results to a CSV file
# results.to_csv('chi_square_results.csv', index=False)

# # Define the non-regional variables
# non_regional_variables = ['Nature', 'Wildlife', 'Attire', 'Cuisine', 'Architecture', 'Leisure Activity']

# # Create an empty DataFrame to store the results
# results = pd.DataFrame(columns=['Variable', 'Chi-Square Statistic', 'p-value', 'Degrees of Freedom'])

# # Perform the Chi-Square test for each non-regional variable
# for variable in non_regional_variables:
#     contingency_table = pd.crosstab(df[variable], df['Orientalism'])
#     chi2, p, dof, expected = chi2_contingency(contingency_table)

#     # Append the results to the DataFrame
#     results.loc[len(results)] = [variable, chi2, p, dof]

# Save the results to a CSV file
results.to_csv('chi_square_results_saudi.csv', index=False)