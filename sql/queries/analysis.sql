SELECT COUNT(*) AS total_rows
FROM superstore;
SELECT *
FROM superstore
LIMIT 5;
SELECT ROUND(SUM(Sales),2) AS total_sales
FROM superstore;
SELECT ROUND(SUM(Profit),2) AS total_profit
FROM superstore;
SELECT Region,
       ROUND(SUM(Sales),2) AS regional_sales
FROM superstore
GROUP BY Region
ORDER BY regional_sales DESC;
SELECT Region,
       ROUND(SUM(Profit),2) AS regional_profit
FROM superstore
GROUP BY Region
ORDER BY regional_profit DESC;
SELECT Product_Name,
       ROUND(SUM(Sales),2) AS total_sales
FROM superstore
GROUP BY Product_Name
ORDER BY total_sales DESC
LIMIT 10;