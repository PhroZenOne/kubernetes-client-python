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

from kubernetes.client.models.v1alpha2_named_resources_allocation_result import V1alpha2NamedResourcesAllocationResult

class TestV1alpha2NamedResourcesAllocationResult(unittest.TestCase):
    """V1alpha2NamedResourcesAllocationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2NamedResourcesAllocationResult:
        """Test V1alpha2NamedResourcesAllocationResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2NamedResourcesAllocationResult`
        """
        model = V1alpha2NamedResourcesAllocationResult()
        if include_optional:
            return V1alpha2NamedResourcesAllocationResult(
                name = ''
            )
        else:
            return V1alpha2NamedResourcesAllocationResult(
                name = '',
        )
        """

    def testV1alpha2NamedResourcesAllocationResult(self):
        """Test V1alpha2NamedResourcesAllocationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
