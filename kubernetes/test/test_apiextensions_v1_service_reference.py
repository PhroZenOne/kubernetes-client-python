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

from kubernetes.client.models.apiextensions_v1_service_reference import ApiextensionsV1ServiceReference

class TestApiextensionsV1ServiceReference(unittest.TestCase):
    """ApiextensionsV1ServiceReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiextensionsV1ServiceReference:
        """Test ApiextensionsV1ServiceReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiextensionsV1ServiceReference`
        """
        model = ApiextensionsV1ServiceReference()
        if include_optional:
            return ApiextensionsV1ServiceReference(
                name = '',
                namespace = '',
                path = '',
                port = 56
            )
        else:
            return ApiextensionsV1ServiceReference(
                name = '',
                namespace = '',
        )
        """

    def testApiextensionsV1ServiceReference(self):
        """Test ApiextensionsV1ServiceReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
