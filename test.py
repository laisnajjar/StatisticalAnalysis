import pandas as pd
from scipy.stats import chi2_contingency

# Read data from csv
df = pd.read_csv('sV.csv', index_col='Catagory')

# Transpose the DataFrame to make variables as rows
df = df.transpose()
results = pd.DataFrame(columns=['Variable', 'Chi-Square Statistic', 'p-value', 'Degrees of Freedom'])

# Perform the Chi-Square test of independence for each variable
for index, row in df.iterrows():
    if index != 'Orientalism':
        # Construct the contingency table
        contingency_table = [row.values, df.loc['Orientalism'].values]
        
        chi2, p, dof, expected = chi2_contingency(contingency_table)

        print(f"\nChi-Square test of independence for variable '{index}':")
        print(f"Chi-Square statistic = {chi2}")
        print(f"p-value = {p}")
        print(f"Degrees of freedom = {dof}")
        print(f"Expected frequencies:\n{expected}")
        # Create a DataFrame with the results
        temp_df = pd.DataFrame([{'Variable': index, 'Chi-Square Statistic': chi2, 
                                  'p-value': p, 'Degrees of Freedom': dof}])
        results = pd.concat([results, temp_df], ignore_index=True)

# Write the results DataFrame to a CSV file
results.to_csv('chi_square_results.csv', index=False)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Load data
df = pd.read_csv('Data_Sets/dubai_data.csv')

# Select relevant columns
relevant_cols = ['Place', 'Cultural Site', 'Religious Theme', 'Desert', 'Nature', 'Wildlife', 'Attire', 
                 'Cuisine', 'Architecture', 'Megaevents/Festivals', 'Leisure Activity', 'Orientalism']
df = df[relevant_cols]

# Define X and y
X = df.drop('Orientalism', axis=1)
y = df['Orientalism']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize logistic regression model
log_reg = LogisticRegression()

# Fit the model
log_reg.fit(X_train, y_train)

# Predict on test set
y_pred = log_reg.predict(X_test)

# Print model accuracy
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset
df = pd.read_csv('Data_Sets/dubai_data.csv')

# Select predictors
predictors = ['Place', 'Cultural Site', 'Religious Theme', 'Desert', 'Nature', 
              'Wildlife', 'Architecture', 'Megaevents/Festivals', 'Leisure Activity']

# Ensure that predictors and target are in numeric form
for var in predictors + ['Orientalism']:
    df[var] = pd.to_numeric(df[var], errors='coerce')

# Drop NA values
df = df.dropna()

# Create feature matrix X and target vector y
X = df[predictors]
y = df['Orientalism']

# Split the data into training set and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Fit the model on training data
model.fit(X_train, y_train)

# Get the coefficients
coefficients = pd.DataFrame({'Variable': X.columns, 'Coefficient': model.coef_[0]})

# Save the coefficients to a csv file
coefficients.to_csv('logistic_coefficients.csv', index=False)

print('Coefficients saved to logistic_coefficients.csv')
