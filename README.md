# Global-Superstore-Analysis
Global Superstore Sales & Performance Analysis
📌 Project Overview

This project focuses on analyzing a global retail dataset to understand sales performance, profitability, customer behavior, and shipping efficiency.
The objective is to transform raw transactional data into meaningful business insights using data analysis and visualization techniques.

The analysis follows an end-to-end data analyst workflow:

Data loading

Data cleaning & transformation

Exploratory analysis

KPI creation

Interactive dashboard development

📊 Dataset Description

Source: Kaggle – Global Superstore Dataset

Records: ~51,000+ rows

Features: Orders, customers, regions, categories, shipping details, sales, profit, discounts

🛠 Tools & Technologies Used

Python (Pandas, NumPy) – Data cleaning and feature engineering

Excel – Cleaned data export and validation

Power BI – Interactive dashboards and business insights

GitHub – Project version control and sharing

🧹 Data Cleaning & Preparation (Python)

Performed the following steps using Python:

Removed duplicate records

Handled missing values

Converted date columns to datetime format

Created new features:

Order Year

Order Month

Shipping Days

Profit Margin

Dropped unnecessary columns

Exported cleaned data to Excel for visualization

📈 Dashboard Structure (Power BI)

The project contains 3 dashboard pages, each answering a specific business question.

📄 Page 1: Sales Performance Overview

Purpose: High-level business performance monitoring

KPIs

Total Sales

Total Profit

Number of Orders

Profit Margin %

Visuals

Sales & Profit trend by year

Sales by region

Sales by category

Sales by month

Sales by segment

Sales by shipping mode

Key Insights

Overall sales show a steady upward trend

Technology category contributes the highest revenue

Certain regions dominate total sales

📄 Page 2: Regional & Category Performance Analysis

Purpose: Identify profitable and loss-making areas

Visuals

Profit by region

Profit by category

Sales by region and category

Monthly sales vs profit trend

Profit by sub-category

Key Insights

Technology category generates the highest profit

Some sub-categories (like Tables & Bookcases) show consistent losses

High sales do not always mean high profit

📄 Page 3: Customer & Shipping Performance Analysis

Purpose: Understand customer value and delivery efficiency

KPIs

Total Orders

Total Customers

Average Shipping Days

Visuals

Top customers by sales

Orders by shipping mode

Average shipping days by ship mode

Orders trend by month

Region and category slicers for filtering

Key Insights

Standard Class shipping has the highest order volume

Faster shipping modes have lower order counts

Shipping time impacts customer experience and cost

📌 Business Insights Summary

Technology is the most profitable category across regions

Several sub-categories generate losses despite high sales

Sales show seasonal trends across months

Shipping mode selection impacts delivery time and operational efficiency

Regional performance varies significantly in profitability

📁 Project Structure
Global-Superstore-Analysis/
│
├── data/
│   ├── Global_Superstore_raw.csv
│   └── cleaned_superstore_data.xlsx
│
├── notebooks/
│   └── data_cleaning_analysis.ipynb
│
├── powerbi/
│   └── Global_Superstore_Dashboard.pbix
│
├── images/
│   ├── page1_sales_overview.png
│   ├── page2_regional_analysis.png
│   └── page3_customer_shipping.png
│
└── README.md

🎯 Project Outcome

This project demonstrates:

Strong understanding of data cleaning & transformation

Ability to design business-focused dashboards

Skill in converting data into actionable insights

End-to-end data analyst project execution

🚀 How to Use This Project

Download the repository

Open the .pbix file in Power BI Desktop

Explore interactive dashboards using slicers

Review Python notebook for data preparation steps

📌 Author

Vishnuvardhan Reddy
Aspiring Data Analyst | Python | Power BI | SQL | Excel
