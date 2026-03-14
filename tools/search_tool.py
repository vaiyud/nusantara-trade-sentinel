import os
from google.adk.tools import VertexAiSearchTool

def get_search_tool():
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    ds_id = os.getenv("DATASTORE_ID")
    datastore_path = f"projects/{project_id}/locations/global/collections/default_collection/dataStores/{ds_id}"
    
    return VertexAiSearchTool(data_store_id=datastore_path)