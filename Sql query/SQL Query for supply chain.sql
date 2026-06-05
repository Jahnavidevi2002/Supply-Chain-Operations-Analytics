CREATE DATABASE Supply_chain
 use Supply_chain


SELECT TOP 10 * 
 From [dbo].[supply_chain];


 SELECT COUNT(*) AS MissingValues
 From [dbo].[supply_chain]
WHERE InventorY_Turnover_Proxy IS NULL;


SELECT COUNT(*) AS TotalRows
FROM [dbo].[supply_chain ]


SELECT TOP 10
    SKU,
    Product_type,
    Stockout_Risk_Score,
    Risk_Category
    FROM [dbo].[supply_chain ]
ORDER BY Stockout_Risk_Score DESC;


SELECT
    SKU,
    Product_type,
    Stock_levels,
    Number_of_products_sold,
    Lead_times,
    Stockout_Risk_Score
 From [dbo].[supply_chain ]
WHERE SKU = 'SKU34';

SELECT TOP 10
    SKU,
    Product_type,
    Stock_levels,
    Number_of_products_sold,
      Excess_Inventory_Flag 
     FROM [dbo].[supply_chain ]
WHERE  Excess_Inventory_Flag  = 1
ORDER BY Stock_levels DESC;

SELECT
    AVG(Stock_levels) AS AvgStock,
    AVG(Number_of_products_sold) AS AvgSales
FROM [dbo].[supply_chain ]

