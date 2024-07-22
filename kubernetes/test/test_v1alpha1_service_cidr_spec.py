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

from kubernetes.client.models.v1alpha1_service_cidr_spec import V1alpha1ServiceCIDRSpec

class TestV1alpha1ServiceCIDRSpec(unittest.TestCase):
    """V1alpha1ServiceCIDRSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1ServiceCIDRSpec:
        """Test V1alpha1ServiceCIDRSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1ServiceCIDRSpec`
        """
        model = V1alpha1ServiceCIDRSpec()
        if include_optional:
            return V1alpha1ServiceCIDRSpec(
                cidrs = [
                    ''
                    ]
            )
        else:
            return V1alpha1ServiceCIDRSpec(
        )
        """

    def testV1alpha1ServiceCIDRSpec(self):
        """Test V1alpha1ServiceCIDRSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
