# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from kubernetes.client.models.v1_volume_attachment_list import V1VolumeAttachmentList

class TestV1VolumeAttachmentList(unittest.TestCase):
    """V1VolumeAttachmentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1VolumeAttachmentList:
        """Test V1VolumeAttachmentList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1VolumeAttachmentList`
        """
        model = V1VolumeAttachmentList()
        if include_optional:
            return V1VolumeAttachmentList(
                api_version = '',
                items = [
                    kubernetes.client.models.v1/volume_attachment.v1.VolumeAttachment(
                        api_version = '', 
                        kind = '', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : ''
                                }, 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                ''
                                ], 
                            generate_name = '', 
                            generation = 56, 
                            labels = {
                                'key' : ''
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '', 
                                    fields_type = '', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '', 
                                    operation = '', 
                                    subresource = '', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '', 
                            namespace = '', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '', 
                                    name = '', 
                                    uid = '', )
                                ], 
                            resource_version = '', 
                            self_link = '', 
                            uid = '', ), 
                        spec = kubernetes.client.models.v1/volume_attachment_spec.v1.VolumeAttachmentSpec(
                            attacher = '', 
                            node_name = '', 
                            source = kubernetes.client.models.v1/volume_attachment_source.v1.VolumeAttachmentSource(
                                inline_volume_spec = kubernetes.client.models.v1/persistent_volume_spec.v1.PersistentVolumeSpec(
                                    access_modes = [
                                        ''
                                        ], 
                                    aws_elastic_block_store = kubernetes.client.models.v1/aws_elastic_block_store_volume_source.v1.AWSElasticBlockStoreVolumeSource(
                                        fs_type = '', 
                                        partition = 56, 
                                        read_only = True, 
                                        volume_id = '', ), 
                                    azure_disk = kubernetes.client.models.v1/azure_disk_volume_source.v1.AzureDiskVolumeSource(
                                        caching_mode = '', 
                                        disk_name = '', 
                                        disk_uri = '', 
                                        fs_type = '', 
                                        kind = '', 
                                        read_only = True, ), 
                                    azure_file = kubernetes.client.models.v1/azure_file_persistent_volume_source.v1.AzureFilePersistentVolumeSource(
                                        read_only = True, 
                                        secret_name = '', 
                                        secret_namespace = '', 
                                        share_name = '', ), 
                                    capacity = {
                                        'key' : ''
                                        }, 
                                    cephfs = kubernetes.client.models.v1/ceph_fs_persistent_volume_source.v1.CephFSPersistentVolumeSource(
                                        monitors = [
                                            ''
                                            ], 
                                        path = '', 
                                        read_only = True, 
                                        secret_file = '', 
                                        secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                                            name = '', 
                                            namespace = '', ), 
                                        user = '', ), 
                                    cinder = kubernetes.client.models.v1/cinder_persistent_volume_source.v1.CinderPersistentVolumeSource(
                                        fs_type = '', 
                                        read_only = True, 
                                        volume_id = '', ), 
                                    claim_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                                        api_version = '', 
                                        field_path = '', 
                                        kind = '', 
                                        name = '', 
                                        namespace = '', 
                                        resource_version = '', 
                                        uid = '', ), 
                                    csi = kubernetes.client.models.v1/csi_persistent_volume_source.v1.CSIPersistentVolumeSource(
                                        controller_expand_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                                            name = '', 
                                            namespace = '', ), 
                                        controller_publish_secret_ref = , 
                                        driver = '', 
                                        fs_type = '', 
                                        node_expand_secret_ref = , 
                                        node_publish_secret_ref = , 
                                        node_stage_secret_ref = , 
                                        read_only = True, 
                                        volume_attributes = {
                                            'key' : ''
                                            }, 
                                        volume_handle = '', ), 
                                    fc = kubernetes.client.models.v1/fc_volume_source.v1.FCVolumeSource(
                                        fs_type = '', 
                                        lun = 56, 
                                        read_only = True, 
                                        target_wwns = [
                                            ''
                                            ], 
                                        wwids = [
                                            ''
                                            ], ), 
                                    flex_volume = kubernetes.client.models.v1/flex_persistent_volume_source.v1.FlexPersistentVolumeSource(
                                        driver = '', 
                                        fs_type = '', 
                                        options = {
                                            'key' : ''
                                            }, 
                                        read_only = True, ), 
                                    flocker = kubernetes.client.models.v1/flocker_volume_source.v1.FlockerVolumeSource(
                                        dataset_name = '', 
                                        dataset_uuid = '', ), 
                                    gce_persistent_disk = kubernetes.client.models.v1/gce_persistent_disk_volume_source.v1.GCEPersistentDiskVolumeSource(
                                        fs_type = '', 
                                        partition = 56, 
                                        pd_name = '', 
                                        read_only = True, ), 
                                    glusterfs = kubernetes.client.models.v1/glusterfs_persistent_volume_source.v1.GlusterfsPersistentVolumeSource(
                                        endpoints = '', 
                                        endpoints_namespace = '', 
                                        path = '', 
                                        read_only = True, ), 
                                    host_path = kubernetes.client.models.v1/host_path_volume_source.v1.HostPathVolumeSource(
                                        path = '', 
                                        type = '', ), 
                                    iscsi = kubernetes.client.models.v1/iscsi_persistent_volume_source.v1.ISCSIPersistentVolumeSource(
                                        chap_auth_discovery = True, 
                                        chap_auth_session = True, 
                                        fs_type = '', 
                                        initiator_name = '', 
                                        iqn = '', 
                                        iscsi_interface = '', 
                                        lun = 56, 
                                        portals = [
                                            ''
                                            ], 
                                        read_only = True, 
                                        target_portal = '', ), 
                                    local = kubernetes.client.models.v1/local_volume_source.v1.LocalVolumeSource(
                                        fs_type = '', 
                                        path = '', ), 
                                    mount_options = [
                                        ''
                                        ], 
                                    nfs = kubernetes.client.models.v1/nfs_volume_source.v1.NFSVolumeSource(
                                        path = '', 
                                        read_only = True, 
                                        server = '', ), 
                                    node_affinity = kubernetes.client.models.v1/volume_node_affinity.v1.VolumeNodeAffinity(
                                        required = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                                            node_selector_terms = [
                                                kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                                    match_expressions = [
                                                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                            key = '', 
                                                            operator = '', 
                                                            values = [
                                                                ''
                                                                ], )
                                                        ], 
                                                    match_fields = [
                                                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                            key = '', 
                                                            operator = '', )
                                                        ], )
                                                ], ), ), 
                                    persistent_volume_reclaim_policy = '', 
                                    photon_persistent_disk = kubernetes.client.models.v1/photon_persistent_disk_volume_source.v1.PhotonPersistentDiskVolumeSource(
                                        fs_type = '', 
                                        pd_id = '', ), 
                                    portworx_volume = kubernetes.client.models.v1/portworx_volume_source.v1.PortworxVolumeSource(
                                        fs_type = '', 
                                        read_only = True, 
                                        volume_id = '', ), 
                                    quobyte = kubernetes.client.models.v1/quobyte_volume_source.v1.QuobyteVolumeSource(
                                        group = '', 
                                        read_only = True, 
                                        registry = '', 
                                        tenant = '', 
                                        user = '', 
                                        volume = '', ), 
                                    rbd = kubernetes.client.models.v1/rbd_persistent_volume_source.v1.RBDPersistentVolumeSource(
                                        fs_type = '', 
                                        image = '', 
                                        keyring = '', 
                                        monitors = [
                                            ''
                                            ], 
                                        pool = '', 
                                        read_only = True, 
                                        user = '', ), 
                                    scale_io = kubernetes.client.models.v1/scale_io_persistent_volume_source.v1.ScaleIOPersistentVolumeSource(
                                        fs_type = '', 
                                        gateway = '', 
                                        protection_domain = '', 
                                        read_only = True, 
                                        secret_ref = , 
                                        ssl_enabled = True, 
                                        storage_mode = '', 
                                        storage_pool = '', 
                                        system = '', 
                                        volume_name = '', ), 
                                    storage_class_name = '', 
                                    storageos = kubernetes.client.models.v1/storage_os_persistent_volume_source.v1.StorageOSPersistentVolumeSource(
                                        fs_type = '', 
                                        read_only = True, 
                                        volume_name = '', 
                                        volume_namespace = '', ), 
                                    volume_attributes_class_name = '', 
                                    volume_mode = '', 
                                    vsphere_volume = kubernetes.client.models.v1/vsphere_virtual_disk_volume_source.v1.VsphereVirtualDiskVolumeSource(
                                        fs_type = '', 
                                        storage_policy_id = '', 
                                        storage_policy_name = '', 
                                        volume_path = '', ), ), 
                                persistent_volume_name = '', ), ), 
                        status = kubernetes.client.models.v1/volume_attachment_status.v1.VolumeAttachmentStatus(
                            attach_error = kubernetes.client.models.v1/volume_error.v1.VolumeError(
                                message = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            attached = True, 
                            attachment_metadata = {
                                'key' : ''
                                }, 
                            detach_error = kubernetes.client.models.v1/volume_error.v1.VolumeError(
                                message = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), )
                    ],
                kind = '',
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1VolumeAttachmentList(
                items = [
                    kubernetes.client.models.v1/volume_attachment.v1.VolumeAttachment(
                        api_version = '', 
                        kind = '', 
                        metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                            annotations = {
                                'key' : ''
                                }, 
                            creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            deletion_grace_period_seconds = 56, 
                            deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            finalizers = [
                                ''
                                ], 
                            generate_name = '', 
                            generation = 56, 
                            labels = {
                                'key' : ''
                                }, 
                            managed_fields = [
                                kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                                    api_version = '', 
                                    fields_type = '', 
                                    fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                                    manager = '', 
                                    operation = '', 
                                    subresource = '', 
                                    time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                                ], 
                            name = '', 
                            namespace = '', 
                            owner_references = [
                                kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                                    api_version = '', 
                                    block_owner_deletion = True, 
                                    controller = True, 
                                    kind = '', 
                                    name = '', 
                                    uid = '', )
                                ], 
                            resource_version = '', 
                            self_link = '', 
                            uid = '', ), 
                        spec = kubernetes.client.models.v1/volume_attachment_spec.v1.VolumeAttachmentSpec(
                            attacher = '', 
                            node_name = '', 
                            source = kubernetes.client.models.v1/volume_attachment_source.v1.VolumeAttachmentSource(
                                inline_volume_spec = kubernetes.client.models.v1/persistent_volume_spec.v1.PersistentVolumeSpec(
                                    access_modes = [
                                        ''
                                        ], 
                                    aws_elastic_block_store = kubernetes.client.models.v1/aws_elastic_block_store_volume_source.v1.AWSElasticBlockStoreVolumeSource(
                                        fs_type = '', 
                                        partition = 56, 
                                        read_only = True, 
                                        volume_id = '', ), 
                                    azure_disk = kubernetes.client.models.v1/azure_disk_volume_source.v1.AzureDiskVolumeSource(
                                        caching_mode = '', 
                                        disk_name = '', 
                                        disk_uri = '', 
                                        fs_type = '', 
                                        kind = '', 
                                        read_only = True, ), 
                                    azure_file = kubernetes.client.models.v1/azure_file_persistent_volume_source.v1.AzureFilePersistentVolumeSource(
                                        read_only = True, 
                                        secret_name = '', 
                                        secret_namespace = '', 
                                        share_name = '', ), 
                                    capacity = {
                                        'key' : ''
                                        }, 
                                    cephfs = kubernetes.client.models.v1/ceph_fs_persistent_volume_source.v1.CephFSPersistentVolumeSource(
                                        monitors = [
                                            ''
                                            ], 
                                        path = '', 
                                        read_only = True, 
                                        secret_file = '', 
                                        secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                                            name = '', 
                                            namespace = '', ), 
                                        user = '', ), 
                                    cinder = kubernetes.client.models.v1/cinder_persistent_volume_source.v1.CinderPersistentVolumeSource(
                                        fs_type = '', 
                                        read_only = True, 
                                        volume_id = '', ), 
                                    claim_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                                        api_version = '', 
                                        field_path = '', 
                                        kind = '', 
                                        name = '', 
                                        namespace = '', 
                                        resource_version = '', 
                                        uid = '', ), 
                                    csi = kubernetes.client.models.v1/csi_persistent_volume_source.v1.CSIPersistentVolumeSource(
                                        controller_expand_secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                                            name = '', 
                                            namespace = '', ), 
                                        controller_publish_secret_ref = , 
                                        driver = '', 
                                        fs_type = '', 
                                        node_expand_secret_ref = , 
                                        node_publish_secret_ref = , 
                                        node_stage_secret_ref = , 
                                        read_only = True, 
                                        volume_attributes = {
                                            'key' : ''
                                            }, 
                                        volume_handle = '', ), 
                                    fc = kubernetes.client.models.v1/fc_volume_source.v1.FCVolumeSource(
                                        fs_type = '', 
                                        lun = 56, 
                                        read_only = True, 
                                        target_wwns = [
                                            ''
                                            ], 
                                        wwids = [
                                            ''
                                            ], ), 
                                    flex_volume = kubernetes.client.models.v1/flex_persistent_volume_source.v1.FlexPersistentVolumeSource(
                                        driver = '', 
                                        fs_type = '', 
                                        options = {
                                            'key' : ''
                                            }, 
                                        read_only = True, ), 
                                    flocker = kubernetes.client.models.v1/flocker_volume_source.v1.FlockerVolumeSource(
                                        dataset_name = '', 
                                        dataset_uuid = '', ), 
                                    gce_persistent_disk = kubernetes.client.models.v1/gce_persistent_disk_volume_source.v1.GCEPersistentDiskVolumeSource(
                                        fs_type = '', 
                                        partition = 56, 
                                        pd_name = '', 
                                        read_only = True, ), 
                                    glusterfs = kubernetes.client.models.v1/glusterfs_persistent_volume_source.v1.GlusterfsPersistentVolumeSource(
                                        endpoints = '', 
                                        endpoints_namespace = '', 
                                        path = '', 
                                        read_only = True, ), 
                                    host_path = kubernetes.client.models.v1/host_path_volume_source.v1.HostPathVolumeSource(
                                        path = '', 
                                        type = '', ), 
                                    iscsi = kubernetes.client.models.v1/iscsi_persistent_volume_source.v1.ISCSIPersistentVolumeSource(
                                        chap_auth_discovery = True, 
                                        chap_auth_session = True, 
                                        fs_type = '', 
                                        initiator_name = '', 
                                        iqn = '', 
                                        iscsi_interface = '', 
                                        lun = 56, 
                                        portals = [
                                            ''
                                            ], 
                                        read_only = True, 
                                        target_portal = '', ), 
                                    local = kubernetes.client.models.v1/local_volume_source.v1.LocalVolumeSource(
                                        fs_type = '', 
                                        path = '', ), 
                                    mount_options = [
                                        ''
                                        ], 
                                    nfs = kubernetes.client.models.v1/nfs_volume_source.v1.NFSVolumeSource(
                                        path = '', 
                                        read_only = True, 
                                        server = '', ), 
                                    node_affinity = kubernetes.client.models.v1/volume_node_affinity.v1.VolumeNodeAffinity(
                                        required = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
                                            node_selector_terms = [
                                                kubernetes.client.models.v1/node_selector_term.v1.NodeSelectorTerm(
                                                    match_expressions = [
                                                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                            key = '', 
                                                            operator = '', 
                                                            values = [
                                                                ''
                                                                ], )
                                                        ], 
                                                    match_fields = [
                                                        kubernetes.client.models.v1/node_selector_requirement.v1.NodeSelectorRequirement(
                                                            key = '', 
                                                            operator = '', )
                                                        ], )
                                                ], ), ), 
                                    persistent_volume_reclaim_policy = '', 
                                    photon_persistent_disk = kubernetes.client.models.v1/photon_persistent_disk_volume_source.v1.PhotonPersistentDiskVolumeSource(
                                        fs_type = '', 
                                        pd_id = '', ), 
                                    portworx_volume = kubernetes.client.models.v1/portworx_volume_source.v1.PortworxVolumeSource(
                                        fs_type = '', 
                                        read_only = True, 
                                        volume_id = '', ), 
                                    quobyte = kubernetes.client.models.v1/quobyte_volume_source.v1.QuobyteVolumeSource(
                                        group = '', 
                                        read_only = True, 
                                        registry = '', 
                                        tenant = '', 
                                        user = '', 
                                        volume = '', ), 
                                    rbd = kubernetes.client.models.v1/rbd_persistent_volume_source.v1.RBDPersistentVolumeSource(
                                        fs_type = '', 
                                        image = '', 
                                        keyring = '', 
                                        monitors = [
                                            ''
                                            ], 
                                        pool = '', 
                                        read_only = True, 
                                        user = '', ), 
                                    scale_io = kubernetes.client.models.v1/scale_io_persistent_volume_source.v1.ScaleIOPersistentVolumeSource(
                                        fs_type = '', 
                                        gateway = '', 
                                        protection_domain = '', 
                                        read_only = True, 
                                        secret_ref = , 
                                        ssl_enabled = True, 
                                        storage_mode = '', 
                                        storage_pool = '', 
                                        system = '', 
                                        volume_name = '', ), 
                                    storage_class_name = '', 
                                    storageos = kubernetes.client.models.v1/storage_os_persistent_volume_source.v1.StorageOSPersistentVolumeSource(
                                        fs_type = '', 
                                        read_only = True, 
                                        volume_name = '', 
                                        volume_namespace = '', ), 
                                    volume_attributes_class_name = '', 
                                    volume_mode = '', 
                                    vsphere_volume = kubernetes.client.models.v1/vsphere_virtual_disk_volume_source.v1.VsphereVirtualDiskVolumeSource(
                                        fs_type = '', 
                                        storage_policy_id = '', 
                                        storage_policy_name = '', 
                                        volume_path = '', ), ), 
                                persistent_volume_name = '', ), ), 
                        status = kubernetes.client.models.v1/volume_attachment_status.v1.VolumeAttachmentStatus(
                            attach_error = kubernetes.client.models.v1/volume_error.v1.VolumeError(
                                message = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                            attached = True, 
                            attachment_metadata = {
                                'key' : ''
                                }, 
                            detach_error = kubernetes.client.models.v1/volume_error.v1.VolumeError(
                                message = '', 
                                time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), ), )
                    ],
        )
        """

    def testV1VolumeAttachmentList(self):
        """Test V1VolumeAttachmentList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
