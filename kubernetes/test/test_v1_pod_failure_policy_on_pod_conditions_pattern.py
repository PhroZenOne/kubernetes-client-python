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

from kubernetes.client.models.v1_pod_failure_policy_on_pod_conditions_pattern import V1PodFailurePolicyOnPodConditionsPattern

class TestV1PodFailurePolicyOnPodConditionsPattern(unittest.TestCase):
    """V1PodFailurePolicyOnPodConditionsPattern unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PodFailurePolicyOnPodConditionsPattern:
        """Test V1PodFailurePolicyOnPodConditionsPattern
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PodFailurePolicyOnPodConditionsPattern`
        """
        model = V1PodFailurePolicyOnPodConditionsPattern()
        if include_optional:
            return V1PodFailurePolicyOnPodConditionsPattern(
                status = '',
                type = ''
            )
        else:
            return V1PodFailurePolicyOnPodConditionsPattern(
                status = '',
                type = '',
        )
        """

    def testV1PodFailurePolicyOnPodConditionsPattern(self):
        """Test V1PodFailurePolicyOnPodConditionsPattern"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()