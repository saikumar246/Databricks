# Databricks notebook source
# MAGIC %md
# MAGIC ##Init Scripts and Github integration
# MAGIC 
# MAGIC There 2 types of init scripts 1. ***Global Init Scripts***  2. ***Cluster-scoped init scripts***
# MAGIC 
# MAGIC Init Script event logs are available in cluster event logs.
# MAGIC If ***Cluster log delivery*** is configured for a cluster, log files will find in the below dbfs path

# COMMAND ----------

# MAGIC %fs ls dbfs:/cluster-logs/0306-112233-vs5567nq/init_scripts/0306-112233-vs5567nq_69_208_0_142/

# COMMAND ----------

# MAGIC %md
# MAGIC -When the cluster log delivery is not configured, logs are written to /databricks/init_scripts.
# MAGIC 
# MAGIC -You can use standard shell commands in a notebook to list and view the logs:

# COMMAND ----------

# MAGIC %sh
# MAGIC ls /databricks/init_scripts/
# MAGIC cat /databricks/init_scripts/20230309_142757_02_postgresql-install.sh.stdout.log

# COMMAND ----------

# MAGIC %md
# MAGIC **Cluster Scoped init Script**
# MAGIC 
# MAGIC -Provide the path of the init script below in the cluster configuration.
# MAGIC 
# MAGIC -See below to check the init file of 'postgresql-install.sh'

# COMMAND ----------

df = spark.read.text('/databricks/scripts/postgresql-install.sh')
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Global init script**
# MAGIC 
# MAGIC Add the init script in the admin console and enable it. And restart the cluster

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /../tmp/sai01/
# MAGIC pwd
# MAGIC touch sample.txt
# MAGIC ls -l

# COMMAND ----------

dbutils.fs.help()
