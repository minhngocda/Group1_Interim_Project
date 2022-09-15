SELECT TerritoryID, SUM(LineTotal) AS Revenue
FROM Sales.SalesOrderHeader
JOIN Sales.SalesOrderDetail 
ON Sales.SalesOrderHeader.SalesOrderID = Sales.SalesOrderDetail.SalesOrderID
GROUP BY TerritoryID