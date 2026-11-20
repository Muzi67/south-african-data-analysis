
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load the Excel dataset
file = "data/QLFS Trends 2008-2026Q3.xlsx"

df = pd.read_excel(
    file,
    sheet_name="Table 2.3",
    header=None
)

# 2. Define the nine provinces
provinces = [
    "Western Cape",
    "Eastern Cape",
    "Northern Cape",
    "Free State",
    "KwaZulu Natal",
    "North West",
    "Gauteng",
    "Mpumalanga",
    "Limpopo"
]

# 3. Extract the latest quarter
latest_quarter = str(df.iloc[1, -1]).strip()

results = []

# 4. Find each province's unemployment rate
for province in provinces:

    # Find the province heading
    province_rows = df.index[
        df.iloc[:, 0].astype(str).str.strip() == province
    ]

    if len(province_rows) == 0:
        print(f"Could not find: {province}")
        continue

    start_row = province_rows[0]

    # Find the LU1 unemployment rate within this province's section
    section = df.iloc[start_row:start_row + 16, 0].astype(str)

    lu1_rows = section[
        section.str.contains("LU1", case=False, na=False)
    ]

    if lu1_rows.empty:
        print(f"Unemployment rate not found: {province}")
        continue

    rate_row = lu1_rows.index[0]

    # Extract the latest quarter's unemployment rate
    rate = pd.to_numeric(
        df.iloc[rate_row, -1],
        errors="coerce"
    )

    results.append({
        "Province": province,
        "Unemployment_Rate": rate
    })

# 5. Create a DataFrame
provincial_data = pd.DataFrame(results)

provincial_data = provincial_data.dropna()

# 6. Sort provinces from highest to lowest
provincial_data = provincial_data.sort_values(
    by="Unemployment_Rate",
    ascending=False
)

print("\nPROVINCIAL UNEMPLOYMENT RATES")
print(f"Quarter: {latest_quarter}")
print(provincial_data.to_string(index=False))

# 7. Create a bar chart
plt.figure(figsize=(12, 7))

plt.bar(
    provincial_data["Province"],
    provincial_data["Unemployment_Rate"]
)

plt.title(
    f"Unemployment Rate by Province ({latest_quarter})",
    fontsize=15
)

plt.xlabel("Province")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45, ha="right")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

# 8. Save the graph
Path("images").mkdir(exist_ok=True)

plt.savefig(
    "images/provincial_unemployment.png",
    dpi=300
)

plt.show()

print("\nProvincial analysis completed successfully!")
