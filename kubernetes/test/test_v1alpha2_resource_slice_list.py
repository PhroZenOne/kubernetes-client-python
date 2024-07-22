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

from kubernetes.client.models.v1alpha2_resource_slice_list import V1alpha2ResourceSliceList

class TestV1alpha2ResourceSliceList(unittest.TestCase):
    """V1alpha2ResourceSliceList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2ResourceSliceList:
        """Test V1alpha2ResourceSliceList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2ResourceSliceList`
        """
        model = V1alpha2ResourceSliceList()
        if include_optional:
            return V1alpha2ResourceSliceList(
                api_version = '',
                items = [
                    kubernetes.client.models.v1alpha2/resource_slice.v1alpha2.ResourceSlice(
                        api_version = '', 
                        driver_name = '', 
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
                        named_resources = kubernetes.client.models.v1alpha2/named_resources_resources.v1alpha2.NamedResourcesResources(
                            instances = [
                                kubernetes.client.models.v1alpha2/named_resources_instance.v1alpha2.NamedResourcesInstance(
                                    attributes = [
                                        kubernetes.client.models.v1alpha2/named_resources_attribute.v1alpha2.NamedResourcesAttribute(
                                            bool = True, 
                                            int = 56, 
                                            int_slice = kubernetes.client.models.v1alpha2/named_resources_int_slice.v1alpha2.NamedResourcesIntSlice(
                                                ints = [
                                                    56
                                                    ], ), 
                                            name = '', 
                                            quantity = '', 
                                            string = '', 
                                            string_slice = kubernetes.client.models.v1alpha2/named_resources_string_slice.v1alpha2.NamedResourcesStringSlice(
                                                strings = [
                                                    ''
                                                    ], ), 
                                            version = '', )
                                        ], 
                                    name = '', )
                                ], ), 
                        node_name = '', )
                    ],
                kind = '',
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1alpha2ResourceSliceList(
                items = [
                    kubernetes.client.models.v1alpha2/resource_slice.v1alpha2.ResourceSlice(
                        api_version = '', 
                        driver_name = '', 
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
                        named_resources = kubernetes.client.models.v1alpha2/named_resources_resources.v1alpha2.NamedResourcesResources(
                            instances = [
                                kubernetes.client.models.v1alpha2/named_resources_instance.v1alpha2.NamedResourcesInstance(
                                    attributes = [
                                        kubernetes.client.models.v1alpha2/named_resources_attribute.v1alpha2.NamedResourcesAttribute(
                                            bool = True, 
                                            int = 56, 
                                            int_slice = kubernetes.client.models.v1alpha2/named_resources_int_slice.v1alpha2.NamedResourcesIntSlice(
                                                ints = [
                                                    56
                                                    ], ), 
                                            name = '', 
                                            quantity = '', 
                                            string = '', 
                                            string_slice = kubernetes.client.models.v1alpha2/named_resources_string_slice.v1alpha2.NamedResourcesStringSlice(
                                                strings = [
                                                    ''
                                                    ], ), 
                                            version = '', )
                                        ], 
                                    name = '', )
                                ], ), 
                        node_name = '', )
                    ],
        )
        """

    def testV1alpha2ResourceSliceList(self):
        """Test V1alpha2ResourceSliceList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
