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

from kubernetes.client.models.v1_type_checking import V1TypeChecking

class TestV1TypeChecking(unittest.TestCase):
    """V1TypeChecking unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1TypeChecking:
        """Test V1TypeChecking
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1TypeChecking`
        """
        model = V1TypeChecking()
        if include_optional:
            return V1TypeChecking(
                expression_warnings = [
                    kubernetes.client.models.v1/expression_warning.v1.ExpressionWarning(
                        field_ref = '', 
                        warning = '', )
                    ]
            )
        else:
            return V1TypeChecking(
        )
        """

    def testV1TypeChecking(self):
        """Test V1TypeChecking"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()