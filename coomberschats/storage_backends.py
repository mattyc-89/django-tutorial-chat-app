from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from storages.backends.azure_storage import AzureStorage
from decouple import config


class AzureMediaStorage(AzureStorage):
    account_name = config("AZURE_ACCOUNT_NAME")
    container_name = config("AZURE_CONTAINER")

    def __init__(self, *args, **kwargs):
        account_url = f"https://{self.account_name}.blob.core.windows.net"
        credential = DefaultAzureCredential()

        # Managed Identity-authenticated client
        self.service_client = BlobServiceClient(account_url, credential=credential)
        self.container_client = self.service_client.get_container_client(
            self.container_name
        )

        # Ensure container exists and create if not
        try:
            self.container_client.create_container()
        except Exception:
            pass

        super().__init__(*args, **kwargs)

    # Ensure django-storages uses the authenticated clients
    def _get_service_client(self):
        return self.service_client

    def _get_container_client(self):
        return self.container_client
