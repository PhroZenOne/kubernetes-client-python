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

from kubernetes.client.models.v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy

class TestV1RollingUpdateStatefulSetStrategy(unittest.TestCase):
    """V1RollingUpdateStatefulSetStrategy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1RollingUpdateStatefulSetStrategy:
        """Test V1RollingUpdateStatefulSetStrategy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1RollingUpdateStatefulSetStrategy`
        """
        model = V1RollingUpdateStatefulSetStrategy()
        if include_optional:
            return V1RollingUpdateStatefulSetStrategy(
                max_unavailable = None,
                partition = 56
            )
        else:
            return V1RollingUpdateStatefulSetStrategy(
        )
        """

    def testV1RollingUpdateStatefulSetStrategy(self):
        """Test V1RollingUpdateStatefulSetStrategy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
