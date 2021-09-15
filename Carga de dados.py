# Databricks notebook source
# DBTITLE 1,Read file in python
# MAGIC %python
# MAGIC clientes = spark.read.options(header="true", inferSchema="false", delimiter=";").csv("/FileStore/tables/carga/clientes_cartao.csv")
# MAGIC display(clientes)

# COMMAND ----------

# DBTITLE 1,Read file in scala
# MAGIC %scala
# MAGIC var clientes = spark.read.format("csv")
# MAGIC   .option("header", "true")
# MAGIC   .option("inferSchema", "false")
# MAGIC   .option("delimiter", ";")
# MAGIC   .load("/FileStore/tables/carga/clientes_cartao.csv")
# MAGIC 
# MAGIC display(clientes)

# COMMAND ----------

# DBTITLE 1,Read file in R
# MAGIC %r
# MAGIC #library(SparkR)
# MAGIC 
# MAGIC clientes <- read.df("/FileStore/tables/carga/clientes_cartao.csv", source="csv", header="true", inferSchema="false", delimiter=";")
# MAGIC 
# MAGIC display(clientes)

# COMMAND ----------

# MAGIC %r
# MAGIC printSchema(clientes)

# COMMAND ----------


