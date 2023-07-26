import pandas as pd
import krippendorff

# Load the data
rater1 = pd.read_csv('MaddySaudi.csv')
rater2 = pd.read_csv('MasaSaudi(sample).csv')

# Make sure the data is in the same order
rater1 = rater1.sort_values(by=['Unit', 'Name'])
rater2 = rater2.sort_values(by=['Unit', 'Name'])

# Calculate Krippendorff's alpha for each category and store the results in a dictionary
alphas = {}
for category in ['Type', 'Place', 'Cultural Site', 'Religion Theme', 'Desert', 'Nature', 'Wildlife', 'Attire', 'Cuisine', 'Architecture', 'Megaevents/Festivals', 'Leisure Activity', 'Orientalism']:
    alphas[category] = krippendorff.alpha([rater1[category], rater2[category]])

# Convert the dictionary to a DataFrame
df_alphas = pd.DataFrame(list(alphas.items()), columns=['Category', 'Krippendorffs Alpha'])

# Save the DataFrame to a CSV file
df_alphas.to_csv('krippendorffs_alpha.csv', index=False)
