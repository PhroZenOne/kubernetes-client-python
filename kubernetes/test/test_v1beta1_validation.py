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

from kubernetes.client.models.v1beta1_validation import V1beta1Validation

class TestV1beta1Validation(unittest.TestCase):
    """V1beta1Validation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1Validation:
        """Test V1beta1Validation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1Validation`
        """
        model = V1beta1Validation()
        if include_optional:
            return V1beta1Validation(
                expression = '',
                message = '',
                message_expression = '',
                reason = ''
            )
        else:
            return V1beta1Validation(
                expression = '',
        )
        """

    def testV1beta1Validation(self):
        """Test V1beta1Validation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
