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

from kubernetes.client.models.v1_sysctl import V1Sysctl

class TestV1Sysctl(unittest.TestCase):
    """V1Sysctl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1Sysctl:
        """Test V1Sysctl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1Sysctl`
        """
        model = V1Sysctl()
        if include_optional:
            return V1Sysctl(
                name = '',
                value = ''
            )
        else:
            return V1Sysctl(
                name = '',
                value = '',
        )
        """

    def testV1Sysctl(self):
        """Test V1Sysctl"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
