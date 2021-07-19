from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, EnumDyField, SizeField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

cst_snapshot = CloudServiceTypeResource()
cst_snapshot.name = 'Snapshot'
cst_snapshot.provider = 'google_cloud'
cst_snapshot.group = 'ComputeEngine'
cst_snapshot.service_code = 'compute'
cst_snapshot.labels = ['Compute', 'Storage']
cst_snapshot.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Compute_Engine.svg',
}

cst_snapshot._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        EnumDyField.data_source('Status', 'data.status', default_state={
            'safe': ['READY'],
            'warning': ['CREATING', 'UPLOADING', 'DELETING'],
            'alert': ['FAILED'],
        }),

        ListDyField.data_source('Location', 'data.storage_locations'),
        SizeField.data_source('SnapShot Size', 'data.disk.storage_bytes'),
        TextDyField.data_source('Creation Type', 'data.creation_type'),
        TextDyField.data_source('Source Disk', 'data.disk.source_disk_display'),
        SizeField.data_source('Disk Size', 'data.disk.disk_size'),
        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp')
    ],
    # TODO: Give a set that fit to its filtered data...
    search=[
        SearchField.set(name='ID', key='data.id'),
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Location', key='data.storage_locations'),
        SearchField.set(name='Source Disk', key='data.disk.source_disk_display'),
        SearchField.set(name='Creation Type', key='data.creation_type'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_snapshot}),
]
