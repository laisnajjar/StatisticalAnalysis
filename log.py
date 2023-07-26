# Logistic Regression Test Between 'Place' and 'Orientalism' in Saudi and Dubai Samples
import pandas as pd
import statsmodels.api as sm
#--------Saudi Sample----------------
saudi_data = pd.read_csv('saudi_data.csv') # Load the data
y = saudi_data['Orientalism'] # Define the dependent variable (Orientalism) and the independent variable
X = saudi_data['Place']  
X = sm.add_constant(X) # Add a constant to the independent variable
model = sm.Logit(y, X) # Run the logistic regression
result = model.fit() # Fit the model
print("Saudi Sample Logistics Regression Results:")
print(result.summary()) # Print the summary of the regressionS
#--------Dubai Sample----------------
dubai_data = pd.read_csv('dubai_data.csv')
y = dubai_data['Orientalism']
X = dubai_data['Place']
X = sm.add_constant(X)
model = sm.Logit(y, X)
result = model.fit()
print("Dubai Sample Logistics Regression Results:")
print(result.summary())