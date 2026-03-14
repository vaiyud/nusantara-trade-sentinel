from google.oauth2 import service_account
from google.adk.tools.bigquery import BigQueryToolset, BigQueryCredentialsConfig

def get_bq_tool():
    credentials_obj = service_account.Credentials.from_service_account_file("keys.json")
    bq_config = BigQueryCredentialsConfig(credentials=credentials_obj)
    return BigQueryToolset(credentials_config=bq_config)