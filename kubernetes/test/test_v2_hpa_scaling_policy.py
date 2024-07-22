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

from kubernetes.client.models.v2_hpa_scaling_policy import V2HPAScalingPolicy

class TestV2HPAScalingPolicy(unittest.TestCase):
    """V2HPAScalingPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2HPAScalingPolicy:
        """Test V2HPAScalingPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2HPAScalingPolicy`
        """
        model = V2HPAScalingPolicy()
        if include_optional:
            return V2HPAScalingPolicy(
                period_seconds = 56,
                type = '',
                value = 56
            )
        else:
            return V2HPAScalingPolicy(
                period_seconds = 56,
                type = '',
                value = 56,
        )
        """

    def testV2HPAScalingPolicy(self):
        """Test V2HPAScalingPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
