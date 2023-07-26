# Logistic Regression Test Between 'Place' and 'Orientalism' in Saudi and Dubai Samples
import pandas as pd
import statsmodels.api as sm
#--------Saudi Sample----------------
saudi_data = pd.read_csv('Data_Sets/saudi_data.csv') # Load the data
y = saudi_data['Orientalism'] # Define the dependent variable (Orientalism) and the independent variable
X = saudi_data['Place']  
X = sm.add_constant(X) # Add a constant to the independent variable
model = sm.Logit(y, X) # Run the logistic regression
result1 = model.fit() # Fit the model
print("Saudi Sample Logistics Regression Results:")
print(result1.summary()) # Print the summary of the regressionS
#--------Dubai Sample----------------
dubai_data = pd.read_csv('Data_Sets/dubai_data.csv')
y = dubai_data['Orientalism']
X = dubai_data['Place']
X = sm.add_constant(X)
model = sm.Logit(y, X)
result2 = model.fit()
print("Dubai Sample Logistics Regression Results:")
print(result2.summary())

# Convert the summary results to text
result1_text = result1.summary().tables[1].as_text()
# Split the text by newline character to create a list of rows
result1_rows = result1_text.split('\n')
# Split each row by its spaces to create a list of columns
result1_data = [row.split() for row in result1_rows]
# Convert the list of columns to a DataFrame
result1_df = pd.DataFrame(result1_data)
# Write the DataFrame to a CSV file
result1_df.to_csv('logistic_regression_saudi.csv', index=False)

# Convert the summary results to text
result2_text = result2.summary().tables[1].as_text()
# Spli2 the text by n2wline character to create a list of rows
result2_rows = result2_text.split('\n')
# Spli2 each row by its spaces to create a list of columns
result2_data = [row.split() for row in result2_rows]
# Conv2rt the list of columns to a DataFrame
result2_df = pd.DataFrame(result2_data)
# Writ2 the DataFrame to a CSV file
result2_df.to_csv('logistic_regression_dubai.csv', index=False)