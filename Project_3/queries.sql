-- ============================================
-- DecodeLabs Data Analytics - Project 3
-- SQL Data Analysis
-- ============================================

-- Query 1: Display all orders
SELECT *
FROM orders;


-- Query 2: Select specific columns
SELECT OrderID, Date, Product, Quantity, TotalPrice
FROM orders;


-- Query 3: Filter orders by quantity
SELECT OrderID, Product, Quantity, TotalPrice
FROM orders
WHERE Quantity >= 4;


-- Query 4: Filter high-value orders
SELECT OrderID, Product, TotalPrice
FROM orders
WHERE TotalPrice > 3000;


-- Query 5: Sort orders by TotalPrice
SELECT OrderID, Product, Quantity, TotalPrice
FROM orders
ORDER BY TotalPrice DESC;


-- Query 6: Count total orders
SELECT COUNT(*) AS Total_Orders
FROM orders;


-- Query 7: Calculate total revenue
SELECT SUM(TotalPrice) AS Total_Revenue
FROM orders;


-- Query 8: Calculate average order value
SELECT AVG(TotalPrice) AS Average_Order_Value
FROM orders;


-- Query 9: Count orders by product
SELECT Product, COUNT(*) AS Order_Count
FROM orders
GROUP BY Product
ORDER BY Order_Count DESC;


-- Query 10: Calculate revenue by product
SELECT Product, SUM(TotalPrice) AS Total_Revenue
FROM orders
GROUP BY Product
ORDER BY Total_Revenue DESC;


-- Query 11: Average price by product
SELECT Product, AVG(UnitPrice) AS Average_Unit_Price
FROM orders
GROUP BY Product
ORDER BY Average_Unit_Price DESC;


-- Query 12: Count orders by payment method
SELECT PaymentMethod, COUNT(*) AS Order_Count
FROM orders
GROUP BY PaymentMethod
ORDER BY Order_Count DESC;


-- Query 13: Count orders by order status
SELECT OrderStatus, COUNT(*) AS Order_Count
FROM orders
GROUP BY OrderStatus
ORDER BY Order_Count DESC;


-- Query 14: Monthly order count
SELECT
    strftime('%Y-%m', Date) AS Order_Month,
    COUNT(*) AS Order_Count
FROM orders
GROUP BY Order_Month
ORDER BY Order_Month;


-- Query 15: Monthly revenue
SELECT
    strftime('%Y-%m', Date) AS Order_Month,
    SUM(TotalPrice) AS Monthly_Revenue
FROM orders
GROUP BY Order_Month
ORDER BY Order_Month;


-- Query 16: Average quantity by product
SELECT Product, AVG(Quantity) AS Average_Quantity
FROM orders
GROUP BY Product
ORDER BY Average_Quantity DESC;


-- Query 17: Products with more than 170 orders
SELECT Product, COUNT(*) AS Order_Count
FROM orders
GROUP BY Product
HAVING COUNT(*) > 170
ORDER BY Order_Count DESC;


-- Query 18: Products with revenue above 180,000
SELECT Product, SUM(TotalPrice) AS Total_Revenue
FROM orders
GROUP BY Product
HAVING SUM(TotalPrice) > 180000
ORDER BY Total_Revenue DESC;


-- Query 19: Highest 10 orders
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;


-- Query 20: Lowest 10 orders
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM orders
ORDER BY TotalPrice ASC
LIMIT 10;