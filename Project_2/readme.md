# Exploratory Data Analysis (EDA)

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on an e-commerce order dataset.

The objective is to understand patterns, trends, distributions, outliers, and relationships within the data and convert the findings into meaningful observations.

## Dataset

The dataset contains:

- 1,200 records
- 14 columns

Important columns analyzed include:

- Date
- Product
- Quantity
- UnitPrice
- ItemsInCart
- PaymentMethod
- OrderStatus
- TotalPrice

## Tools Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- VS Code

## Analysis Performed

### 1. Basic Statistics

Basic descriptive statistics were calculated for:

- Quantity
- UnitPrice
- ItemsInCart
- TotalPrice

| Metric | Quantity | UnitPrice | ItemsInCart | TotalPrice |
|---|---:|---:|---:|---:|
| Count | 1200 | 1200 | 1200 | 1200 |
| Mean | 2.95 | 356.41 | 5.49 | 1053.97 |
| Median | 3.00 | 364.21 | 5.00 | 823.62 |

### 2. Outlier Analysis

The IQR method was used to identify unusual TotalPrice values.

- Q1 = 410.52
- Q3 = 1578.475
- IQR = 1167.955
- Upper Bound = 3330.4075
- Number of Outliers = 8

The 8 identified outliers were high-value orders.

These records were retained because their TotalPrice values were valid based on the Quantity × UnitPrice calculation.

### 3. Yearly Trend

Orders by year:

| Year | Orders |
|---|---:|
| 2023 | 510 |
| 2024 | 459 |
| 2025 | 231 |

2023 recorded the highest number of orders.

The 2025 value should be interpreted carefully because the dataset may not represent a complete calendar year.

### 4. Monthly Trend

The highest number of orders occurred in:

- June: 147 orders

The lowest number of orders occurred in:

- September: 73 orders

Order activity was generally higher during the first half of the year and lower during several months in the second half.

### 5. Product Analysis

Orders by product:

| Product | Orders |
|---|---:|
| Printer | 181 |
| Tablet | 179 |
| Chair | 178 |
| Laptop | 173 |
| Desk | 170 |
| Monitor | 163 |
| Phone | 156 |

Printer was the most frequently ordered product, while Phone had the fewest orders.

### 6. Revenue by Product

| Product | Revenue |
|---|---:|
| Chair | 195620.11 |
| Printer | 195612.61 |
| Laptop | 192126.56 |
| Tablet | 186568.95 |
| Monitor | 175651.41 |
| Desk | 167459.93 |
| Phone | 151722.39 |

Chair generated the highest total revenue, while Phone generated the lowest.

An interesting observation is that Printer had the highest number of orders, but Chair generated slightly higher revenue.

### 7. Payment Method Analysis

| Payment Method | Orders |
|---|---:|
| Online | 258 |
| Cash | 246 |
| Credit Card | 234 |
| Debit Card | 232 |
| Gift Card | 230 |

Online payment was the most frequently used payment method.

The payment methods were relatively balanced in the dataset.

### 8. Order Status Analysis

| Order Status | Orders |
|---|---:|
| Cancelled | 250 |
| Returned | 247 |
| Pending | 237 |
| Shipped | 235 |
| Delivered | 231 |

Cancelled was the most common order status, while Delivered was the least common.

### 9. Correlation Analysis

The following numerical variables were analyzed:

- Quantity
- UnitPrice
- ItemsInCart
- TotalPrice

Important correlations:

| Relationship | Correlation |
|---|---:|
| UnitPrice - TotalPrice | 0.717 |
| Quantity - TotalPrice | 0.615 |
| Quantity - ItemsInCart | 0.650 |
| ItemsInCart - TotalPrice | 0.393 |
| Quantity - UnitPrice | 0.015 |
| UnitPrice - ItemsInCart | 0.001 |

The strongest relationship was between UnitPrice and TotalPrice, with a correlation of 0.717.

Quantity also showed a positive relationship with TotalPrice.

Correlation indicates association between variables and does not by itself prove causation.

## Key Findings

1. The average TotalPrice (1053.97) is higher than the median (823.62), indicating that some higher-value orders influence the average.
2. Eight high-value orders were identified using the IQR method.
3. June had the highest monthly order count with 147 orders.
4. Printer had the highest number of orders with 181.
5. Chair generated the highest total revenue at 195620.11.
6. Online payment was the most frequently used payment method.
7. UnitPrice had the strongest correlation with TotalPrice.
8. Quantity also had a strong positive relationship with TotalPrice.

## Visualizations

The following charts were created and saved in the `output` folder:

1. Total Price Distribution
2. Monthly Order Trend
3. Orders by Product
4. Revenue by Product
5. Orders by Payment Method
6. Orders by Order Status
7. Correlation Matrix

## Project Structure

```text
Data_Analytics_Project_2
│
├── cleaned_dataset.xlsx
├── eda_analysis.py
├── README.md
│
└── output
    ├── 01_total_price_distribution.png
    ├── 02_monthly_order_trend.png
    ├── 03_orders_by_product.png
    ├── 04_revenue_by_product.png
    ├── 05_orders_by_payment_method.png
    ├── 06_orders_by_status.png
    └── 07_correlation_matrix.png


    Conclusion

This EDA helped transform the cleaned e-commerce dataset into meaningful analytical insights.

The analysis covered descriptive statistics, trends, outliers, product performance, payment methods, order statuses, and correlations.

The findings provide a foundation for further data analysis and visualization.


### STEP 16

Press:

**Ctrl + S**

Then your Project 2 folder should contain:

```text
Data_Analytics_Project_2
│
├── cleaned_dataset.xlsx
├── eda_analysis.py
├── README.md
└── output
    ├── 7 charts...