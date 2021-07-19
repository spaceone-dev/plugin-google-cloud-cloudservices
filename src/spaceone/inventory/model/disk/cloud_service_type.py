from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField, SizeField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta


cst_disk = CloudServiceTypeResource()
cst_disk.name = 'Disk'
cst_disk.provider = 'google_cloud'
cst_disk.group = 'ComputeEngine'
cst_disk.labels = ['Compute', 'Storage']
cst_disk.is_major = True
cst_disk.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Compute_Engine.svg',
    'spaceone:display_name': 'Disk'
}

cst_disk._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Name', 'data.name'),
        TextDyField.data_source('ID', 'data.id'),
        TextDyField.data_source('Zone', 'data.zone'),
        TextDyField.data_source('Source Image', 'data.source_image_display'),
        EnumDyField.data_source('Disk Type', 'data.disk_type',
                                default_outline_badge=['local-ssd', 'pd-balanced', 'pd-ssd', 'pd-standard']),
        SizeField.data_source('Size', 'data.size'),
        ListDyField.data_source('In Used By', 'data.in_used_by',
                                default_badge={'type': 'outline', 'delimiter': '<br>'}),
        ListDyField.data_source('Snapshot Schedule', 'data.snapshot_schedule_display',
                                default_badge={'type': 'outline', 'delimiter': '<br>'}),
        TextDyField.data_source('Source Image', 'data.source_image_display', options={'is_optional': True}),


        TextDyField.data_source('Read IOPS', 'data.read_iops', options={'is_optional': True}),
        TextDyField.data_source('Write IOPS', 'data.write_iops', options={'is_optional': True}),
        TextDyField.data_source('Read Throughput(MB/s)', 'data.read_throughput', options={'is_optional': True}),
        TextDyField.data_source('Write Throughput(MB/s)', 'data.write_throughput', options={'is_optional': True}),

        DateTimeDyField.data_source('Creation Time', 'data.creation_timestamp'),
    ],
    search=[
        SearchField.set(name='ID', key='data.id'),
        SearchField.set(name='Name', key='data.name'),
        SearchField.set(name='Status', key='data.status'),
        SearchField.set(name='Disk Type', key='data.disk_type'),
        SearchField.set(name='Size (Bytes)', key='data.size', data_type='integer'),
        SearchField.set(name='Project', key='data.project'),
        SearchField.set(name='Zone', key='data.zone'),
        SearchField.set(name='Region', key='region_code'),
        SearchField.set(name='Creation Time', key='data.creation_timestamp', data_type='datetime'),
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_disk}),
]
