import pandas as pd

# -------------------------------
# LOAD ANALYTICS TABLES
# -------------------------------

fact_orders = pd.read_csv("fact_orders.csv")
dim_customers = pd.read_csv("dim_customers.csv")

print("Analytics tables loaded successfully! ✅")


# -------------------------------
# CUSTOMER PERFORMANCE ANALYSIS
# -------------------------------

print("\n========== CUSTOMER PERFORMANCE ANALYSIS ==========")

customer_analysis = (
    fact_orders
    .groupby("Customer_ID", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order_ID", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )
)


# -------------------------------
# CALCULATE CUSTOMER PROFIT MARGIN
# -------------------------------

customer_analysis["Profit_Margin_%"] = (
    customer_analysis["Total_Profit"]
    / customer_analysis["Total_Sales"]
) * 100


# -------------------------------
# ADD CUSTOMER INFORMATION
# -------------------------------

customer_columns = [
    col for col in dim_customers.columns
    if col != "Customer_ID"
]

customer_analysis = pd.merge(
    customer_analysis,
    dim_customers,
    on="Customer_ID",
    how="left"
)


# -------------------------------
# TOP 10 CUSTOMERS BY SALES
# -------------------------------

print("\n========== TOP 10 CUSTOMERS BY SALES ==========")

top_sales_customers = (
    customer_analysis
    .sort_values(
        by="Total_Sales",
        ascending=False
    )
    .head(10)
)

print(top_sales_customers)


# -------------------------------
# TOP 10 CUSTOMERS BY PROFIT
# -------------------------------

print("\n========== TOP 10 CUSTOMERS BY PROFIT ==========")

top_profit_customers = (
    customer_analysis
    .sort_values(
        by="Total_Profit",
        ascending=False
    )
    .head(10)
)

print(top_profit_customers)


# -------------------------------
# TOP 10 CUSTOMERS BY ORDERS
# -------------------------------

print("\n========== TOP 10 CUSTOMERS BY ORDER COUNT ==========")

top_order_customers = (
    customer_analysis
    .sort_values(
        by="Total_Orders",
        ascending=False
    )
    .head(10)
)

print(top_order_customers)


# -------------------------------
# LOWEST PERFORMING CUSTOMERS
# -------------------------------

print("\n========== LOWEST PERFORMING CUSTOMERS ==========")

lowest_sales_customers = (
    customer_analysis
    .sort_values(
        by="Total_Sales",
        ascending=True
    )
    .head(10)
)

print(lowest_sales_customers)


# -------------------------------
# SAVE COMPLETE ANALYSIS
# -------------------------------

customer_analysis.to_csv(
    "customer_performance_analysis.csv",
    index=False
)

top_sales_customers.to_csv(
    "top_10_customers_by_sales.csv",
    index=False
)

top_profit_customers.to_csv(
    "top_10_customers_by_profit.csv",
    index=False
)

top_order_customers.to_csv(
    "top_10_customers_by_orders.csv",
    index=False
)


# -------------------------------
# BEST CUSTOMER BY SALES
# -------------------------------

best_sales_customer = (
    customer_analysis
    .sort_values(
        by="Total_Sales",
        ascending=False
    )
    .iloc[0]
)

print("\n========== BEST CUSTOMER BY SALES ==========")

print(
    "Customer ID:",
    best_sales_customer["Customer_ID"]
)

print(
    "Total Sales:",
    best_sales_customer["Total_Sales"]
)

print(
    "Total Profit:",
    best_sales_customer["Total_Profit"]
)

print(
    "Total Orders:",
    best_sales_customer["Total_Orders"]
)


# -------------------------------
# BEST CUSTOMER BY PROFIT
# -------------------------------

best_profit_customer = (
    customer_analysis
    .sort_values(
        by="Total_Profit",
        ascending=False
    )
    .iloc[0]
)

print("\n========== BEST CUSTOMER BY PROFIT ==========")

print(
    "Customer ID:",
    best_profit_customer["Customer_ID"]
)

print(
    "Total Profit:",
    best_profit_customer["Total_Profit"]
)

print(
    "Total Sales:",
    best_profit_customer["Total_Sales"]
)


# -------------------------------
# MOST FREQUENT CUSTOMER
# -------------------------------

most_frequent_customer = (
    customer_analysis
    .sort_values(
        by="Total_Orders",
        ascending=False
    )
    .iloc[0]
)

print("\n========== MOST FREQUENT CUSTOMER ==========")

print(
    "Customer ID:",
    most_frequent_customer["Customer_ID"]
)

print(
    "Total Orders:",
    most_frequent_customer["Total_Orders"]
)

print(
    "Total Sales:",
    most_frequent_customer["Total_Sales"]
)


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n==========================================")
print("CUSTOMER PERFORMANCE ANALYSIS COMPLETED!")
print("==========================================")

print("✅ Customer-wise Sales Analysis Completed!")
print("✅ Customer-wise Profit Analysis Completed!")
print("✅ Customer Order Frequency Analysis Completed!")
print("✅ Top Customers Identified!")
print("✅ Low-performing Customers Identified!")
print("✅ Analysis Files Saved Successfully!")

print("\n🎉 CUSTOMER ANALYSIS COMPLETED SUCCESSFULLY!")
