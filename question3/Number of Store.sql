  SELECT CountryRegionName, COUNT(*)AS NumberOfStore
  FROM Sales.vStoreWithAddresses
  GROUP BY CountryRegionName
  ORDER BY NumberOfStore DESC