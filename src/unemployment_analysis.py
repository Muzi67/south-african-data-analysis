
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load the Stats SA Excel dataset
file = "data/QLFS Trends 2008-2026Q3.xlsx"

df = pd.read_excel(
    file,
    sheet_name="Table 2",
    header=None
)

# 2. Read the row labels
labels = df.iloc[:, 0].astype(str).str.strip()

# 3. Find the unemployment rate for all population groups
# There are three LU1 rows, so we select the first one.
row_index = labels[
    labels.str.contains("LU1", case=False, na=False)
].index[0]

print("Selected row:", row_index)
print("Selected label:", labels.iloc[row_index])

# 4. Extract the quarter labels
quarters = df.iloc[1, 1:].astype(str).str.strip()

# 5. Extract unemployment rates
rates = pd.to_numeric(
    df.iloc[row_index, 1:],
    errors="coerce"
)

# 6. Create a clean DataFrame
unemployment = pd.DataFrame({
    "Quarter": quarters.values,
    "Unemployment_Rate": rates.values
})

# Remove missing observations
unemployment = unemployment.dropna()

# 7. Display the data
print("\nFIRST FIVE QUARTERS")
print(unemployment.head())

print("\nLATEST FIVE QUARTERS")
print(unemployment.tail())

# 8. Calculate summary statistics
print("\nSUMMARY STATISTICS")
print(unemployment["Unemployment_Rate"].describe())


# 9. Create the unemployment trend graph

plt.figure(figsize=(15, 7))

# Actual unemployment trend
plt.plot(
    range(len(unemployment)),
    unemployment["Unemployment_Rate"],
    color="blue",
    marker="o",
    markersize=3,
    linewidth=1.8,
    label="Quarterly unemployment rate"
)

# Historical average
average_rate = unemployment["Unemployment_Rate"].mean()

plt.axhline(
    y=average_rate,
    color="red",
    linestyle="--",
    linewidth=1.5,
    label=f"Historical average: {average_rate:.1f}%"
)

# Latest unemployment rate
latest_rate = unemployment["Unemployment_Rate"].iloc[-1]

plt.scatter(
    len(unemployment) - 1,
    latest_rate,
    color="green",
    s=100,
    zorder=5,
    label=f"Latest rate: {latest_rate:.1f}%"
)

# Graph labels
plt.title(
    "South African Unemployment Rate (2008–2026)",
    fontsize=16
)

plt.xlabel("Quarter")
plt.ylabel("Unemployment Rate (%)")

# Display every fifth quarter
tick_positions = list(range(0, len(unemployment), 5))

plt.xticks(
    tick_positions,
    unemployment["Quarter"].iloc[tick_positions],
    rotation=45,
    ha="right"
)

plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Save graph
plt.savefig(
    "images/sa_unemployment_trend.png",
    dpi=300
)

plt.show()
