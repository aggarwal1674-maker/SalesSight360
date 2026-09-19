import pandas as pd

# -------------------------------
# LOAD ANALYTICS TABLES
# -------------------------------

fact_orders = pd.read_csv("fact_orders.csv")
fact_payments = pd.read_csv("fact_payments.csv")
fact_marketing = pd.read_csv("fact_marketing.csv")
fact_crm = pd.read_csv("fact_crm.csv")
fact_target = pd.read_csv("fact_target.csv")

print("All analytics tables loaded successfully! ✅")


# -------------------------------
# 1. SALES KPIs
# -------------------------------

print("\n========== SALES KPIs ==========")

total_sales = fact_orders["Sales"].sum()
total_profit = fact_orders["Profit"].sum()
total_orders = fact_orders["Order_ID"].nunique()
average_order_value = total_sales / total_orders

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)


# -------------------------------
# 2. PROFITABILITY KPIs
# -------------------------------

print("\n========== PROFITABILITY KPIs ==========")

overall_profit_margin = (
    total_profit / total_sales
) * 100

print("Overall Profit Margin %:", overall_profit_margin)


# -------------------------------
# 3. DISCOUNT & NET SALES KPIs
# -------------------------------

print("\n========== DISCOUNT KPIs ==========")

total_discount = fact_orders["Discount_Amount"].sum()
total_net_sales = fact_orders["Net_Sales"].sum()

print("Total Discount Amount:", total_discount)
print("Total Net Sales:", total_net_sales)


# -------------------------------
# 4. PAYMENT KPIs
# -------------------------------

print("\n========== PAYMENT KPIs ==========")

total_payment_amount = fact_payments["Amount"].sum()

print("Total Payment Amount:", total_payment_amount)

# -------------------------------
# 5. MARKETING KPIs
# -------------------------------

print("\n========== MARKETING KPIs ==========")

total_leads = fact_marketing["Leads"].sum()
total_conversions = fact_marketing["Conversions"].sum()
total_marketing_spend = fact_marketing["Spend"].sum()

overall_conversion_rate = (
    total_conversions / total_leads
) * 100

overall_cost_per_lead = (
    total_marketing_spend / total_leads
)

overall_cost_per_conversion = (
    total_marketing_spend / total_conversions
)

print("Total Leads:", total_leads)
print("Total Conversions:", total_conversions)
print("Total Marketing Spend:", total_marketing_spend)
print("Overall Conversion Rate %:", overall_conversion_rate)
print("Overall Cost Per Lead:", overall_cost_per_lead)
print("Overall Cost Per Conversion:", overall_cost_per_conversion)


# -------------------------------
# 6. CRM KPIs
# -------------------------------

print("\n========== CRM KPIs ==========")

total_deal_value = fact_crm["Deal_Value"].sum()
total_expected_revenue = fact_crm["Expected_Revenue"].sum()

print("Total Deal Value:", total_deal_value)
print("Total Expected Revenue:", total_expected_revenue)


# -------------------------------
# 7. TARGET KPIs
# -------------------------------

print("\n========== TARGET KPIs ==========")

print("Target Table Rows:", len(fact_target))

print("\nTarget Columns:")
print(fact_target.columns.tolist())


# -------------------------------
# FINAL KPI SUMMARY
# -------------------------------

print("\n========== FINAL KPI SUMMARY ==========")

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)
print("Overall Profit Margin %:", overall_profit_margin)
print("Total Net Sales:", total_net_sales)
print("Total Payment Amount:", total_payment_amount)
print("Total Leads:", total_leads)
print("Total Conversions:", total_conversions)
print("Overall Conversion Rate %:", overall_conversion_rate)
print("Total Deal Value:", total_deal_value)
print("Total Expected Revenue:", total_expected_revenue)

print("\n✅ KPI ANALYSIS COMPLETED SUCCESSFULLY! 🎉")