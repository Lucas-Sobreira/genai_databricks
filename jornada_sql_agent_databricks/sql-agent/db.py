import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

access_token = os.getenv("DATABRICKS_TOKEN")
server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
http_path = os.getenv("DATABRICKS_HTTP_PATH")
catalog = os.getenv("DATABRICKS_CATALOG", "erp_farma")
schema = os.getenv("DATABRICKS_SCHEMA", "gold")

engine = create_engine(
    url=f"databricks://token:{access_token}@{server_hostname}?"
    + f"http_path={http_path}&catalog={catalog}&schema={schema}"
)
