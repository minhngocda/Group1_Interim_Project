WITH sales_per_country AS (
SELECT TOP 1 c.CountryRegionCode AS Country_code, a.CountryRegionName AS Country, SUM(d.AnnualRevenue) as Revenue, SUM(d.AnnualSales) AS Sales
FROM Sales.vStoreWithAddresses AS a
	INNER JOIN	Sales.vStoreWithDemographics AS d
	ON a.BusinessEntityID = d.BusinessEntityID
	INNER JOIN Person.CountryRegion AS c
	ON c.Name = a.CountryRegionName
GROUP BY a.CountryRegionName, c.CountryRegionCode
ORDER BY Revenue DESC, Sales DESC)

SELECT t.Name as Region, 
		t.SalesYTD, 
		t.SalesLastYear, 
		s.Country
FROM Sales.SalesTerritory AS t
INNER JOIN sales_per_country AS s
	ON t.CountryRegionCode = s.Country_code;