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

from kubernetes.client.models.v1_port_status import V1PortStatus

class TestV1PortStatus(unittest.TestCase):
    """V1PortStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PortStatus:
        """Test V1PortStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PortStatus`
        """
        model = V1PortStatus()
        if include_optional:
            return V1PortStatus(
                error = '',
                port = 56,
                protocol = ''
            )
        else:
            return V1PortStatus(
                port = 56,
                protocol = '',
        )
        """

    def testV1PortStatus(self):
        """Test V1PortStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
