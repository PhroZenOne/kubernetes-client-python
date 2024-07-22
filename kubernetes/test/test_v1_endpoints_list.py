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

from kubernetes.client.models.v1_endpoints_list import V1EndpointsList

class TestV1EndpointsList(unittest.TestCase):
    """V1EndpointsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EndpointsList:
        """Test V1EndpointsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EndpointsList`
        """
        model = V1EndpointsList()
        if include_optional:
            return V1EndpointsList(
                api_version = '',
                items = [
                    kubernetes.client.models.v1/endpoints.v1.Endpoints(
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
                        subsets = [
                            kubernetes.client.models.v1/endpoint_subset.v1.EndpointSubset(
                                addresses = [
                                    kubernetes.client.models.v1/endpoint_address.v1.EndpointAddress(
                                        hostname = '', 
                                        ip = '', 
                                        node_name = '', 
                                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                                            api_version = '', 
                                            field_path = '', 
                                            kind = '', 
                                            name = '', 
                                            namespace = '', 
                                            resource_version = '', 
                                            uid = '', ), )
                                    ], 
                                not_ready_addresses = [
                                    kubernetes.client.models.v1/endpoint_address.v1.EndpointAddress(
                                        hostname = '', 
                                        ip = '', 
                                        node_name = '', )
                                    ], 
                                ports = [
                                    kubernetes.client.models.core/v1/endpoint_port.core.v1.EndpointPort(
                                        app_protocol = '', 
                                        name = '', 
                                        port = 56, 
                                        protocol = '', )
                                    ], )
                            ], )
                    ],
                kind = '',
                metadata = kubernetes.client.models.v1/list_meta.v1.ListMeta(
                    continue = '', 
                    remaining_item_count = 56, 
                    resource_version = '', 
                    self_link = '', )
            )
        else:
            return V1EndpointsList(
                items = [
                    kubernetes.client.models.v1/endpoints.v1.Endpoints(
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
                        subsets = [
                            kubernetes.client.models.v1/endpoint_subset.v1.EndpointSubset(
                                addresses = [
                                    kubernetes.client.models.v1/endpoint_address.v1.EndpointAddress(
                                        hostname = '', 
                                        ip = '', 
                                        node_name = '', 
                                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                                            api_version = '', 
                                            field_path = '', 
                                            kind = '', 
                                            name = '', 
                                            namespace = '', 
                                            resource_version = '', 
                                            uid = '', ), )
                                    ], 
                                not_ready_addresses = [
                                    kubernetes.client.models.v1/endpoint_address.v1.EndpointAddress(
                                        hostname = '', 
                                        ip = '', 
                                        node_name = '', )
                                    ], 
                                ports = [
                                    kubernetes.client.models.core/v1/endpoint_port.core.v1.EndpointPort(
                                        app_protocol = '', 
                                        name = '', 
                                        port = 56, 
                                        protocol = '', )
                                    ], )
                            ], )
                    ],
        )
        """

    def testV1EndpointsList(self):
        """Test V1EndpointsList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
