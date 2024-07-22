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

from kubernetes.client.models.v1_endpoint_slice import V1EndpointSlice

class TestV1EndpointSlice(unittest.TestCase):
    """V1EndpointSlice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1EndpointSlice:
        """Test V1EndpointSlice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1EndpointSlice`
        """
        model = V1EndpointSlice()
        if include_optional:
            return V1EndpointSlice(
                address_type = '',
                api_version = '',
                endpoints = [
                    kubernetes.client.models.v1/endpoint.v1.Endpoint(
                        addresses = [
                            ''
                            ], 
                        conditions = kubernetes.client.models.v1/endpoint_conditions.v1.EndpointConditions(
                            ready = True, 
                            serving = True, 
                            terminating = True, ), 
                        deprecated_topology = {
                            'key' : ''
                            }, 
                        hints = kubernetes.client.models.v1/endpoint_hints.v1.EndpointHints(
                            for_zones = [
                                kubernetes.client.models.v1/for_zone.v1.ForZone(
                                    name = '', )
                                ], ), 
                        hostname = '', 
                        node_name = '', 
                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '', 
                            field_path = '', 
                            kind = '', 
                            name = '', 
                            namespace = '', 
                            resource_version = '', 
                            uid = '', ), 
                        zone = '', )
                    ],
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
                ports = [
                    kubernetes.client.models.discovery/v1/endpoint_port.discovery.v1.EndpointPort(
                        app_protocol = '', 
                        name = '', 
                        port = 56, 
                        protocol = '', )
                    ]
            )
        else:
            return V1EndpointSlice(
                address_type = '',
                endpoints = [
                    kubernetes.client.models.v1/endpoint.v1.Endpoint(
                        addresses = [
                            ''
                            ], 
                        conditions = kubernetes.client.models.v1/endpoint_conditions.v1.EndpointConditions(
                            ready = True, 
                            serving = True, 
                            terminating = True, ), 
                        deprecated_topology = {
                            'key' : ''
                            }, 
                        hints = kubernetes.client.models.v1/endpoint_hints.v1.EndpointHints(
                            for_zones = [
                                kubernetes.client.models.v1/for_zone.v1.ForZone(
                                    name = '', )
                                ], ), 
                        hostname = '', 
                        node_name = '', 
                        target_ref = kubernetes.client.models.v1/object_reference.v1.ObjectReference(
                            api_version = '', 
                            field_path = '', 
                            kind = '', 
                            name = '', 
                            namespace = '', 
                            resource_version = '', 
                            uid = '', ), 
                        zone = '', )
                    ],
        )
        """

    def testV1EndpointSlice(self):
        """Test V1EndpointSlice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
