-- Databricks notebook source
-- MAGIC %sql
-- MAGIC SELECT pais, sum(preco) AS total_vendido from vinhos
-- MAGIC WHERE preco > 0
-- MAGIC GROUP BY pais
-- MAGIC ORDER BY total_vendido DESC
-- MAGIC LIMIT 10

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC SELECT pais, variante, sum(preco) AS total_vendido from vinhos
-- MAGIC WHERE preco > 0
-- MAGIC GROUP BY pais, variante
-- MAGIC ORDER BY total_vendido DESC
-- MAGIC LIMIT 10

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC SELECT pontos, preco from vinhos

-- COMMAND ----------


