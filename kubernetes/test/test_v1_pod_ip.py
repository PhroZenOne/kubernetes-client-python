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

from kubernetes.client.models.v1_pod_ip import V1PodIP

class TestV1PodIP(unittest.TestCase):
    """V1PodIP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PodIP:
        """Test V1PodIP
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PodIP`
        """
        model = V1PodIP()
        if include_optional:
            return V1PodIP(
                ip = ''
            )
        else:
            return V1PodIP(
        )
        """

    def testV1PodIP(self):
        """Test V1PodIP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()