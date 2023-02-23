import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("OWA AER.csv")

# subset the data to include only Abandoned, Suspended, Commingled, and Drilled & Cased
sub_data = data[data['status'].isin(['Abandoned', 'Suspended', 'Commingled', 'Drilled & Cased'])]

# count the number of wells for each status
status_counts = sub_data['status'].value_counts()

# create a bar plot
plt.bar(status_counts.index, status_counts.values)

# set axis labels and title
plt.xlabel('Status')
plt.ylabel('Count')
plt.title('Count of Wells by Status')

# add total score column to the plot
plt.twinx()
plt.plot(sub_data.groupby('status')['total score'].mean(), linestyle='-', marker='o', color='red', label='Mean Total Score')
plt.ylabel('Mean Total Score')
plt.legend()

# show the plot
plt.show()

