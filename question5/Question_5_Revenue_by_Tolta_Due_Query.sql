--Opetion Revenue by TotalDue
SELECT 
	st.Name,
	(2019 - de.YearOpened) AS Duration,
	SUM(soh.TotalDue) AS Revenue
FROM Sales.SalesOrderHeader AS soh
INNER JOIN Sales.Store AS st
	ON soh.SalesPersonID = st.SalesPersonID
INNER JOIN Sales.vStoreWithDemographics AS de
	ON st.BusinessEntityID = de.BusinessEntityID
WHERE soh.Status = 5
GROUP BY st.Name, de.YearOpened
ORDER BY Duration;