from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, EnumDyField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_network = CloudServiceTypeResource()
cst_network.name = 'VPCNetwork'
cst_network.provider = 'google_cloud'
cst_network.group = 'VPC'
cst_network.service_code = 'vpc'
cst_network.is_primary = True
cst_network.labels = ['Networking']
cst_network.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/VPC.svg',
}

cst_network._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        TextDyField.data_source('Number of Subnet', 'data.subnetwork_data.total_number'),
        TextDyField.data_source('Maximum transmission unit', 'data.mtu'),
        TextDyField.data_source('Mode', 'data.subnet_creation_mode'),
        EnumDyField.data_source('Global Dynamic Routing', 'data.global_dynamic_route', default_state={
            'safe': ['On'],
            'warning': ['Off'],
        }),

        # is_optional - Default
        TextDyField.data_source('Description', 'data.description', options={
            'is_optional': True
        }),
        TextDyField.data_source('IPv4 Range', 'data.ipv4_range', options={
            'is_optional': True
        }),
        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],

    search=[
        SearchField.set(name='ID', key='data.id'),
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='description', key='data.description'),
        SearchField.set(name='firewall', key='data.firewall_data.firewall'),
        SearchField.set(name='route', key='data.route_data.route'),
        SearchField.set(name='subnetwork', key='data.subnetwork_data.subnets'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_network}),
]
