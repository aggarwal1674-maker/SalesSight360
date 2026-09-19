import pandas as pd
import os

# Data folder path
DATA_FOLDER = "data"

# Read CSV files
customers = pd.read_csv(os.path.join(DATA_FOLDER, "customers.csv"))
orders = pd.read_csv(os.path.join(DATA_FOLDER, "orders.csv"))
products = pd.read_csv(os.path.join(DATA_FOLDER, "products.csv"))
payments = pd.read_csv(os.path.join(DATA_FOLDER, "payments.csv"))
marketing = pd.read_csv(os.path.join(DATA_FOLDER, "marketing.csv"))
crm = pd.read_csv(os.path.join(DATA_FOLDER, "crm.csv"))
target = pd.read_csv(os.path.join(DATA_FOLDER, "target.csv"))

print("All data files loaded successfully!")

print("\nCustomers:", customers.shape)
print("Orders:", orders.shape)
print("Products:", products.shape)
print("Payments:", payments.shape)
print("Marketing:", marketing.shape)
print("CRM:", crm.shape)
print("Target:", target.shape)

# -------------------------------
# TRANSFORM: DATA CLEANING
# -------------------------------

# Remove duplicate rows
customers = customers.drop_duplicates()
orders = orders.drop_duplicates()
products = products.drop_duplicates()
payments = payments.drop_duplicates()
marketing = marketing.drop_duplicates()
crm = crm.drop_duplicates()
target = target.drop_duplicates()

# Remove extra spaces from column names
customers.columns = customers.columns.str.strip()
orders.columns = orders.columns.str.strip()
products.columns = products.columns.str.strip()
payments.columns = payments.columns.str.strip()
marketing.columns = marketing.columns.str.strip()
crm.columns = crm.columns.str.strip()
target.columns = target.columns.str.strip()

# Convert date columns
orders["Order_Date"] = pd.to_datetime(
    orders["Order_Date"],
    errors="coerce"
)

crm["Lead_Date"] = pd.to_datetime(
    crm["Lead_Date"],
    errors="coerce"
)

crm["Close_Date"] = pd.to_datetime(
    crm["Close_Date"],
    errors="coerce"
)

# Fill missing numerical values with 0
for df in [orders, payments, marketing, crm, target]:
    numeric_columns = df.select_dtypes(include="number").columns
    df[numeric_columns] = df[numeric_columns].fillna(0)

# Remove leading/trailing spaces from text columns
for df in [
    customers,
    orders,
    products,
    payments,
    marketing,
    crm,
    target
]:
    text_columns = df.select_dtypes(include="object").columns
    for col in text_columns:
        df[col] = df[col].str.strip()

print("\nData cleaning completed successfully!")

# -------------------------------
# LOAD: SAVE CLEANED DATA
# -------------------------------

OUTPUT_FOLDER = "."

# Save cleaned datasets
customers.to_csv("customers_cleaned.csv", index=False)
orders.to_csv("orders_cleaned.csv", index=False)
products.to_csv("products_cleaned.csv", index=False)
payments.to_csv("payments_cleaned.csv", index=False)
marketing.to_csv("marketing_cleaned.csv", index=False)
crm.to_csv("crm_cleaned.csv", index=False)
target.to_csv("target_cleaned.csv", index=False)

print("\nCleaned datasets saved successfully!")
print("ETL PROCESS COMPLETED SUCCESSFULLY! 🎉")

# -------------------------------
# VALIDATE: CHECK CLEANED DATA
# -------------------------------

print("\n========== CLEANED DATA VALIDATION ==========")

datasets = {
    "Customers": customers,
    "Orders": orders,
    "Products": products,
    "Payments": payments,
    "Marketing": marketing,
    "CRM": crm,
    "Target": target
}

for name, df in datasets.items():
    print(f"\n{name}")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Missing Values:")
    print(df.isnull().sum())
    print("-" * 50)

print("\nDATA VALIDATION COMPLETED SUCCESSFULLY! ✅")