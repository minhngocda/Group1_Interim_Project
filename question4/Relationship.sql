SELECT pp.PersonType, hre.JobTitle, hre.SickLeaveHours
FROM HumanResources.Employee AS hre
INNER JOIN Person.Person AS pp ON pp.BusinessEntityID = hre.BusinessEntityID
ORDER BY hre.SickLeaveHours DESC