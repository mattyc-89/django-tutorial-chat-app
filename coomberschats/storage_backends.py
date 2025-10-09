from storages.backends.azure_storage import AzureStorage
from azure.identity import DefaultAzureCredential
from decouple import config

class AzureMediaStorage(AzureStorage):
    account_name = config("AZURE_ACCOUNT_NAME")
    container_name = config("AZURE_CONTAINER")
    credential = DefaultAzureCredential()
