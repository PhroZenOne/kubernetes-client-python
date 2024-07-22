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

from kubernetes.client.models.v1alpha2_resource_claim_status import V1alpha2ResourceClaimStatus

class TestV1alpha2ResourceClaimStatus(unittest.TestCase):
    """V1alpha2ResourceClaimStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2ResourceClaimStatus:
        """Test V1alpha2ResourceClaimStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2ResourceClaimStatus`
        """
        model = V1alpha2ResourceClaimStatus()
        if include_optional:
            return V1alpha2ResourceClaimStatus(
                allocation = kubernetes.client.models.v1alpha2/allocation_result.v1alpha2.AllocationResult(
                    available_on_nodes = kubernetes.client.models.v1/node_selector.v1.NodeSelector(
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
                            ], ), 
                    resource_handles = [
                        kubernetes.client.models.v1alpha2/resource_handle.v1alpha2.ResourceHandle(
                            data = '', 
                            driver_name = '', 
                            structured_data = kubernetes.client.models.v1alpha2/structured_resource_handle.v1alpha2.StructuredResourceHandle(
                                node_name = '', 
                                results = [
                                    kubernetes.client.models.v1alpha2/driver_allocation_result.v1alpha2.DriverAllocationResult(
                                        named_resources = kubernetes.client.models.v1alpha2/named_resources_allocation_result.v1alpha2.NamedResourcesAllocationResult(
                                            name = '', ), 
                                        vendor_request_parameters = kubernetes.client.models.vendor_request_parameters.vendorRequestParameters(), )
                                    ], 
                                vendor_claim_parameters = kubernetes.client.models.vendor_claim_parameters.vendorClaimParameters(), 
                                vendor_class_parameters = kubernetes.client.models.vendor_class_parameters.vendorClassParameters(), ), )
                        ], 
                    shareable = True, ),
                deallocation_requested = True,
                driver_name = '',
                reserved_for = [
                    kubernetes.client.models.v1alpha2/resource_claim_consumer_reference.v1alpha2.ResourceClaimConsumerReference(
                        api_group = '', 
                        name = '', 
                        resource = '', 
                        uid = '', )
                    ]
            )
        else:
            return V1alpha2ResourceClaimStatus(
        )
        """

    def testV1alpha2ResourceClaimStatus(self):
        """Test V1alpha2ResourceClaimStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
