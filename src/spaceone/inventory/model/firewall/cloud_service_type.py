from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, EnumDyField, ListDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_firewall = CloudServiceTypeResource()
cst_firewall.name = 'Firewall'
cst_firewall.provider = 'google_cloud'
cst_firewall.group = 'VPC'
cst_firewall.service_code = 'vpc'
cst_firewall.labels = ['Networking']
cst_firewall.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Firewall_Rule.svg',
}


cst_firewall._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        EnumDyField.data_source('Logs', 'data.display.logs', default_badge={
            'indigo.500': ['On'], 'coral.600': ['Off']
        }),
        TextDyField.data_source('Network', 'data.display.network_display'),
        TextDyField.data_source('Direction', 'data.display.direction_display'),
        TextDyField.data_source('Priority', 'data.priority'),
        EnumDyField.data_source('Action On Match', 'data.display.action', default_badge={
            'indigo.500': ['Allow'], 'coral.600': ['Deny']
        }),

        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],

    search=[
        SearchField.set(name='ID', key='data.id'),
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Priority', key='data.priority'),
        SearchField.set(name='Direction', key='data.display.direction_display'),
        SearchField.set(name='Action', key='data.display.action'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_firewall}),
]
