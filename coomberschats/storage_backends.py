from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from storages.backends.azure_storage import AzureStorage
from decouple import config


class AzureMediaStorage(AzureStorage):
    account_name = config("AZURE_ACCOUNT_NAME")
    container_name = config("AZURE_CONTAINER")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        account_url = f"https://{self.account_name}.blob.core.windows.net"
        credential = DefaultAzureCredential()
        # build a client once and reuse it
        self._service_client = BlobServiceClient(account_url, credential=credential)
        self._container_client = self._service_client.get_container_client(
            self.container_name
        )

    # override the accessors so django-storages uses our MI-enabled client
    def _get_service_client(self):
        return self._service_client

    def _get_container_client(self):
        return self._container_client
