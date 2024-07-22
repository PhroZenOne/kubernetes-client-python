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

from kubernetes.client.models.v1_runtime_class_list import V1RuntimeClassList

class TestV1RuntimeClassList(unittest.TestCase):
    """V1RuntimeClassList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1RuntimeClassList:
        """Test V1RuntimeClassList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1RuntimeClassList`
        """
        model = V1RuntimeClassList()
        if include_optional:
            return V1RuntimeClassList(
                api_version = '',
                items = [
                    kubernetes.client.models.v1/runtime_class.v1.RuntimeClass(
                        api_version = '', 
                        handler = '', 
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
                        overhead = kubernetes.client.models.v1/overhead.v1.Overhead(
                            pod_fixed = {
                                'key' : ''
                                }, ), 
                        scheduling = kubernetes.client.models.v1/scheduling.v1.Scheduling(
                            node_selector = {
                                'key' : ''
                                }, 
                            tolerations = [
                                kubernetes.client.models.v1/toleration.v1.Toleration(
                                    effect = '', 
                                    key = '', 
                                    operator = '', 
                                    toleration_seconds = 56, 
                                    value = '', )
                                ], ), )
                    ],
                kind = '',
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1RuntimeClassList(
                items = [
                    kubernetes.client.models.v1/runtime_class.v1.RuntimeClass(
                        api_version = '', 
                        handler = '', 
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
                        overhead = kubernetes.client.models.v1/overhead.v1.Overhead(
                            pod_fixed = {
                                'key' : ''
                                }, ), 
                        scheduling = kubernetes.client.models.v1/scheduling.v1.Scheduling(
                            node_selector = {
                                'key' : ''
                                }, 
                            tolerations = [
                                kubernetes.client.models.v1/toleration.v1.Toleration(
                                    effect = '', 
                                    key = '', 
                                    operator = '', 
                                    toleration_seconds = 56, 
                                    value = '', )
                                ], ), )
                    ],
        )
        """

    def testV1RuntimeClassList(self):
        """Test V1RuntimeClassList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()