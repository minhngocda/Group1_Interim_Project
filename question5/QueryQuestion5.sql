

SELECT YearOpened, (2022 - YearOpened) as OperationDuration 
FROM Sales.vStoreWithDemographics;

SELECT YearOpened, (DATEPART(year, GETDATE()) - YearOpened) as OperationDuration,
		AnnualRevenue,
		BusinessEntityID
FROM Sales.vStoreWithDemographics;

