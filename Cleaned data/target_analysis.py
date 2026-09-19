import pandas as pd

# -------------------------------
# LOAD ANALYTICS TABLES
# -------------------------------

fact_orders = pd.read_csv("fact_orders.csv")
fact_target = pd.read_csv("fact_target.csv")

print("Analytics tables loaded successfully! ✅")


# -------------------------------
# DISPLAY AVAILABLE COLUMNS
# -------------------------------

print("\n========== ORDERS TABLE COLUMNS ==========")
print(fact_orders.columns.tolist())

print("\n========== TARGET TABLE COLUMNS ==========")
print(fact_target.columns.tolist())


# -------------------------------
# 1. ACTUAL SALES SUMMARY
# -------------------------------

print("\n========== ACTUAL SALES SUMMARY ==========")

total_actual_sales = fact_orders["Sales"].sum()

print("Total Actual Sales:", total_actual_sales)


# -------------------------------
# 2. TOTAL SALES TARGET
# -------------------------------

print("\n========== SALES TARGET SUMMARY ==========")

total_sales_target = fact_target["Sales_Target"].sum()

print("Total Sales Target:", total_sales_target)


# -------------------------------
# 3. TARGET VS ACTUAL
# -------------------------------

print("\n========== TARGET VS ACTUAL ==========")

sales_variance = (
    total_actual_sales - total_sales_target
)

target_achievement = (
    total_actual_sales / total_sales_target
) * 100

print("Actual Sales:", total_actual_sales)
print("Sales Target:", total_sales_target)
print("Sales Variance:", sales_variance)
print("Target Achievement %:", target_achievement)


# -------------------------------
# 4. REGION-WISE ANALYSIS
# -------------------------------

print("\n========== REGION-WISE TARGET ANALYSIS ==========")

if "Region" in fact_orders.columns and "Region" in fact_target.columns:

    region_actual_sales = (
        fact_orders
        .groupby("Region", as_index=False)["Sales"]
        .sum()
    )

    region_target_sales = (
        fact_target
        .groupby("Region", as_index=False)["Sales_Target"]
        .sum()
    )

    region_analysis = pd.merge(
        region_actual_sales,
        region_target_sales,
        on="Region",
        how="outer"
    )

    region_analysis["Sales"] = (
        region_analysis["Sales"].fillna(0)
    )

    region_analysis["Sales_Target"] = (
        region_analysis["Sales_Target"].fillna(0)
    )

    region_analysis["Sales_Variance"] = (
        region_analysis["Sales"]
        - region_analysis["Sales_Target"]
    )

    region_analysis["Achievement_%"] = (
        region_analysis["Sales"]
        / region_analysis["Sales_Target"]
    ) * 100

    print(region_analysis)

    region_analysis.to_csv(
        "region_target_analysis.csv",
        index=False
    )

    print("\n✅ Region analysis saved successfully!")

else:

    print(
        "⚠️ Region column is not available in both tables."
    )


# -------------------------------
# 5. TEAM-WISE ANALYSIS
# -------------------------------

print("\n========== TEAM-WISE TARGET ANALYSIS ==========")

if "Team" in fact_orders.columns and "Team" in fact_target.columns:

    team_actual_sales = (
        fact_orders
        .groupby("Team", as_index=False)["Sales"]
        .sum()
    )

    team_target_sales = (
        fact_target
        .groupby("Team", as_index=False)["Sales_Target"]
        .sum()
    )

    team_analysis = pd.merge(
        team_actual_sales,
        team_target_sales,
        on="Team",
        how="outer"
    )

    team_analysis["Sales"] = (
        team_analysis["Sales"].fillna(0)
    )

    team_analysis["Sales_Target"] = (
        team_analysis["Sales_Target"].fillna(0)
    )

    team_analysis["Sales_Variance"] = (
        team_analysis["Sales"]
        - team_analysis["Sales_Target"]
    )

    team_analysis["Achievement_%"] = (
        team_analysis["Sales"]
        / team_analysis["Sales_Target"]
    ) * 100

    print(team_analysis)

    team_analysis.to_csv(
        "team_target_analysis.csv",
        index=False
    )

    print("\n✅ Team analysis saved successfully!")

else:

    print(
        "⚠️ Team column is not available in both tables."
    )


# -------------------------------
# 6. MONTH-WISE ANALYSIS
# -------------------------------

print("\n========== MONTH-WISE TARGET ANALYSIS ==========")

if "Month" in fact_orders.columns and "Month" in fact_target.columns:

    monthly_actual_sales = (
        fact_orders
        .groupby("Month", as_index=False)["Sales"]
        .sum()
    )

    monthly_target_sales = (
        fact_target
        .groupby("Month", as_index=False)["Sales_Target"]
        .sum()
    )

    monthly_analysis = pd.merge(
        monthly_actual_sales,
        monthly_target_sales,
        on="Month",
        how="outer"
    )

    monthly_analysis["Sales"] = (
        monthly_analysis["Sales"].fillna(0)
    )

    monthly_analysis["Sales_Target"] = (
        monthly_analysis["Sales_Target"].fillna(0)
    )

    monthly_analysis["Sales_Variance"] = (
        monthly_analysis["Sales"]
        - monthly_analysis["Sales_Target"]
    )

    monthly_analysis["Achievement_%"] = (
        monthly_analysis["Sales"]
        / monthly_analysis["Sales_Target"]
    ) * 100

    print(monthly_analysis)

    monthly_analysis.to_csv(
        "monthly_target_analysis.csv",
        index=False
    )

    print("\n✅ Monthly analysis saved successfully!")

else:

    print(
        "⚠️ Month column is not available in both tables."
    )


# -------------------------------
# FINAL MESSAGE
# -------------------------------

print("\n==========================================")
print("TARGET VS ACTUAL ANALYSIS COMPLETED!")
print("==========================================")

print("\n✅ Overall Target vs Actual calculated!")

print("\n🎉 TARGET ANALYSIS PROCESS COMPLETED SUCCESSFULLY!")