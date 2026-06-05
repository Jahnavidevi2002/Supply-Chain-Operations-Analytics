import pandas as pd
import numpy as np

print("Supply Chain Automation Pipeline Started")

# =====================================
# Load Dataset
# =====================================

df = pd.read_csv("cleaned_supply_chain.csv")

print("Dataset Loaded Successfully")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# =====================================
# High Risk SKU Report
# =====================================

high_risk = df[df["Risk Category"] == "High"]

high_risk[
    [
        "SKU",
        "Product type",
        "Stockout Risk Score",
        "Risk Category"
    ]
].to_csv(
    "high_risk_skus.csv",
    index=False
)

print("High Risk Report Generated")

# =====================================
# Excess Inventory Report
# =====================================

excess_inventory = df[
    df["Excess Inventory Flag"] == "Yes"
]

excess_inventory[
    [
        "SKU",
        "Product type",
        "Stock levels",
        "Number of products sold",
        "Excess Inventory Flag"
    ]
].to_csv(
    "excess_inventory_products.csv",
    index=False
)

print("Excess Inventory Report Generated")

# =====================================
# Supplier Risk Report
# =====================================

supplier_report = (
    df.groupby("Supplier name")
      .agg({
          "Lead times":"mean",
          "Defect rates":"mean",
          "Supplier Quality Score":"mean"
      })
      .reset_index()
)

supplier_report.to_csv(
    "supplier_risk_report.csv",
    index=False
)

print("Supplier Risk Report Generated")

print("=" * 50)
print("AUTOMATION PIPELINE COMPLETED")
print("=" * 50)