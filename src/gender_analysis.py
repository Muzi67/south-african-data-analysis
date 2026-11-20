
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load the Stats SA dataset
file = "data/QLFS Trends 2008-2026Q3.xlsx"

df = pd.read_excel(
    file,
    sheet_name="Table 2",
    header=None
)

# 2. Extract quarter labels
quarters = df.iloc[1, 1:].astype(str).str.strip()

# 3. Extract unemployment rates
women_rates = pd.to_numeric(
    df.iloc[49, 1:],
    errors="coerce"
)

men_rates = pd.to_numeric(
    df.iloc[74, 1:],
    errors="coerce"
)

# 4. Create a clean DataFrame
gender_data = pd.DataFrame({
    "Quarter": quarters.values,
    "Women": women_rates.values,
    "Men": men_rates.values
})

gender_data = gender_data.dropna()

# 5. Display the latest results
latest = gender_data.iloc[-1]

print("\nGENDER UNEMPLOYMENT COMPARISON")
print("Latest quarter:", latest["Quarter"])
print(f"Women: {latest['Women']:.1f}%")
print(f"Men: {latest['Men']:.1f}%")

gap = latest["Women"] - latest["Men"]

print(f"Gender gap: {gap:.1f} percentage points")

# 6. Plot the comparison
plt.figure(figsize=(15, 7))

x = range(len(gender_data))

plt.plot(
    x,
    gender_data["Women"],
    marker="o",
    markersize=3,
    linewidth=1.8,
    label="Women"
)

plt.plot(
    x,
    gender_data["Men"],
    marker="o",
    markersize=3,
    linewidth=1.8,
    label="Men"
)

# 7. Add graph labels
plt.title(
    "Unemployment Rate by Gender in South Africa (2008–2026)",
    fontsize=15
)

plt.xlabel("Quarter")
plt.ylabel("Unemployment Rate (%)")

tick_positions = list(range(0, len(gender_data), 5))

plt.xticks(
    tick_positions,
    gender_data["Quarter"].iloc[tick_positions],
    rotation=45,
    ha="right"
)

plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# 8. Save the graph
Path("images").mkdir(exist_ok=True)

plt.savefig(
    "images/gender_unemployment.png",
    dpi=300
)

plt.show()

print("\nGender analysis completed successfully!")
