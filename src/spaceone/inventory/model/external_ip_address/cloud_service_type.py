from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, EnumDyField, ListDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_external_ip = CloudServiceTypeResource()
cst_external_ip.name = 'ExternalIPAddress'
cst_external_ip.provider = 'google_cloud'
cst_external_ip.group = 'VPC'
cst_external_ip.service_code = 'vpc'
cst_external_ip.labels = ['Networking']
cst_external_ip.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/External_IP_Address.svg',
}


cst_external_ip._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        TextDyField.data_source('External Address', 'data.address'),
        TextDyField.data_source('Region', 'data.region'),
        EnumDyField.data_source('Type', 'data.is_ephemeral', default_badge={
            'indigo.500': ['Static'], 'coral.600': ['Ephemeral']
        }),
        EnumDyField.data_source('Version', 'data.ip_version_display', default_badge={
            'indigo.500': ['IPv4'], 'coral.600': ['IPv6']
        }),
        ListDyField.data_source('In Used By', 'data.used_by'),

        TextDyField.data_source('Network Tier', 'data.network_tier_display'),

        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],

    search=[
        SearchField.set(name='ID', key='data.id'),
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='IP Address', key='data.address'),
        SearchField.set(name='Version', key='data.ip_version_display'),
        SearchField.set(name='Network Tier', key='data.network_tier_display'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_external_ip}),
]
