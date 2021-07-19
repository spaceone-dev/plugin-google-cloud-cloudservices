from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, \
    EnumDyField, ListDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_load_balancing = CloudServiceTypeResource()
cst_load_balancing.name = 'LoadBalancing'
cst_load_balancing.provider = 'google_cloud'
cst_load_balancing.group = 'NetworkService'
cst_load_balancing.service_code = 'netservice'
cst_load_balancing.is_primary = True
cst_load_balancing.is_major = True
cst_load_balancing.labels = ['Networking']
cst_load_balancing.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Load_Balancing.svg',
}

cst_load_balancing._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        EnumDyField.data_source('Protocol', 'data.lead_protocol', default_badge={
            'primary': ['HTTP', 'HTTPS', 'HTTP(S)'], 'indigo.500': ['TCP', 'TCP (Proxy)'],
            'coral.600': ['UDP', 'UDP (Proxy)']
        }),
        TextDyField.data_source('Region', 'data.region'),
        TextDyField.data_source('Frontends', 'data.frontend_display'),
        TextDyField.data_source('Backends', 'data.backends_display'),
        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],

    search=[
        SearchField.set(name='ID', key='data.id'),
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Protocol', key='data.lead_protocol'),
        SearchField.set(name='Region', key='data.region'),
        SearchField.set(name='description', key='data.description'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_load_balancing}),
]
