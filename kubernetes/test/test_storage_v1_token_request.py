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

from kubernetes.client.models.storage_v1_token_request import StorageV1TokenRequest

class TestStorageV1TokenRequest(unittest.TestCase):
    """StorageV1TokenRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StorageV1TokenRequest:
        """Test StorageV1TokenRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StorageV1TokenRequest`
        """
        model = StorageV1TokenRequest()
        if include_optional:
            return StorageV1TokenRequest(
                audience = '',
                expiration_seconds = 56
            )
        else:
            return StorageV1TokenRequest(
                audience = '',
        )
        """

    def testStorageV1TokenRequest(self):
        """Test StorageV1TokenRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
