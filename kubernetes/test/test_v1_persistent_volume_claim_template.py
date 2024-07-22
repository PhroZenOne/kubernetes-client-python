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

from kubernetes.client.models.v1_persistent_volume_claim_template import V1PersistentVolumeClaimTemplate

class TestV1PersistentVolumeClaimTemplate(unittest.TestCase):
    """V1PersistentVolumeClaimTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PersistentVolumeClaimTemplate:
        """Test V1PersistentVolumeClaimTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PersistentVolumeClaimTemplate`
        """
        model = V1PersistentVolumeClaimTemplate()
        if include_optional:
            return V1PersistentVolumeClaimTemplate(
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
                spec = kubernetes.client.models.v1/persistent_volume_claim_spec.v1.PersistentVolumeClaimSpec(
                    access_modes = [
                        ''
                        ], 
                    data_source = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                        api_group = '', 
                        kind = '', 
                        name = '', ), 
                    data_source_ref = kubernetes.client.models.v1/typed_object_reference.v1.TypedObjectReference(
                        api_group = '', 
                        kind = '', 
                        name = '', 
                        namespace = '', ), 
                    resources = kubernetes.client.models.v1/volume_resource_requirements.v1.VolumeResourceRequirements(
                        limits = {
                            'key' : ''
                            }, 
                        requests = {
                            'key' : ''
                            }, ), 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '', 
                                operator = '', 
                                values = [
                                    ''
                                    ], )
                            ], 
                        match_labels = {
                            'key' : ''
                            }, ), 
                    storage_class_name = '', 
                    volume_attributes_class_name = '', 
                    volume_mode = '', 
                    volume_name = '', )
            )
        else:
            return V1PersistentVolumeClaimTemplate(
                spec = kubernetes.client.models.v1/persistent_volume_claim_spec.v1.PersistentVolumeClaimSpec(
                    access_modes = [
                        ''
                        ], 
                    data_source = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                        api_group = '', 
                        kind = '', 
                        name = '', ), 
                    data_source_ref = kubernetes.client.models.v1/typed_object_reference.v1.TypedObjectReference(
                        api_group = '', 
                        kind = '', 
                        name = '', 
                        namespace = '', ), 
                    resources = kubernetes.client.models.v1/volume_resource_requirements.v1.VolumeResourceRequirements(
                        limits = {
                            'key' : ''
                            }, 
                        requests = {
                            'key' : ''
                            }, ), 
                    selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                        match_expressions = [
                            kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                                key = '', 
                                operator = '', 
                                values = [
                                    ''
                                    ], )
                            ], 
                        match_labels = {
                            'key' : ''
                            }, ), 
                    storage_class_name = '', 
                    volume_attributes_class_name = '', 
                    volume_mode = '', 
                    volume_name = '', ),
        )
        """

    def testV1PersistentVolumeClaimTemplate(self):
        """Test V1PersistentVolumeClaimTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()