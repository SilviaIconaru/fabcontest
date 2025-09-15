-- Fabric notebook source

-- METADATA ********************

-- META {
-- META   "kernel_info": {
-- META     "name": "synapse_pyspark"
-- META   },
-- META   "dependencies": {
-- META     "lakehouse": {
-- META       "default_lakehouse": "647c29e4-45fb-4ec6-b372-d383cb222e72",
-- META       "default_lakehouse_name": "Lakehouse_Silver",
-- META       "default_lakehouse_workspace_id": "22922658-b7be-477b-bc44-2ba43b0f9e7b",
-- META       "known_lakehouses": [
-- META         {
-- META           "id": "647c29e4-45fb-4ec6-b372-d383cb222e72"
-- META         }
-- META       ]
-- META     },
-- META     "environment": {}
-- META   }
-- META }

-- CELL ********************

select count(*) from dbo.t3

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

select countryOrRegion, count(1) from dbo.t3 group by countryOrRegion

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

select count(*) from dbo.t2

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }

-- CELL ********************

select count(*) from dbo.t1

-- METADATA ********************

-- META {
-- META   "language": "sparksql",
-- META   "language_group": "synapse_pyspark"
-- META }
