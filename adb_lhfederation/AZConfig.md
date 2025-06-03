## Setup on MS Fabric
- create workspace
- create lakehouse to reference inside Databricks UC (as foreign catalog)
- assign Entra ID security group an admin/member on workspace (SPN to be a member of this group)
- Fabric tenant setting to be enabled: "Service principals can use Fabric APIs" = enabled for security group 

## Setup on Azure
- create App Registration
- create security group and add service principal from app reg as member

### App registration configuration
1) In Aurthentication: SPA, redirect URI=https://[databricks-workspace-id].azuredatabricks.net/login/oauth/azure.html
2) Certificates & secrets: use client secret
3) API permissions: 

    - for MS Fabric REST APIs: choose appropiate Fabric Item under add permissions > Power BI > Delegated permissions > e.g. Lakehouse > Lakehouse.ReadAll
    - for Databricks Lakehouse federation: Add permission > APIs my organization uses > type "Azure SQL" > choose Azure SQL Database > Delegated permissions > user_impersonation

## Setup on Databricks
- Service Principal has CREATE CONNECTION and CREATE FOREIGN CATALOG on the connection

## Vendor References
Databricks REST API Reference, Create CONNECTION: https://docs.databricks.com/api/workspace/connections/create

Databricks Lakehouse Federation, SQL Server: https://learn.microsoft.com/en-us/azure/databricks/query-federation/sql-server

MS Entra ID SPN Authentication on Databricks: https://learn.microsoft.com/en-us/azure/databricks/dev-tools/auth/azure-sp

MS Fabric REST API, Scopes: https://learn.microsoft.com/en-us/rest/api/fabric/articles/scopes

MS Fabric REST API, Identity support: https://learn.microsoft.com/en-us/rest/api/fabric/articles/identity-support

