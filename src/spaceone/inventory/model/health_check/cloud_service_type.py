from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, EnumDyField, SizeField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_health_check = CloudServiceTypeResource()
cst_health_check.name = 'HealthCheck'
cst_health_check.provider = 'google_cloud'
cst_health_check.group = 'ComputeEngine'
cst_health_check.service_code = 'compute'
cst_health_check.labels = ['Networking', 'Compute']
cst_health_check.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Generic.svg',
}

cst_health_check._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        TextDyField.data_source('Location', 'data.location'),
        EnumDyField.data_source('Type', 'data.type', default_badge={
            'primary': ['TCP'],
            'indigo.500': ['SSL'],
            'coral.600': ['HTTP', 'HTTPS'],
            'green.500': ['HTTP2']
        }),
        DateTimeDyField.data_source('Creation Time', 'data.creation_time')
    ],

    search=[
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Creation Time', key='data.creation_time', data_type='datetime')
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_health_check}),
]
