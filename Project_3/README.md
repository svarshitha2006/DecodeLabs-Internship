\# DecodeLabs Data Analytics - Project 3



\## SQL Data Analysis



This project is part of my Data Analytics Internship at DecodeLabs.



The objective of this project is to use SQL queries to extract useful insights from an e-commerce dataset through filtering, sorting, grouping, and aggregation.



\## Project Objective



The main objectives of this project are:



\- Write SELECT queries

\- Filter data using WHERE

\- Sort data using ORDER BY

\- Group data using GROUP BY

\- Perform aggregations using COUNT, SUM, and AVG

\- Use HAVING to filter grouped results

\- Extract meaningful business insights from the dataset



\## Dataset



The dataset contains e-commerce order information.



\- Records: 1,200

\- Columns: 14

\- Source: Cleaned dataset from Project 1



\### Main Columns



\- OrderID

\- Date

\- CustomerID

\- Product

\- Quantity

\- UnitPrice

\- ShippingAddress

\- PaymentMethod

\- OrderStatus

\- TrackingNumber

\- ItemsInCart

\- CouponCode

\- ReferralSource

\- TotalPrice



\## Tools Used



\- Python

\- Pandas

\- SQLite

\- SQL

\- VS Code

\- Excel



\## Database



The Excel dataset was converted into a SQLite database.



Database:



`ecommerce.db`



Table:



`orders`



A Python script was used to load the cleaned Excel dataset into the SQLite database.



\## SQL Operations Performed



\### SELECT



Used SELECT queries to retrieve all records and specific columns from the orders table.



\### WHERE



Used WHERE to filter records, including:



\- Orders with Quantity greater than or equal to 4

\- Orders with TotalPrice greater than 3000



\### ORDER BY



Used ORDER BY to sort orders by TotalPrice in ascending and descending order.



\### GROUP BY



Used GROUP BY to analyze:



\- Orders by product

\- Revenue by product

\- Payment methods

\- Order status

\- Monthly orders

\- Monthly revenue



\### Aggregations



Used the following SQL aggregate functions:



\- COUNT()

\- SUM()

\- AVG()



\### HAVING



Used HAVING to identify:



\- Products with more than 170 orders

\- Products with revenue above ₹180,000



\## Key Results



\### Overall Statistics



| Metric | Result |

|---|---:|

| Total Orders | 1,200 |

| Total Revenue | ₹1,264,761.96 |

| Average Order Value | ₹1,053.97 |



\### Orders by Product



| Product | Orders |

|---|---:|

| Printer | 181 |

| Tablet | 179 |

| Chair | 178 |

| Laptop | 173 |

| Desk | 170 |

| Monitor | 163 |

| Phone | 156 |



Printer had the highest number of orders with 181 orders.



\### Revenue by Product



| Product | Revenue |

|---|---:|

| Chair | ₹195,620.11 |

| Printer | ₹195,612.61 |

| Laptop | ₹192,126.56 |

| Tablet | ₹186,568.95 |

| Monitor | ₹175,651.41 |

| Desk | ₹167,459.93 |

| Phone | ₹151,722.39 |



Chair generated the highest total revenue, closely followed by Printer.



\### Payment Methods



| Payment Method | Orders |

|---|---:|

| Online | 258 |

| Cash | 246 |

| Credit Card | 234 |

| Debit Card | 232 |

| Gift Card | 230 |



Online was the most frequently used payment method.



\### Order Status



| Order Status | Orders |

|---|---:|

| Cancelled | 250 |

| Returned | 247 |

| Pending | 237 |

| Shipped | 235 |

| Delivered | 231 |



Cancelled was the most common order status in the dataset.



\## High-Value Orders



The analysis identified orders with TotalPrice greater than ₹3,000.



The highest-value order was:



\- Order ID: ORD200789

\- Product: Tablet

\- Quantity: 5

\- Unit Price: ₹691.28

\- Total Price: ₹3,456.40



\## Top 10 Highest-Value Orders



The top 10 highest-value orders were extracted using:



```sql

ORDER BY TotalPrice DESC

LIMIT 10;

All top 10 orders had a quantity of 5.



Lowest-Value Orders



The lowest-value orders were also identified using:



ORDER BY TotalPrice ASC

LIMIT 10;



The lowest order was:



Order ID: ORD201161

Product: Phone

Quantity: 1

Total Price: ₹11.39

Monthly Analysis



Monthly order counts and revenue were calculated using SQLite's strftime() function.



The dataset contains records from January 2023 through June 2025.



Highest Monthly Order Count



The highest monthly order count was recorded in:



June 2024: 53 orders

Highest Monthly Revenue



The highest monthly revenue was recorded in:



June 2024: ₹68,068.54



2025 contains data only through June, so it represents a partial year.



Key Observations

The dataset contains 1,200 e-commerce orders.

Total revenue is ₹1,264,761.96.

The average order value is approximately ₹1,053.97.

Printer has the highest order count.

Chair has the highest total revenue.

Online is the most frequently used payment method.

Cancelled is the most common order status.

June 2024 recorded the highest monthly order count.

June 2024 also recorded the highest monthly revenue.

SQL GROUP BY and aggregation functions helped identify product-level and business-level patterns.

SQL Queries



The file queries.sql contains SQL queries covering:



SELECT

WHERE

ORDER BY

GROUP BY

COUNT

SUM

AVG

HAVING

LIMIT

Project Structure

Data\_Analytics\_Project\_3/

│

├── cleaned\_dataset.xlsx

├── ecommerce.db

├── create\_database.py

├── sql\_analysis.py

├── queries.sql

└── README.md

Conclusion



This project helped strengthen my understanding of SQL data analysis and relational querying.



By using SELECT, WHERE, ORDER BY, GROUP BY, COUNT, SUM, AVG, and HAVING, I was able to extract meaningful insights from the e-commerce dataset.



The project also improved my practical understanding of how SQL can be used to transform raw data into useful business information.

