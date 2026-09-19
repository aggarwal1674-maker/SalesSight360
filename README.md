# SalesSight 360 – Multi-Channel Revenue Analytics Platform

## 📌 Project Overview

SalesSight 360 is a multi-channel revenue analytics platform designed to provide businesses with a unified view of sales, customer, product, payment, marketing, and CRM data.

Businesses often store data across multiple systems such as CRM platforms, order management systems, payment systems, and marketing platforms. This makes it difficult for decision-makers to get a complete and timely view of business performance.

SalesSight 360 addresses this problem by integrating multiple datasets, cleaning and validating the data, creating an analytics data model, calculating key performance indicators (KPIs), and performing business-focused analytics.

The project helps business stakeholders understand sales performance, profitability, customer behavior, product performance, marketing efficiency, CRM pipeline performance, and target achievement.

---

## 🎯 Project Objectives

The main objectives of SalesSight 360 are:

* Integrate multiple business datasets into a unified analytics workflow.
* Clean and prepare raw datasets for analysis.
* Validate relationships between business entities.
* Create dimension and fact tables for analytics.
* Calculate important business KPIs.
* Analyze sales and profit trends over time.
* Identify high-performing and low-performing products.
* Identify top and low-performing customers.
* Analyze marketing campaign and channel performance.
* Analyze CRM pipeline and expected revenue.
* Compare actual sales with sales targets.
* Generate structured analytical output files for business reporting.

---

## 🏗️ Project Architecture

The project follows a structured data analytics pipeline:

Raw Data
↓
Data Cleaning & ETL
↓
Data Validation
↓
Analytics Data Model
↓
KPI Calculation
↓
Business Analytics
↓
Analysis Output Files
↓
Business Insights & Reporting

---

## 📂 Project Structure

