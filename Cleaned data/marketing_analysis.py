import pandas as pd

# -------------------------------
# LOAD ANALYTICS TABLE
# -------------------------------

fact_marketing = pd.read_csv("fact_marketing.csv")

print("Marketing analytics table loaded successfully! ✅")


# -------------------------------
# CHECK COLUMNS
# -------------------------------

print("\n========== MARKETING TABLE COLUMNS ==========")
print(fact_marketing.columns.tolist())


# -------------------------------
# OVERALL MARKETING KPIs
# -------------------------------

print("\n========== OVERALL MARKETING KPIs ==========")

total_leads = fact_marketing["Leads"].sum()
total_conversions = fact_marketing["Conversions"].sum()
total_spend = fact_marketing["Spend"].sum()

overall_conversion_rate = (
    total_conversions / total_leads
) * 100

overall_cost_per_lead = (
    total_spend / total_leads
)

overall_cost_per_conversion = (
    total_spend / total_conversions
)

print("Total Leads:", total_leads)
print("Total Conversions:", total_conversions)
print("Total Marketing Spend:", total_spend)
print("Overall Conversion Rate %:", overall_conversion_rate)
print("Overall Cost Per Lead:", overall_cost_per_lead)
print("Overall Cost Per Conversion:", overall_cost_per_conversion)


# -------------------------------
# CAMPAIGN PERFORMANCE
# -------------------------------

print("\n========== CAMPAIGN PERFORMANCE ==========")

campaign_analysis = (
    fact_marketing
    .groupby("Campaign_Name", as_index=False)
    .agg(
        Total_Leads=("Leads", "sum"),
        Total_Conversions=("Conversions", "sum"),
        Total_Spend=("Spend", "sum")
    )
)


# -------------------------------
# CAMPAIGN KPIs
# -------------------------------

campaign_analysis["Conversion_Rate_%"] = (
    campaign_analysis["Total_Conversions"]
    / campaign_analysis["Total_Leads"]
) * 100

campaign_analysis["Cost_Per_Lead"] = (
    campaign_analysis["Total_Spend"]
    / campaign_analysis["Total_Leads"]
)

campaign_analysis["Cost_Per_Conversion"] = (
    campaign_analysis["Total_Spend"]
    / campaign_analysis["Total_Conversions"]
)

print(campaign_analysis)


# -------------------------------
# TOP CAMPAIGNS BY CONVERSIONS
# -------------------------------

print("\n========== TOP CAMPAIGNS BY CONVERSIONS ==========")

top_conversion_campaigns = (
    campaign_analysis
    .sort_values(
        by="Total_Conversions",
        ascending=False
    )
    .head(10)
)

print(top_conversion_campaigns)


# -------------------------------
# BEST CAMPAIGNS BY CONVERSION RATE
# -------------------------------

print("\n========== BEST CAMPAIGNS BY CONVERSION RATE ==========")

best_conversion_rate_campaigns = (
    campaign_analysis
    .sort_values(
        by="Conversion_Rate_%",
        ascending=False
    )
    .head(10)
)

print(best_conversion_rate_campaigns)


# -------------------------------
# MOST EFFICIENT CAMPAIGNS
# -------------------------------

print("\n========== MOST EFFICIENT CAMPAIGNS ==========")

most_efficient_campaigns = (
    campaign_analysis
    .sort_values(
        by="Cost_Per_Conversion",
        ascending=True
    )
    .head(10)
)

print(most_efficient_campaigns)


# -------------------------------
# HIGHEST SPENDING CAMPAIGNS
# -------------------------------

print("\n========== HIGHEST SPENDING CAMPAIGNS ==========")

highest_spending_campaigns = (
    campaign_analysis
    .sort_values(
        by="Total_Spend",
        ascending=False
    )
    .head(10)
)

print(highest_spending_campaigns)


# -------------------------------
# CHANNEL PERFORMANCE ANALYSIS
# -------------------------------

print("\n========== CHANNEL PERFORMANCE ==========")

channel_analysis = (
    fact_marketing
    .groupby("Channel", as_index=False)
    .agg(
        Total_Leads=("Leads", "sum"),
        Total_Conversions=("Conversions", "sum"),
        Total_Spend=("Spend", "sum")
    )
)

