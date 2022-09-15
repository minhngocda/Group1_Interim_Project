SELECT CountryRegionCode, SalesYTD, SalesLastYear, Revenue
FROM Sales.SalesTerritory
JOIN 
	  (SELECT TerritoryID, SUM(LineTotal) AS Revenue
   FROM Sales.SalesOrderHeader
	  JOIN Sales.SalesOrderDetail 
  ON Sales.SalesOrderHeader.SalesOrderID = Sales.SalesOrderDetail.SalesOrderID
	  GROUP BY TerritoryID) AS TerritoryRevenue
ON Sales.SalesTerritory.TerritoryID = TerritoryRevenue.TerritoryID