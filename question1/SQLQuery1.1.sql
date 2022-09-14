SELECT c.CountryRegionCode AS Country_code, a.CountryRegionName AS Country, SUM(d.AnnualRevenue) as Revenue, SUM(d.AnnualSales) AS Sales
FROM Sales.vStoreWithAddresses AS a
	INNER JOIN	Sales.vStoreWithDemographics AS d
	ON a.BusinessEntityID = d.BusinessEntityID
	INNER JOIN Person.CountryRegion AS c
	ON c.Name = a.CountryRegionName
GROUP BY a.CountryRegionName, c.CountryRegionCode
ORDER BY Revenue DESC, Sales DESC;