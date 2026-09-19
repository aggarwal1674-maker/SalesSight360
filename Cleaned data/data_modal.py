import pandas as pd

# -------------------------------
# LOAD CLEANED DATASETS
# -------------------------------

customers = pd.read_csv("customers_cleaned.csv")
orders = pd.read_csv("orders_cleaned.csv")
products = pd.read_csv("products_cleaned.csv")
payments = pd.read_csv("payments_cleaned.csv")
marketing = pd.read_csv("marketing_cleaned.csv")
crm = pd.read_csv("crm_cleaned.csv")
target = pd.read_csv("target_cleaned.csv")

print("All cleaned datasets loaded successfully! ✅")


# -------------------------------
# DATA MODEL VALIDATION
# -------------------------------

print("\n========== DATA MODEL VALIDATION ==========")


# 1. Check Customer_ID relationship
print("\n1. CUSTOMER - ORDER RELATIONSHIP")

missing_customers = orders[
    ~orders["Customer_ID"].isin(customers["Customer_ID"])
]

print("Orders with invalid Customer_ID:", len(missing_customers))


# 2. Check Product_ID relationship
print("\n2. PRODUCT - ORDER RELATIONSHIP")

missing_products = orders[
    ~orders["Product_ID"].isin(products["Product_ID"])
]

print("Orders with invalid Product_ID:", len(missing_products))


# 3. Check Order_ID relationship
print("\n3. ORDER - PAYMENT RELATIONSHIP")

missing_orders = payments[
    ~payments["Order_ID"].isin(orders["Order_ID"])
]

print("Payments with invalid Order_ID:", len(missing_orders))


# -------------------------------
# DISPLAY DATA MODEL SUMMARY
# -------------------------------

print("\n========== DATA MODEL SUMMARY ==========")

print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Products:", products.shape)
print("Payments:", payments.shape)
print("Marketing:", marketing.shape)
print("CRM:", crm.shape)
print("Target:", target.shape)


# -------------------------------
# FINAL RESULT
# -------------------------------

if (
    len(missing_customers) == 0
    and len(missing_products) == 0
    and len(missing_orders) == 0
):
    print("\n✅ ALL CORE DATA RELATIONSHIPS ARE VALID!")
    print("DATA MODEL VALIDATION COMPLETED SUCCESSFULLY! 🎉")
else:
    print("\n⚠️ SOME DATA RELATIONSHIPS NEED ATTENTION.")

# -------------------------------
# CREATE ANALYTICS DATA MODEL
# -------------------------------

print("\n========== CREATING ANALYTICS DATA MODEL ==========")


# -------------------------------
# 1. DIMENSION TABLES
# -------------------------------

# Customer Dimension
dim_customers = customers.copy()

# Product Dimension
dim_products = products.copy()


# -------------------------------
# 2. FACT TABLES
# -------------------------------

# Orders Fact Table
fact_orders = orders.copy()

# Payments Fact Table
fact_payments = payments.copy()

# CRM Fact Table
fact_crm = crm.copy()

# Marketing Fact Table
fact_marketing = marketing.copy()

# Target Fact Table
fact_target = target.copy()


# -------------------------------
# 3. CREATE KPI COLUMNS
# -------------------------------

# Profit Margin %
fact_orders["Profit_Margin"] = (
    fact_orders["Profit"] / fact_orders["Sales"]
) * 100

# Discount Amount
fact_orders["Discount_Amount"] = (
    fact_orders["Sales"] * fact_orders["Discount"]
)

# Net Sales after Discount
fact_orders["Net_Sales"] = (
    fact_orders["Sales"] - fact_orders["Discount_Amount"]
)


# -------------------------------
# 4. CRM KPI
# -------------------------------

# Expected Deal Value
fact_crm["Expected_Revenue"] = (
    fact_crm["Deal_Value"] * fact_crm["Probability"]
)


# -------------------------------
# 5. MARKETING KPI
# -------------------------------

# Conversion Rate %
fact_marketing["Conversion_Rate"] = (
    fact_marketing["Conversions"] / fact_marketing["Leads"]
) * 100

# Cost per Lead
fact_marketing["Cost_Per_Lead"] = (
    fact_marketing["Spend"] / fact_marketing["Leads"]
)

# Cost per Conversion
fact_marketing["Cost_Per_Conversion"] = (
    fact_marketing["Spend"] / fact_marketing["Conversions"]
)


# -------------------------------
# 6. SAVE ANALYTICS TABLES
# -------------------------------

dim_customers.to_csv(
    "dim_customers.csv",
    index=False
)

dim_products.to_csv(
    "dim_products.csv",
    index=False
)

fact_orders.to_csv(
    "fact_orders.csv",
    index=False
)

fact_payments.to_csv(
    "fact_payments.csv",
    index=False
)

fact_crm.to_csv(
    "fact_crm.csv",
    index=False
)

fact_marketing.to_csv(
    "fact_marketing.csv",
    index=False
)

fact_target.to_csv(
    "fact_target.csv",
    index=False
)


# -------------------------------
# 7. DISPLAY FINAL MODEL
# -------------------------------

print("\n========== ANALYTICS DATA MODEL ==========")

print("Dimension Tables:")
print("DIM_CUSTOMERS:", dim_customers.shape)
print("DIM_PRODUCTS:", dim_products.shape)

print("\nFact Tables:")
print("FACT_ORDERS:", fact_orders.shape)
print("FACT_PAYMENTS:", fact_payments.shape)
print("FACT_CRM:", fact_crm.shape)
print("FACT_MARKETING:", fact_marketing.shape)
print("FACT_TARGET:", fact_target.shape)


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n✅ ANALYTICS DATA MODEL CREATED SUCCESSFULLY!")
print("✅ KPI COLUMNS CREATED SUCCESSFULLY!")
print("✅ ANALYTICS TABLES SAVED SUCCESSFULLY! 🎉")
