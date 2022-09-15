SELECT DISTINCT hre.OrganizationLevel, hre.JobTitle, AVG(hre.SickLeaveHours) AS AverageSickLeaveHours, pp.PersonType
FROM HumanResources.Employee AS hre
INNER JOIN Person.Person AS pp ON pp.BusinessEntityID = hre.BusinessEntityID
GROUP BY hre.JobTitle, pp.PersonType, hre.OrganizationLevel
HAVING hre.OrganizationLevel IS NOT NULL
ORDER BY hre.OrganizationLevel
