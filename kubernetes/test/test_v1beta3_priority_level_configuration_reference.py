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

from kubernetes.client.models.v1beta3_priority_level_configuration_reference import V1beta3PriorityLevelConfigurationReference

class TestV1beta3PriorityLevelConfigurationReference(unittest.TestCase):
    """V1beta3PriorityLevelConfigurationReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta3PriorityLevelConfigurationReference:
        """Test V1beta3PriorityLevelConfigurationReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta3PriorityLevelConfigurationReference`
        """
        model = V1beta3PriorityLevelConfigurationReference()
        if include_optional:
            return V1beta3PriorityLevelConfigurationReference(
                name = ''
            )
        else:
            return V1beta3PriorityLevelConfigurationReference(
                name = '',
        )
        """

    def testV1beta3PriorityLevelConfigurationReference(self):
        """Test V1beta3PriorityLevelConfigurationReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()