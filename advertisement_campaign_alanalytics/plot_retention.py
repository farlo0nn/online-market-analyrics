import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('retention_result.csv')

# Create pivot table
pivot_table = df.pivot(index='day_number', columns='ads_campaign', values='retention')

# Plot pivot table
plt.figure(figsize=(8, 5))
for campaign in pivot_table.columns:
    plt.plot(pivot_table.index, pivot_table[campaign], marker='o', label=campaign)

plt.title('Retention Over Time by Ad Campaign')
plt.xlabel('Day Number')
plt.ylabel('Retention Rate')
plt.legend(title='Campaign')
plt.grid(True)

plt.show()
