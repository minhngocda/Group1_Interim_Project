SELECT VacationHours, 
        Bonus
FROM HumanResources.Employee
INNER JOIN Sales.SalesPerson
ON Sales.SalesPerson.BusinessEntityID = HumanResources.Employee.BusinessEntityID
ORDER BY Bonus DESC