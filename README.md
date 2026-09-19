# SalesSight 360 – Multi-Channel Revenue Analytics Platform

## 📌 Project Overview

SalesSight 360 is a multi-channel revenue analytics platform developed to
integrate and analyze data from multiple business sources such as CRM,
orders, payments, marketing, customers, products, and sales targets.

The platform transforms raw business data into structured analytical
datasets and provides meaningful insights into revenue performance,
customer activity, sales pipeline, marketing performance, and target
achievement.

The project demonstrates an end-to-end data analytics workflow including
data ingestion, data cleaning, data transformation, data modeling,
KPI calculation, analysis, and business intelligence dashboarding.

---

## 🎯 Objectives

The main objectives of SalesSight 360 are:

- Integrate data from multiple business sources.
- Clean and preprocess raw datasets.
- Create structured analytical datasets.
- Analyze sales and revenue performance.
- Monitor customer and product activity.
- Analyze CRM leads and sales pipeline.
- Measure marketing campaign performance.
- Calculate important business KPIs.
- Compare actual performance with sales targets.
- Identify performance gaps and business trends.
- Present insights through an interactive Power BI dashboard.

---

## 🏢 Business Problem

Organizations often maintain sales, customer, payment, marketing, and CRM
information in separate datasets.

This makes it difficult to obtain a unified view of business performance.

SalesSight 360 addresses this problem by bringing these data sources
together into a structured analytical system that enables users to
understand:

- How much revenue is being generated
- Which products and regions contribute to sales
- How customers and orders are performing
- How leads move through the sales pipeline
- How marketing campaigns perform
- How actual sales compare with targets
- Where performance gaps exist

---

## 🔄 Project Workflow

The overall workflow of the project is:

Raw Data
   ↓
Data Ingestion
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Data Modeling
   ↓
KPI Calculation
   ↓
Data Analysis
   ↓
Power BI Dashboard
   ↓
Business Insights

---

## 📊 Data Sources

The project works with multiple business datasets:

### 1. Customers

Contains customer-related information used for customer and sales analysis.

### 2. Orders

Contains order-level information used to calculate sales, revenue,
profit, and order-related KPIs.

### 3. Products

Contains product information used for product-level performance analysis.

### 4. Payments

Contains payment information used for payment and revenue analysis.

### 5. CRM

Contains sales-lead and pipeline information used to analyze lead
conversion and expected revenue.

### 6. Marketing

Contains campaign-level marketing information used to evaluate marketing
spending and conversion performance.

### 7. Sales Targets

Contains target information used to compare actual performance against
planned targets.

---

## 🧹 Data Cleaning

The raw datasets were processed before analysis.

Major data preparation activities included:

- Handling missing values
- Checking duplicate records
- Validating identifiers
- Standardizing data types
- Cleaning categorical fields
- Checking invalid IDs
- Preparing date fields
- Creating consistent analytical datasets
- Removing or handling invalid records where required

---

## 🏗️ Data Model

The project uses a structured analytical data model.

### Dimension Tables

- DIM_CUSTOMERS
- DIM_PRODUCTS

### Fact Tables

- FACT_ORDERS
- FACT_PAYMENTS
- FACT_CRM
- FACT_MARKETING

The dimensional structure helps organize business data and supports
efficient analysis and reporting.

---

## 📐 Key Performance Indicators

The project calculates several important business KPIs.

### Sales KPIs

- Total Sales
- Total Profit
- Number of Orders
- Average Order Value
- Profit Margin
- Net Sales

### Marketing KPIs

- Marketing Spend
- Leads
- Conversions
- Conversion Rate
- Cost per Lead
- Cost per Conversion

### CRM KPIs

- CRM Deal Value
- Expected Revenue
- Sales Pipeline Performance

### Target KPIs

- Sales Target
- Actual Sales
- Target Achievement
- Target Performance Gap

---

## 📈 Project Results

Based on the processed project datasets, important calculated metrics
include:

| KPI | Value |
|---|---:|
| Total Sales | 7,991,578.75 |
| Total Profit | 2,615,311.75 |
| Total Orders | 1,000 |
| Average Order Value | 7,991.58 |
| Profit Margin | 32.73% |
| Net Sales | 7,452,024.71 |
| Leads | 32,223 |
| Conversions | 7,901 |
| Marketing Spend | 1,511,485 |
| Conversion Rate | 24.52% |
| Cost per Lead | 46.91 |
| Cost per Conversion | 191.30 |
| CRM Deal Value | 6,097,679 |
| Expected Revenue | 2,454,355 |
| Sales Target | 35,610,644 |
| Target Achievement | 22.44% |

---

## 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of business
performance.

The dashboard can be used to analyze:

### Revenue Analysis

- Total revenue
- Net sales
- Profit
- Profit margin
- Average order value

### Sales Analysis

- Order performance
- Product performance
- Regional performance
- Sales representative performance
- Channel-level performance

### CRM Analysis

- Lead volume
- Sales pipeline
- Deal value
- Expected revenue
- Conversion performance

### Marketing Analysis

- Campaign spending
- Leads generated
- Conversions
- Conversion rate
- Cost per lead
- Cost per conversion

### Target Analysis

- Actual sales versus target
- Target achievement
- Performance gaps
- Target-miss areas

---

## 🛠️ Technologies Used

- Python
- Pandas
- Power BI
- Microsoft Excel
- CSV
- Data Cleaning
- Data Transformation
- ETL
- Data Modeling
- Business Intelligence
- Data Analytics

---

## 📁 Project Structure

```text
SalesSight360/
│
├── Cleaned data/
│   ├── customers
│   ├── orders
│   ├── products
│   ├── payments
│   ├── marketing
│   ├── CRM
│   └── target
│
├── Data/
│
├── SalesSight360.pbix
│
├── README.md
│
└── Other project files

#Project Outcome

The project successfully demonstrates an end-to-end data analytics workflow, from data cleaning and transformation to KPI analysis and business intelligence dashboarding.

SalesSight 360 provides a unified view of sales, CRM, marketing, customer, product, payment, and target data. The analysis helps identify revenue performance, sales pipeline trends, marketing performance, and gaps between actual sales and targets.

The project demonstrates how multiple business datasets can be transformed into meaningful insights using Python, Pandas, data modeling, and Power BI.