# Databricks notebook source
# MAGIC %fs ls /databricks-datasets/structured-streaming/events/

# COMMAND ----------

# MAGIC %fs head /databricks-datasets/structured-streaming/events/file-13.json

# COMMAND ----------

# DBTITLE 1,Loading databricks JSON file
# MAGIC %python
# MAGIC df = spark.read.json("/databricks-datasets/structured-streaming/events/file-0.json")
# MAGIC df.printSchema()
# MAGIC df.show()

# COMMAND ----------

# MAGIC %python
# MAGIC df2 = spark.read.json("/databricks-datasets/structured-streaming/events/*.json")
# MAGIC df2.show()

# COMMAND ----------

# MAGIC %python
# MAGIC df2.write.json("/FileStore/tables/json/events.json")

# COMMAND ----------

# MAGIC %python
# MAGIC spark.sql("CREATE OR REPLACE TEMPORARY VIEW event_view USING json OPTIONS" +
# MAGIC          " (path '/FileStore/tables/json/events.json')")
# MAGIC spark.sql("SELECT * FROM event_view").show()

# COMMAND ----------


