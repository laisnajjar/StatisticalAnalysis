import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('Data_Sets/saudi_data.csv')
# List of variables for which you want to count the frequencies
variables = ['Place', 'Like Count (Masa Only)', 'Cultural Site', 'Religious Theme','Desert', 'Nature', 'Name of lanscape', 'Wildlife', 'Name of Wildlife', 'Architecture', 'Name of Artifact', 'Megaevents/Festivals', 'Name of Event', 'Leisure Activity', 'Orientalism']

# Initialize a dictionary to store the results
results = {}

# Loop through the variables
for var in variables:
    # Count the frequency of 0's and 1's
    counts = df[var].value_counts()
    # Store the results
    if(var == 'Cultural Site'): 
        print(counts)
    results[var] = {'0': counts.get(0, 0), '1': counts.get(1, 0)}

# Convert the results dictionary to a DataFrame
df_results = pd.DataFrame(results).T

# Append the DataFrame to the existing CSV file
#df_results.to_csv('results.csv')

# Initialize a dictionary to store the results
results = {}

# Handle 'Cuisine' and 'Attire' separately
for var in ['Cuisine']:
    # Count the frequency of each unique value
    counts = df[var].value_counts().to_dict()
    # Store the results
    results[var] = counts

# Convert the results dictionary to a DataFrame
df_results = pd.DataFrame(results).T

# Append the DataFrame to the existing CSV file
df_results.to_csv('results.csv', mode='a', header=False)

# Initialize a dictionary to store the results
results = {}

# Handle 'Cuisine' and 'Attire' separately
for var in ['Attire']:
    # Count the frequency of each unique value
    counts = df[var].value_counts().to_dict()
    # Store the results
    results[var] = counts

# Convert the results dictionary to a DataFrame
#df_results = pd.DataFrame(results).T

# Append the DataFrame to the existing CSV file
df_results.to_csv('results.csv', mode='a', header=False)


