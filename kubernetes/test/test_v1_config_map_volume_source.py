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

from kubernetes.client.models.v1_config_map_volume_source import V1ConfigMapVolumeSource

class TestV1ConfigMapVolumeSource(unittest.TestCase):
    """V1ConfigMapVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ConfigMapVolumeSource:
        """Test V1ConfigMapVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ConfigMapVolumeSource`
        """
        model = V1ConfigMapVolumeSource()
        if include_optional:
            return V1ConfigMapVolumeSource(
                default_mode = 56,
                items = [
                    kubernetes.client.models.v1/key_to_path.v1.KeyToPath(
                        key = '', 
                        mode = 56, 
                        path = '', )
                    ],
                name = '',
                optional = True
            )
        else:
            return V1ConfigMapVolumeSource(
        )
        """

    def testV1ConfigMapVolumeSource(self):
        """Test V1ConfigMapVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
