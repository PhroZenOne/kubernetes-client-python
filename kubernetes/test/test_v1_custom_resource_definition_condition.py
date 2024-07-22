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

from kubernetes.client.models.v1_custom_resource_definition_condition import V1CustomResourceDefinitionCondition

class TestV1CustomResourceDefinitionCondition(unittest.TestCase):
    """V1CustomResourceDefinitionCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CustomResourceDefinitionCondition:
        """Test V1CustomResourceDefinitionCondition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CustomResourceDefinitionCondition`
        """
        model = V1CustomResourceDefinitionCondition()
        if include_optional:
            return V1CustomResourceDefinitionCondition(
                last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                message = '',
                reason = '',
                status = '',
                type = ''
            )
        else:
            return V1CustomResourceDefinitionCondition(
                status = '',
                type = '',
        )
        """

    def testV1CustomResourceDefinitionCondition(self):
        """Test V1CustomResourceDefinitionCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
