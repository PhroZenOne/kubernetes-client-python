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

from kubernetes.client.models.v1_service_account_token_projection import V1ServiceAccountTokenProjection

class TestV1ServiceAccountTokenProjection(unittest.TestCase):
    """V1ServiceAccountTokenProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ServiceAccountTokenProjection:
        """Test V1ServiceAccountTokenProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ServiceAccountTokenProjection`
        """
        model = V1ServiceAccountTokenProjection()
        if include_optional:
            return V1ServiceAccountTokenProjection(
                audience = '',
                expiration_seconds = 56,
                path = ''
            )
        else:
            return V1ServiceAccountTokenProjection(
                path = '',
        )
        """

    def testV1ServiceAccountTokenProjection(self):
        """Test V1ServiceAccountTokenProjection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
