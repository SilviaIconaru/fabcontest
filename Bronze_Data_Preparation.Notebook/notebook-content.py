# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "23622aa8-57f7-4eb4-ac8f-594540f98df3",
# META       "default_lakehouse_name": "Lakehouse_Bronze",
# META       "default_lakehouse_workspace_id": "22922658-b7be-477b-bc44-2ba43b0f9e7b",
# META       "known_lakehouses": [
# META         {
# META           "id": "23622aa8-57f7-4eb4-ac8f-594540f98df3"
# META         }
# META       ]
# META     },
# META     "environment": {}
# META   }
# META }

# MARKDOWN ********************

# # Dev/Test/Prod data set simulation in a Bronze layer
# 
# Shortcuts will be created to different t3_* tables depending on stage.

# CELL ********************

t3_prod_df = spark.table("t3_prod")

t3_dev_df = t3_prod_df.sample(fraction=0.01, seed=42).write.format("delta").mode("overwrite").saveAsTable("dbo.t3_dev")

t3_test_df = t3_prod_df.sample(fraction=0.10, seed=123).write.format("delta").mode("overwrite").saveAsTable("dbo.t3_test")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print(spark.table("t3_prod").count(), spark.table("t3_test").count(), spark.table("t3_dev").count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
