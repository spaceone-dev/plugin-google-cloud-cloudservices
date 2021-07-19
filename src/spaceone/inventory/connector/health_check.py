import logging

from spaceone.inventory.libs.connector import GoogleCloudConnector
from spaceone.inventory.error import *

__all__ = ['HealthCheckConnector']
_LOGGER = logging.getLogger(__name__)


class HealthCheckConnector(GoogleCloudConnector):
    google_client_service = 'compute'
    version = 'v1'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def list_health_checks(self, **query):
        machine_image_list = []
        query.update({'project': self.project_id})
        request = self.client.machineImages().list(**query)
        while request is not None:
            try:
                response = request.execute()
                for image in response.get('items', []):
                    machine_image_list.append(image)
                request = self.client.machineImages().list_next(previous_request=request, previous_response=response)
            except Exception as e:
                request = None
                print(f'Error at machineImages().aggregatedList: {e}')

        return machine_image_list

