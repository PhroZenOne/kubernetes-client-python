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

from kubernetes.client.models.v1_node_config_source import V1NodeConfigSource

class TestV1NodeConfigSource(unittest.TestCase):
    """V1NodeConfigSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1NodeConfigSource:
        """Test V1NodeConfigSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1NodeConfigSource`
        """
        model = V1NodeConfigSource()
        if include_optional:
            return V1NodeConfigSource(
                config_map = kubernetes.client.models.v1/config_map_node_config_source.v1.ConfigMapNodeConfigSource(
                    kubelet_config_key = '', 
                    name = '', 
                    namespace = '', 
                    resource_version = '', 
                    uid = '', )
            )
        else:
            return V1NodeConfigSource(
        )
        """

    def testV1NodeConfigSource(self):
        """Test V1NodeConfigSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
