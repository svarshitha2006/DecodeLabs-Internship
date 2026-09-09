import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("ecommerce.db")

print("=" * 60)
print("DecodeLabs - Project 3: SQL Data Analysis")
print("=" * 60)

# Query 1: Total number of orders
query = """
SELECT COUNT(*) AS Total_Orders
FROM orders;
"""
result = pd.read_sql_query(query, connection)
print("\n1. TOTAL ORDERS")
print(result.to_string(index=False))


# Query 2: Total revenue
query = """
SELECT SUM(TotalPrice) AS Total_Revenue
FROM orders;
"""
result = pd.read_sql_query(query, connection)
print("\n2. TOTAL REVENUE")
print(result.to_string(index=False))


# Query 3: Average order value
query = """
SELECT AVG(TotalPrice) AS Average_Order_Value
FROM orders;
"""
result = pd.read_sql_query(query, connection)
print("\n3. AVERAGE ORDER VALUE")
print(result.to_string(index=False))


# Query 4: High-value orders
query = """
SELECT OrderID, Product, Quantity, TotalPrice
FROM orders
WHERE TotalPrice > 3000
ORDER BY TotalPrice DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n4. HIGH-VALUE ORDERS (TotalPrice > 3000)")
print(result.to_string(index=False))


# Query 5: Orders by product
query = """
SELECT Product, COUNT(*) AS Order_Count
FROM orders
GROUP BY Product
ORDER BY Order_Count DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n5. ORDERS BY PRODUCT")
print(result.to_string(index=False))


# Query 6: Revenue by product
query = """
SELECT Product, SUM(TotalPrice) AS Total_Revenue
FROM orders
GROUP BY Product
ORDER BY Total_Revenue DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n6. REVENUE BY PRODUCT")
print(result.to_string(index=False))


# Query 7: Average unit price by product
query = """
SELECT Product, AVG(UnitPrice) AS Average_Unit_Price
FROM orders
GROUP BY Product
ORDER BY Average_Unit_Price DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n7. AVERAGE UNIT PRICE BY PRODUCT")
print(result.to_string(index=False))


# Query 8: Orders by payment method
query = """
SELECT PaymentMethod, COUNT(*) AS Order_Count
FROM orders
GROUP BY PaymentMethod
ORDER BY Order_Count DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n8. ORDERS BY PAYMENT METHOD")
print(result.to_string(index=False))


# Query 9: Orders by status
query = """
SELECT OrderStatus, COUNT(*) AS Order_Count
FROM orders
GROUP BY OrderStatus
ORDER BY Order_Count DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n9. ORDERS BY STATUS")
print(result.to_string(index=False))


# Query 10: Monthly order count
query = """
SELECT
    strftime('%Y-%m', Date) AS Order_Month,
    COUNT(*) AS Order_Count
FROM orders
GROUP BY Order_Month
ORDER BY Order_Month;
"""
result = pd.read_sql_query(query, connection)
print("\n10. MONTHLY ORDER COUNT")
print(result.to_string(index=False))


# Query 11: Monthly revenue
query = """
SELECT
    strftime('%Y-%m', Date) AS Order_Month,
    SUM(TotalPrice) AS Monthly_Revenue
FROM orders
GROUP BY Order_Month
ORDER BY Order_Month;
"""
result = pd.read_sql_query(query, connection)
print("\n11. MONTHLY REVENUE")
print(result.to_string(index=False))


# Query 12: Products with more than 170 orders
query = """
SELECT Product, COUNT(*) AS Order_Count
FROM orders
GROUP BY Product
HAVING COUNT(*) > 170
ORDER BY Order_Count DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n12. PRODUCTS WITH MORE THAN 170 ORDERS")
print(result.to_string(index=False))


# Query 13: Products with revenue above 180000
query = """
SELECT Product, SUM(TotalPrice) AS Total_Revenue
FROM orders
GROUP BY Product
HAVING SUM(TotalPrice) > 180000
ORDER BY Total_Revenue DESC;
"""
result = pd.read_sql_query(query, connection)
print("\n13. PRODUCTS WITH REVENUE ABOVE 180,000")
print(result.to_string(index=False))


# Query 14: Highest 10 orders
query = """
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;
"""
result = pd.read_sql_query(query, connection)
print("\n14. TOP 10 HIGHEST-VALUE ORDERS")
print(result.to_string(index=False))


# Query 15: Lowest 10 orders
query = """
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice ASC
LIMIT 10;
"""
result = pd.read_sql_query(query, connection)
print("\n15. TOP 10 LOWEST-VALUE ORDERS")
print(result.to_string(index=False))


# Close database connection
connection.close()

print("\n" + "=" * 60)
print("SQL ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)