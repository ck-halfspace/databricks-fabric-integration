## 1: Activate virtual environment ##
Activate virtual envirnment to make sure code is run with the configured Python version (running project isolated of a users global Python installation) - see: https://python-poetry.org/docs/managing-environments/

```powershell
poetry env activate  # Use 'pyenv local' for MacOS
```

Display the environment:
```powershell
poetry env info
```


## 2: Install databricks-connect ##
Install the Databricks Connect client with Poetry - see: https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-connect/python/install#install-the-databricks-connect-client-with-poetry

databricks-connect conflicts with pyspark. Check for pyspark installations and remove accordingly before installing databricks-connect.

```powershell
poetry add databricks-connect@~15.4  # Or X.Y to match your cluster version.
```

## 3: Install databricks-sdk for python ##

```powershell
poetry add databricks-sdk
```

## 4: Install dotenv plugin ##
```
poetry add poetry-dotenv-plugin
```