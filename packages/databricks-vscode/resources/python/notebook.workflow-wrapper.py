#This file is autogenerated by the Databricks Extension for VS Code

dbutils.widgets.text("DATABRICKS_SOURCE_FILE", "")
dbutils.widgets.text("DATABRICKS_PROJECT_ROOT", "")

if dbutils.widgets.get("DATABRICKS_SOURCE_FILE") != "":
	import os
	os.chdir(os.path.dirname(dbutils.widgets.get("DATABRICKS_SOURCE_FILE")))

if dbutils.widgets.get("DATABRICKS_PROJECT_ROOT") != "":
	import sys
	sys.path.insert(0, dbutils.widgets.get("DATABRICKS_PROJECT_ROOT"))
