import matplotlib.pyplot as plt
import pandas as pd

# Load the data
rater1 = pd.read_csv('MaddySaudi.csv')
rater2 = pd.read_csv('MasaSaudi(sample).csv')

# Create a new figure
plt.figure()

# Create a subplot for the first dataset
plt.subplot(1, 2, 1)
plt.title('Dataset 1')
rater1['Cuisine'].value_counts().plot(kind='bar')

# Create a subplot for the second dataset
plt.subplot(1, 2, 2)
plt.title('Dataset 2')
rater2['Cuisine'].value_counts().plot(kind='bar')

# Show the plot
plt.savefig('plot.png')