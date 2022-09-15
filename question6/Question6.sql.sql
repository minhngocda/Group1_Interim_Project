SELECT 
	s.Name,
	s.BusinessEntityID, 
	SUM(o.TotalDue) as Revenue,   
	d.SquareFeet, 
	d.NumberEmployees
FROM Sales.SalesOrderHeader AS o
INNER JOIN Sales.Store AS s
	ON o.SalesPersonID = s.SalesPersonID
INNER JOIN Sales.vStoreWithDemographics AS d
	ON s.BusinessEntityID = d.BusinessEntityID
GROUP BY o.SalesPersonID, s.BusinessEntityID, s.Name, d.SquareFeet, d.NumberEmployees
ORDER BY Revenue;