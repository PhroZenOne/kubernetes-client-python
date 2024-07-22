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

from kubernetes.client.models.v1alpha2_driver_allocation_result import V1alpha2DriverAllocationResult

class TestV1alpha2DriverAllocationResult(unittest.TestCase):
    """V1alpha2DriverAllocationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2DriverAllocationResult:
        """Test V1alpha2DriverAllocationResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2DriverAllocationResult`
        """
        model = V1alpha2DriverAllocationResult()
        if include_optional:
            return V1alpha2DriverAllocationResult(
                named_resources = kubernetes.client.models.v1alpha2/named_resources_allocation_result.v1alpha2.NamedResourcesAllocationResult(
                    name = '', ),
                vendor_request_parameters = kubernetes.client.models.vendor_request_parameters.vendorRequestParameters()
            )
        else:
            return V1alpha2DriverAllocationResult(
        )
        """

    def testV1alpha2DriverAllocationResult(self):
        """Test V1alpha2DriverAllocationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()