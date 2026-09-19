import pandas as pd

# -------------------------------
# LOAD CRM ANALYTICS TABLE
# -------------------------------

fact_crm = pd.read_csv("fact_crm.csv")

print("CRM analytics table loaded successfully! ✅")


# -------------------------------
# CHECK CRM COLUMNS
# -------------------------------

print("\n========== CRM TABLE COLUMNS ==========")
print(fact_crm.columns.tolist())


# -------------------------------
# OVERALL CRM KPIs
# -------------------------------

print("\n========== OVERALL CRM KPIs ==========")

total_deal_value = fact_crm["Deal_Value"].sum()

total_expected_revenue = fact_crm["Expected_Revenue"].sum()

average_deal_value = fact_crm["Deal_Value"].mean()

total_deals = fact_crm.shape[0]

average_probability = fact_crm["Probability"].mean() * 100


print("Total Deals:", total_deals)

print(
    "Total Deal Value:",
    total_deal_value
)

print(
    "Total Expected Revenue:",
    total_expected_revenue
)

print(
    "Average Deal Value:",
    average_deal_value
)

print(
    "Average Deal Probability %:",
    average_probability
)


# -------------------------------
# CRM STAGE PERFORMANCE ANALYSIS
# -------------------------------

print("\n========== CRM PERFORMANCE ANALYSIS ==========")

crm_analysis = (
    fact_crm
    .groupby("Stage", as_index=False)
    .agg(
        Total_Deals=("Lead_ID", "nunique"),
        Total_Deal_Value=("Deal_Value", "sum"),
        Total_Expected_Revenue=("Expected_Revenue", "sum"),
        Average_Probability=("Probability", "mean")
    )
)


# -------------------------------
# CONVERT PROBABILITY TO %
# -------------------------------

crm_analysis["Average_Probability_%"] = (
    crm_analysis["Average_Probability"] * 100
)


print(crm_analysis)


# -------------------------------
# TOP STAGES BY DEAL VALUE
# -------------------------------

print("\n========== TOP CRM STAGES BY DEAL VALUE ==========")

top_value_stages = (
    crm_analysis
    .sort_values(
        by="Total_Deal_Value",
        ascending=False
    )
)

print(top_value_stages)


# -------------------------------
# TOP STAGES BY EXPECTED REVENUE
# -------------------------------

print("\n========== TOP CRM STAGES BY EXPECTED REVENUE ==========")

top_revenue_stages = (
    crm_analysis
    .sort_values(
        by="Total_Expected_Revenue",
        ascending=False
    )
)

print(top_revenue_stages)


# -------------------------------
# HIGHEST PROBABILITY STAGES
# -------------------------------

print("\n========== HIGHEST PROBABILITY CRM STAGES ==========")

highest_probability_stages = (
    crm_analysis
    .sort_values(
        by="Average_Probability_%",
        ascending=False
    )
)

print(highest_probability_stages)


# -------------------------------
# TOP 10 DEALS BY DEAL VALUE
# -------------------------------

print("\n========== TOP 10 DEALS BY DEAL VALUE ==========")

top_deals = (
    fact_crm
    .sort_values(
        by="Deal_Value",
        ascending=False
    )
    .head(10)
)

print(top_deals)


# -------------------------------
# TOP 10 DEALS BY EXPECTED REVENUE
# -------------------------------

print("\n========== TOP 10 DEALS BY EXPECTED REVENUE ==========")

top_expected_revenue_deals = (
    fact_crm
    .sort_values(
        by="Expected_Revenue",
        ascending=False
    )
    .head(10)
)

print(top_expected_revenue_deals)


# -------------------------------
# SAVE CRM ANALYSIS FILES
# -------------------------------

crm_analysis.to_csv(
    "crm_stage_analysis.csv",
    index=False
)

top_deals.to_csv(
    "top_10_crm_deals.csv",
    index=False
)

top_expected_revenue_deals.to_csv(
    "top_10_expected_revenue_deals.csv",
    index=False
)

print("\n✅ CRM analysis files saved successfully!")


# -------------------------------
# HIGHEST VALUE STAGE
# -------------------------------

highest_value_stage = (
    crm_analysis
    .sort_values(
        by="Total_Deal_Value",
        ascending=False
    )
    .iloc[0]
)

print("\n========== HIGHEST VALUE CRM STAGE ==========")

print(
    "Stage:",
    highest_value_stage["Stage"]
)

print(
    "Total Deal Value:",
    highest_value_stage["Total_Deal_Value"]
)

print(
    "Expected Revenue:",
    highest_value_stage["Total_Expected_Revenue"]
)


# -------------------------------
# HIGHEST EXPECTED REVENUE STAGE
# -------------------------------

highest_revenue_stage = (
    crm_analysis
    .sort_values(
        by="Total_Expected_Revenue",
        ascending=False
    )
    .iloc[0]
)

print("\n========== HIGHEST EXPECTED REVENUE STAGE ==========")

print(
    "Stage:",
    highest_revenue_stage["Stage"]
)

print(
    "Expected Revenue:",
    highest_revenue_stage["Total_Expected_Revenue"]
)

print(
    "Average Probability %:",
    highest_revenue_stage["Average_Probability_%"]
)


# -------------------------------
# HIGHEST VALUE DEAL
# -------------------------------

highest_value_deal = (
    fact_crm
    .sort_values(
        by="Deal_Value",
        ascending=False
    )
    .iloc[0]
)

print("\n========== HIGHEST VALUE DEAL ==========")

print(
    "Lead ID:",
    highest_value_deal["Lead_ID"]
)

print(
    "Deal Value:",
    highest_value_deal["Deal_Value"]
)

print(
    "Expected Revenue:",
    highest_value_deal["Expected_Revenue"]
)

print(
    "Probability:",
    highest_value_deal["Probability"] * 100
)


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n==========================================")
print("CRM PERFORMANCE ANALYSIS COMPLETED!")
print("==========================================")

print("✅ Overall CRM KPIs Calculated!")
print("✅ CRM Stage Performance Analyzed!")
print("✅ Deal Value Analysis Completed!")
print("✅ Expected Revenue Analysis Completed!")
print("✅ Probability Analysis Completed!")
print("✅ Top CRM Deals Identified!")
print("✅ CRM Analysis Files Saved Successfully!")

print("\n🎉 CRM ANALYSIS COMPLETED SUCCESSFULLY!")