# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from kubernetes.client.api.policy_api import PolicyApi


class TestPolicyApi(unittest.TestCase):
    """PolicyApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PolicyApi()

    def tearDown(self) -> None:
        pass

    def test_get_api_group(self) -> None:
        """Test case for get_api_group

        """
        pass


if __name__ == '__main__':
    unittest.main()
