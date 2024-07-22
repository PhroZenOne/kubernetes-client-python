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

from kubernetes.client.models.v1_se_linux_options import V1SELinuxOptions

class TestV1SELinuxOptions(unittest.TestCase):
    """V1SELinuxOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SELinuxOptions:
        """Test V1SELinuxOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SELinuxOptions`
        """
        model = V1SELinuxOptions()
        if include_optional:
            return V1SELinuxOptions(
                level = '',
                role = '',
                type = '',
                user = ''
            )
        else:
            return V1SELinuxOptions(
        )
        """

    def testV1SELinuxOptions(self):
        """Test V1SELinuxOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
