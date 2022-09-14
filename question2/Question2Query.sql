SELECT
Employee.BusinessEntityID, 
VacationHours, 
Rate, 
PayFrequency, 
RateChangeDate
FROM HumanResources.Employee 
INNER JOIN HumanResources.EmployeePayHistory 
ON EmployeePayHistory.BusinessEntityID = Employee.BusinessEntityID
ORDER BY HumanResources.Employee.VacationHours ASC;

