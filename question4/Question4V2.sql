SELECT hre.OrganizationLevel, pp.PersonType, AVG(hre.SickLeaveHours) AS AverageSickLeaveHours
FROM HumanResources.Employee AS hre
INNER JOIN Person.Person AS pp ON pp.BusinessEntityID = hre.BusinessEntityID
GROUP BY hre.OrganizationLevel, pp.PersonType
HAVING hre.OrganizationLevel IS NOT NULL
ORDER BY AVG(hre.SickLeaveHours) DESC;