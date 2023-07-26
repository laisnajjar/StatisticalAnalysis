import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MasaDubaiFull.csv')

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

freq_df = pd.DataFrame()
for column in numeric_columns:
    try:
        freq_df[column] = df[column].value_counts().loc[[0, 1]]
    except KeyError:
        pass

freq_df.to_csv('FrequencyTable_MasaDubaiFull.csv')

# unstack the DataFrame
unstacked_df = freq_df.unstack().reset_index()
unstacked_df.columns = ['Variable', 'Value', 'Frequency']

# plot bar graph
plt.figure(figsize=(10, 5))  # adjust size as needed
sns.barplot(x='Variable', y='Frequency', hue='Value', data=unstacked_df)
plt.title('Frequency of 0 and 1 in Variables')
plt.xlabel('Variables')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # rotate x-axis labels if they're long
plt.tight_layout()  # adjust layout for better fit
plt.savefig('FreqBar_MasaDubaiFull.png')
