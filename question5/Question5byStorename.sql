/*SELECT 
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
*/


-- Option by Sales Person (Relation to Trading Store Duration vs Revenue)
SELECT
	Store.Name, 
	SUM(SalesPerson.SalesYTD) as Revenue,
	YearOpened,
	(2019 - YearOpened) as StoreDuration
FROM Sales.Store
INNER JOIN Sales.vStoreWithDemographics ON Store.BusinessEntityID = vStoreWithDemographics.BusinessEntityID
LEFT JOIN Sales.SalesPerson ON SalesPerson.BusinessEntityID = Store.SalesPersonID
GROUP BY 
	Store.Name, 
	vStoreWithDemographics.YearOpened
ORDER BY Revenue DESC;