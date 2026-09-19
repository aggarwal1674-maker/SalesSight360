import pandas as pd

# -------------------------------
# LOAD ANALYTICS TABLE
# -------------------------------

fact_orders = pd.read_csv("fact_orders.csv")

print("Fact Orders table loaded successfully! ✅")


# -------------------------------
# CHECK AVAILABLE COLUMNS
# -------------------------------

print("\n========== ORDERS TABLE COLUMNS ==========")
print(fact_orders.columns.tolist())


# -------------------------------
# CONVERT ORDER DATE
# -------------------------------

fact_orders["Order_Date"] = pd.to_datetime(
    fact_orders["Order_Date"]
)

print("\nOrder_Date converted successfully! ✅")


# -------------------------------
# CREATE MONTH COLUMN
# -------------------------------

fact_orders["Month"] = (
    fact_orders["Order_Date"]
    .dt.to_period("M")
    .astype(str)
)

print("Month column created successfully! ✅")


# -------------------------------
# MONTHLY SALES ANALYSIS
# -------------------------------

print("\n========== MONTHLY SALES ANALYSIS ==========")

monthly_sales = (
    fact_orders
    .groupby("Month", as_index=False)["Sales"]
    .sum()
)

monthly_sales = monthly_sales.rename(
    columns={
        "Sales": "Total_Sales"
    }
)

print(monthly_sales)


# -------------------------------
# MONTHLY PROFIT ANALYSIS
# -------------------------------

print("\n========== MONTHLY PROFIT ANALYSIS ==========")

monthly_profit = (
    fact_orders
    .groupby("Month", as_index=False)["Profit"]
    .sum()
)

monthly_profit = monthly_profit.rename(
    columns={
        "Profit": "Total_Profit"
    }
)

print(monthly_profit)


# -------------------------------
# MONTHLY ORDER COUNT
# -------------------------------

print("\n========== MONTHLY ORDER ANALYSIS ==========")

monthly_orders = (
    fact_orders
    .groupby("Month", as_index=False)["Order_ID"]
    .nunique()
)

monthly_orders = monthly_orders.rename(
    columns={
        "Order_ID": "Total_Orders"
    }
)

print(monthly_orders)


# -------------------------------
# COMBINE MONTHLY ANALYSIS
# -------------------------------

print("\n========== COMBINED MONTHLY ANALYSIS ==========")

monthly_analysis = pd.merge(
    monthly_sales,
    monthly_profit,
    on="Month"
)

monthly_analysis = pd.merge(
    monthly_analysis,
    monthly_orders,
    on="Month"
)

print(monthly_analysis)


# -------------------------------
# CALCULATE MONTHLY GROWTH
# -------------------------------

monthly_analysis["Sales_Growth_%"] = (
    monthly_analysis["Total_Sales"]
    .pct_change()
    * 100
)

print("\n========== MONTHLY GROWTH ANALYSIS ==========")

print(monthly_analysis)


# -------------------------------
# SAVE MONTHLY ANALYSIS
# -------------------------------

monthly_analysis.to_csv(
    "sales_trend_analysis.csv",
    index=False
)

print("\n✅ SALES TREND ANALYSIS SAVED SUCCESSFULLY!")


# -------------------------------
# FIND BEST SALES MONTH
# -------------------------------

best_sales_month = monthly_analysis.loc[
    monthly_analysis["Total_Sales"].idxmax()
]

print("\n========== BEST SALES MONTH ==========")

print(
    "Best Sales Month:",
    best_sales_month["Month"]
)

print(
    "Highest Sales:",
    best_sales_month["Total_Sales"]
)


# -------------------------------
# FIND BEST PROFIT MONTH
# -------------------------------

best_profit_month = monthly_analysis.loc[
    monthly_analysis["Total_Profit"].idxmax()
]

print("\n========== BEST PROFIT MONTH ==========")

print(
    "Best Profit Month:",
    best_profit_month["Month"]
)

print(
    "Highest Profit:",
    best_profit_month["Total_Profit"]
)


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n==========================================")
print("SALES TREND ANALYSIS COMPLETED!")
print("==========================================")

print("✅ Monthly Sales Analysis Completed!")
print("✅ Monthly Profit Analysis Completed!")
print("✅ Monthly Order Analysis Completed!")
print("✅ Monthly Growth Analysis Completed!")
print("✅ Best Sales Month Identified!")
print("✅ Best Profit Month Identified!")

print("\n🎉 SALES TREND ANALYSIS COMPLETED SUCCESSFULLY!")