channel_analysis["Conversion_Rate_%"] = (
    channel_analysis["Total_Conversions"]
    / channel_analysis["Total_Leads"]
) * 100

channel_analysis["Cost_Per_Lead"] = (
    channel_analysis["Total_Spend"]
    / channel_analysis["Total_Leads"]
)

channel_analysis["Cost_Per_Conversion"] = (
    channel_analysis["Total_Spend"]
    / channel_analysis["Total_Conversions"]
)

print(channel_analysis)


# -------------------------------
# BEST CHANNEL BY CONVERSIONS
# -------------------------------

print("\n========== BEST CHANNEL BY CONVERSIONS ==========")

best_channel = (
    channel_analysis
    .sort_values(
        by="Total_Conversions",
        ascending=False
    )
    .iloc[0]
)

print(
    "Best Channel:",
    best_channel["Channel"]
)

print(
    "Total Conversions:",
    best_channel["Total_Conversions"]
)

print(
    "Conversion Rate %:",
    best_channel["Conversion_Rate_%"]
)


# -------------------------------
# SAVE ANALYSIS FILES
# -------------------------------

campaign_analysis.to_csv(
    "campaign_performance_analysis.csv",
    index=False
)

top_conversion_campaigns.to_csv(
    "top_campaigns_by_conversions.csv",
    index=False
)

best_conversion_rate_campaigns.to_csv(
    "best_campaigns_by_conversion_rate.csv",
    index=False
)

most_efficient_campaigns.to_csv(
    "most_efficient_campaigns.csv",
    index=False
)

channel_analysis.to_csv(
    "channel_performance_analysis.csv",
    index=False
)

print("\n✅ Marketing analysis files saved successfully!")


# -------------------------------
# BEST CAMPAIGN BY CONVERSIONS
# -------------------------------

best_campaign_conversions = (
    campaign_analysis
    .sort_values(
        by="Total_Conversions",
        ascending=False
    )
    .iloc[0]
)

print("\n========== BEST CAMPAIGN BY CONVERSIONS ==========")

print(
    "Campaign:",
    best_campaign_conversions["Campaign_Name"]
)

print(
    "Total Conversions:",
    best_campaign_conversions["Total_Conversions"]
)

print(
    "Conversion Rate %:",
    best_campaign_conversions["Conversion_Rate_%"]
)


# -------------------------------
# BEST CAMPAIGN BY CONVERSION RATE
# -------------------------------

best_campaign_rate = (
    campaign_analysis
    .sort_values(
        by="Conversion_Rate_%",
        ascending=False
    )
    .iloc[0]
)

print("\n========== BEST CAMPAIGN BY CONVERSION RATE ==========")

print(
    "Campaign:",
    best_campaign_rate["Campaign_Name"]
)

print(
    "Conversion Rate %:",
    best_campaign_rate["Conversion_Rate_%"]
)

print(
    "Total Leads:",
    best_campaign_rate["Total_Leads"]
)

print(
    "Total Conversions:",
    best_campaign_rate["Total_Conversions"]
)


# -------------------------------
# MOST COST-EFFICIENT CAMPAIGN
# -------------------------------

most_efficient_campaign = (
    campaign_analysis
    .sort_values(
        by="Cost_Per_Conversion",
        ascending=True
    )
    .iloc[0]
)

print("\n========== MOST COST-EFFICIENT CAMPAIGN ==========")

print(
    "Campaign:",
    most_efficient_campaign["Campaign_Name"]
)

print(
    "Cost Per Conversion:",
    most_efficient_campaign["Cost_Per_Conversion"]
)

print(
    "Total Spend:",
    most_efficient_campaign["Total_Spend"]
)


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n==========================================")
print("MARKETING PERFORMANCE ANALYSIS COMPLETED!")
print("==========================================")

print("✅ Overall Marketing KPIs Calculated!")
print("✅ Campaign Performance Analyzed!")
print("✅ Conversion Rate Calculated!")
print("✅ Cost Per Lead Calculated!")
print("✅ Cost Per Conversion Calculated!")
print("✅ Channel Performance Analyzed!")
print("✅ Top Campaigns Identified!")
print("✅ Most Efficient Campaign Identified!")
print("✅ Analysis Files Saved Successfully!")

print("\n🎉 MARKETING ANALYSIS COMPLETED SUCCESSFULLY!")