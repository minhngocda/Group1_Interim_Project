SELECT hre.OrganizationLevel, hre.JobTitle, pp.PersonType, AVG(hre.SickLeaveHours) AS AverageSickLeaveHours
FROM HumanResources.Employee AS hre
INNER JOIN Person.Person AS pp ON pp.BusinessEntityID = hre.BusinessEntityID
GROUP BY hre.OrganizationLevel, hre.JobTitle, pp.PersonType
ORDER BY AVG(hre.SickLeaveHours) DESC;