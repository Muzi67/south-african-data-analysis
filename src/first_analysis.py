
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create a folder for the graphs
Path("images").mkdir(exist_ok=True)

# Example dataset (fictional practice data)
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Sales": [12000, 15000, 11000, 18000, 16000, 21000]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print("\nSALES DATA")
print(df)

# Calculate basic statistics
print("\nDATA SUMMARY")
print(df["Sales"].describe())

print("\nAverage sales:", df["Sales"].mean())
print("Highest sales:", df["Sales"].max())
print("Lowest sales:", df["Sales"].min())

# Create a bar chart
plt.figure(figsize=(10, 5))
plt.bar(df["Month"], df["Sales"])

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales (R)")
plt.xticks(rotation=30)
plt.tight_layout()

# Save the graph
plt.savefig("images/monthly_sales.png")
plt.show()