```text
SalesSight360/
│
├── Cleaned data/
│   ├── etl.py
│   ├── data_modal.py
│   ├── kpi_analysis.py
│   ├── target_analysis.py
│   ├── sales_trend_analysis.py
│   ├── product_analysis.py
│   ├── customer_analysis.py
│   ├── marketing_analysis.py
│   └── crm_analysis.py
│
├── Data/
│   ├── Raw datasets
│   ├── Cleaned datasets
│   ├── Dimension tables
│   ├── Fact tables
│   └── Analysis output files
│
├── README.md
└── requirements.txt
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* CSV Data Processing
* Data Cleaning
* ETL (Extract, Transform, Load)
* Data Validation
* Data Modeling
* KPI Analysis
* Business Analytics

---

# 🔄 ETL Process

The ETL pipeline is implemented using Python and Pandas.

### 1. Extract

Raw business datasets are loaded into the Python environment.

The project uses data related to:

* Customers
* Orders
* Products
* Payments
* Marketing
* CRM
* Sales Targets

### 2. Transform

The datasets are cleaned and prepared for analysis.

The transformation process includes:

* Handling missing values
* Standardizing data
* Validating identifiers
* Preparing datasets for analytics
* Creating calculated KPI columns

### 3. Load

The cleaned datasets are saved as CSV files and used to create the analytics data model.

---

# 🧩 Data Model

The analytics data model consists of dimension and fact tables.

## Dimension Tables

### DIM_CUSTOMERS

Contains customer-related information used for customer-level analysis.

### DIM_PRODUCTS

Contains product-related information used for product performance analysis.

## Fact Tables

### FACT_ORDERS

Contains order-level sales and profitability information.

### FACT_PAYMENTS

Contains payment transaction information.

### FACT_CRM

Contains CRM leads, sales stages, deal values, probabilities, and expected revenue.

### FACT_MARKETING

Contains marketing campaign performance information.

### FACT_TARGET

Contains sales targets by month, region, and team.

---

# 📊 KPI Analysis

The project calculates important business KPIs including:

### Sales KPIs

* Total Sales
* Total Profit
* Total Orders
* Average Order Value

### Profitability KPIs

* Overall Profit Margin
* Total Net Sales

### Discount KPIs

* Total Discount Amount
* Net Sales After Discount

### Payment KPIs

* Total Payment Amount

### Marketing KPIs

* Total Leads
* Total Conversions
* Total Marketing Spend
* Conversion Rate
* Cost Per Lead
* Cost Per Conversion

### CRM KPIs

* Total Deal Value
* Total Expected Revenue
* Average Deal Value
* Average Deal Probability

---

# 📈 Sales Trend Analysis

Sales trend analysis is performed using order date information.

The analysis includes:

* Monthly Sales Analysis
* Monthly Profit Analysis
* Monthly Order Analysis
* Monthly Sales Growth
* Best Sales Month
* Best Profit Month

### Key Finding

The highest sales and profit were recorded in **June 2026**.

* Highest Sales: 593,330.60
* Highest Profit: 183,251.60

The analysis also identifies month-to-month changes in sales performance to help understand business growth and fluctuations.

---

# 📦 Product Performance Analysis

Product-level analysis is performed to identify:

* Top 10 Products by Sales
* Top 10 Products by Profit
* Top 10 Products by Quantity
* Lowest Performing Products
* Product Profitability
* Best Product by Sales
* Best Product by Profit

### Key Finding

**Product P002** was identified as the best-performing product based on both sales and profit.

* Total Sales: 370,603.10
* Total Profit: 148,495.10

This indicates that P002 is a strong contributor to overall business performance.

---

# 👥 Customer Performance Analysis

Customer analytics is performed to identify:

* Top 10 Customers by Sales
* Top 10 Customers by Profit
* Top 10 Customers by Order Count
* Lowest Performing Customers
* Best Customer by Sales
* Best Customer by Profit
* Most Frequent Customer

### Key Findings

**Customer C155** was identified as the best customer based on sales and profit.

* Total Sales: 130,470.20
* Total Profit: 41,665.20
* Total Orders: 12

**Customer C050** was identified as one of the most frequent customers with 12 orders.

Customer-level analysis helps businesses identify valuable customers and understand customer contribution to revenue and profitability.

---

# 📢 Marketing Performance Analysis

Marketing analytics evaluates campaign and channel performance.

The analysis includes:

* Overall Marketing KPIs
* Campaign Performance
* Conversion Rate
* Cost Per Lead
* Cost Per Conversion
* Top Campaigns by Conversions
* Best Campaigns by Conversion Rate
* Most Efficient Campaigns
* Highest Spending Campaigns
* Channel Performance

### Key Findings

**Campaign 3** generated the highest number of conversions.

* Total Conversions: 496
* Conversion Rate: 29.75%

**Campaign 2** achieved the highest conversion rate.

* Conversion Rate: 95.37%
* Total Leads: 389
* Total Conversions: 371

**Campaign 21** was identified as the most cost-efficient campaign.

* Cost Per Conversion: 37.93
* Total Spend: 17,108

At the channel level, **LinkedIn** generated the highest number of conversions.

* Total Conversions: 3,469
* Conversion Rate: 32.37%

The analysis also highlights that high marketing spending does not always guarantee strong conversion performance.

---

# 💼 CRM Performance Analysis

CRM analytics evaluates the sales pipeline and potential revenue.

The analysis includes:

* Total Deal Value
* Expected Revenue
* Average Deal Value
* Average Deal Probability
* Stage-wise Deal Analysis
* Stage-wise Expected Revenue
* Top Deals by Deal Value
* Top Deals by Expected Revenue
* CRM Pipeline Performance

### Key Findings

* Total Deals: 500
* Total Deal Value: 6,097,679
* Total Expected Revenue: 2,454,355
* Average Deal Value: 12,195.36
* Average Deal Probability: 40.77%

The **Lead** stage had the highest total deal value.

* Total Deal Value: 1,750,295

The **Closed Won** stage generated the highest expected revenue.

* Expected Revenue: 926,082

The highest-value individual deal was:

* Lead ID: 1422
* Deal Value: 24,994
* Expected Revenue: 12,497

---

# 🎯 Target vs Actual Analysis

The project compares actual sales performance against predefined sales targets.

The analysis calculates:

* Total Actual Sales
* Total Sales Target
* Sales Variance
* Target Achievement Percentage

### Key Finding

* Actual Sales: 7,991,578.75
* Sales Target: 35,610,644
* Sales Variance: -27,619,065.25
* Target Achievement: 22.44%

The analysis indicates that actual sales were below the overall target during the analyzed period.

This provides an important business insight for management to investigate performance gaps and improve future sales planning.

---

# 📁 Analysis Outputs

The project generates multiple analytical output files including:

* Sales Trend Analysis
* Product Performance Analysis
* Customer Performance Analysis
* Campaign Performance Analysis
* Channel Performance Analysis
* CRM Stage Analysis
* Top CRM Deals
* Top Customers
* Top Products
* Marketing Campaign Rankings

These output files can be used for further reporting and dashboard development.

---

# 💡 Key Business Insights

The major insights generated from the analysis are:

1. Sales performance varies significantly across different months.
2. June 2026 recorded the highest sales and profit during the analyzed period.
3. Product P002 was the strongest product based on sales and profit.
4. Customer C155 was the highest-value customer based on sales and profit.
5. LinkedIn generated the highest number of marketing conversions.
6. Campaign 21 showed the strongest cost efficiency.
7. Campaign 2 achieved the highest conversion rate but operated with a comparatively smaller lead volume.
8. The Lead CRM stage contains the highest total deal value.
9. Closed Won deals contribute the highest expected revenue.
10. Actual sales were significantly below the overall sales target, indicating a performance gap that requires business attention.

---

# ▶️ How to Run the Project

## Step 1: Install Python

Install Python 3.x on your system.

## Step 2: Install Dependencies

Open a terminal in the project directory and run:

```bash
pip install -r requirements.txt
```

## Step 3: Run the ETL Pipeline

Run the ETL script to clean and prepare the datasets.

```bash
python etl.py
```

## Step 4: Validate the Data Model

Run:

```bash
python data_modal.py
```

This validates important relationships between customers, orders, products, and payments.

## Step 5: Run KPI Analysis

```bash
python kpi_analysis.py
```

## Step 6: Run Business Analytics

Run the following scripts:

```bash
python target_analysis.py
python sales_trend_analysis.py
python product_analysis.py
python customer_analysis.py
python marketing_analysis.py
python crm_analysis.py
```

The scripts generate analytical results and save output CSV files.

---

# 🚀 Future Scope

The project can be further enhanced by:

* Developing an interactive Power BI dashboard.
* Adding automated data refresh pipelines.
* Implementing sales forecasting.
* Adding customer churn prediction.
* Building marketing ROI analysis.
* Adding advanced CRM funnel conversion analysis.
* Implementing real-time analytics.
* Integrating databases and cloud data sources.
* Adding machine learning-based revenue prediction.

---

# 👩‍💻 Project Summary

SalesSight 360 demonstrates how Python and Pandas can be used to build an end-to-end business analytics solution.

The project covers the complete analytics workflow from data cleaning and ETL to data validation, data modeling, KPI calculation, and business performance analysis.

The solution provides actionable insights into sales, profitability, customers, products, marketing campaigns, CRM pipeline performance, and sales target achievement.

The project establishes a strong foundation for future business intelligence and dashboard development.
