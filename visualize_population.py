import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Function to format y-axis tick labels
def format_y_tick_labels(value, _):
    if value >= 1e9:
        return f'{value/1e9:.1f} billion'
    elif value >= 1e6:
        return f'{value/1e6:.1f} million'
    else:
        return str(value)

# Read the data
data = pd.read_json("countrypoparea.json")
data_sorted = data.sort_values('population', ascending=False).head(20)

# Set up a modern and stylistic plot style
sns.set_style("whitegrid")
sns.set_palette("pastel")

# Create the bar plot
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='name', y='population', data=data_sorted, ax=ax)

# Format the y-axis tick labels
y_formatter = FuncFormatter(format_y_tick_labels)
ax.yaxis.set_major_formatter(y_formatter)

# Set plot title and labels
plt.title("Top 20 Countries by Population")
plt.xlabel('Name')
plt.ylabel('Population')

# Rotate x-axis tick labels
plt.xticks(rotation=45, ha='right')

# Adjust spacing
plt.tight_layout()

# Show the plot
plt.show()
