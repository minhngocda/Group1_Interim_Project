-- Optio Revenue by Sales Person (Relation to Trading Store Duration vs Revenue)
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