import pandas as pd

# -------------------------------
# LOAD ANALYTICS TABLES
# -------------------------------

fact_orders = pd.read_csv("fact_orders.csv")
dim_products = pd.read_csv("dim_products.csv")

print("Analytics tables loaded successfully! ✅")


# -------------------------------
# PRODUCT PERFORMANCE ANALYSIS
# -------------------------------

print("\n========== PRODUCT PERFORMANCE ANALYSIS ==========")

product_analysis = (
    fact_orders
    .groupby("Product_ID", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Order_ID", "nunique")
    )
)

# -------------------------------
# CALCULATE PROFIT MARGIN
# -------------------------------

product_analysis["Profit_Margin_%"] = (
    product_analysis["Total_Profit"]
    / product_analysis["Total_Sales"]
) * 100


# -------------------------------
# ADD PRODUCT INFORMATION
# -------------------------------

product_columns = [
    col for col in dim_products.columns
    if col != "Product_ID"
]

product_analysis = pd.merge(
    product_analysis,
    dim_products,
    on="Product_ID",
    how="left"
)


# -------------------------------
# SORT BY SALES
# -------------------------------

product_analysis = product_analysis.sort_values(
    by="Total_Sales",
    ascending=False
)


# -------------------------------
# TOP 10 PRODUCTS BY SALES
# -------------------------------

print("\n========== TOP 10 PRODUCTS BY SALES ==========")

top_sales_products = product_analysis.head(10)

print(top_sales_products)


# -------------------------------
# TOP 10 PRODUCTS BY PROFIT
# -------------------------------

print("\n========== TOP 10 PRODUCTS BY PROFIT ==========")

top_profit_products = (
    product_analysis
    .sort_values(
        by="Total_Profit",
        ascending=False
    )
    .head(10)
)

print(top_profit_products)


# -------------------------------
# TOP 10 PRODUCTS BY QUANTITY
# -------------------------------

print("\n========== TOP 10 PRODUCTS BY QUANTITY ==========")

top_quantity_products = (
    product_analysis
    .sort_values(
        by="Total_Quantity",
        ascending=False
    )
    .head(10)
)

print(top_quantity_products)


# -------------------------------
# LOWEST PERFORMING PRODUCTS
# -------------------------------

print("\n========== LOWEST PERFORMING PRODUCTS ==========")

lowest_sales_products = (
    product_analysis
    .sort_values(
        by="Total_Sales",
        ascending=True
    )
    .head(10)
)

print(lowest_sales_products)


# -------------------------------
# SAVE COMPLETE ANALYSIS
# -------------------------------

product_analysis.to_csv(
    "product_performance_analysis.csv",
    index=False
)

# Save top product reports

top_sales_products.to_csv(
    "top_10_products_by_sales.csv",
    index=False
)

top_profit_products.to_csv(
    "top_10_products_by_profit.csv",
    index=False
)

top_quantity_products.to_csv(
    "top_10_products_by_quantity.csv",
    index=False
)


# -------------------------------
# BEST PRODUCT BY SALES
# -------------------------------

best_sales_product = product_analysis.iloc[0]

print("\n========== BEST PRODUCT BY SALES ==========")

print(
    "Product ID:",
    best_sales_product["Product_ID"]
)

print(
    "Total Sales:",
    best_sales_product["Total_Sales"]
)

print(
    "Total Profit:",
    best_sales_product["Total_Profit"]
)


# -------------------------------
# BEST PRODUCT BY PROFIT
# -------------------------------

best_profit_product = (
    product_analysis
    .sort_values(
        by="Total_Profit",
        ascending=False
    )
    .iloc[0]
)

print("\n========== BEST PRODUCT BY PROFIT ==========")

print(
    "Product ID:",
    best_profit_product["Product_ID"]
)

print(
    "Total Profit:",
    best_profit_product["Total_Profit"]
)

print(
    "Total Sales:",
    best_profit_product["Total_Sales"]
)


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n==========================================")
print("PRODUCT PERFORMANCE ANALYSIS COMPLETED!")
print("==========================================")

print("✅ Product-wise Sales Analysis Completed!")
print("✅ Product-wise Profit Analysis Completed!")
print("✅ Product-wise Quantity Analysis Completed!")
print("✅ Product-wise Profit Margin Calculated!")
print("✅ Top Products Identified!")
print("✅ Low-performing Products Identified!")
print("✅ Analysis Files Saved Successfully!")

print("\n🎉 PRODUCT ANALYSIS COMPLETED SUCCESSFULLY!")