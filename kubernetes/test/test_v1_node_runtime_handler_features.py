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

from kubernetes.client.models.v1_node_runtime_handler_features import V1NodeRuntimeHandlerFeatures

class TestV1NodeRuntimeHandlerFeatures(unittest.TestCase):
    """V1NodeRuntimeHandlerFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1NodeRuntimeHandlerFeatures:
        """Test V1NodeRuntimeHandlerFeatures
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1NodeRuntimeHandlerFeatures`
        """
        model = V1NodeRuntimeHandlerFeatures()
        if include_optional:
            return V1NodeRuntimeHandlerFeatures(
                recursive_read_only_mounts = True
            )
        else:
            return V1NodeRuntimeHandlerFeatures(
        )
        """

    def testV1NodeRuntimeHandlerFeatures(self):
        """Test V1NodeRuntimeHandlerFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()