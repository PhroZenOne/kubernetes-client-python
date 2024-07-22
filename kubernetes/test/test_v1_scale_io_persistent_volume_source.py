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

from kubernetes.client.models.v1_scale_io_persistent_volume_source import V1ScaleIOPersistentVolumeSource

class TestV1ScaleIOPersistentVolumeSource(unittest.TestCase):
    """V1ScaleIOPersistentVolumeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ScaleIOPersistentVolumeSource:
        """Test V1ScaleIOPersistentVolumeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ScaleIOPersistentVolumeSource`
        """
        model = V1ScaleIOPersistentVolumeSource()
        if include_optional:
            return V1ScaleIOPersistentVolumeSource(
                fs_type = '',
                gateway = '',
                protection_domain = '',
                read_only = True,
                secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                ssl_enabled = True,
                storage_mode = '',
                storage_pool = '',
                system = '',
                volume_name = ''
            )
        else:
            return V1ScaleIOPersistentVolumeSource(
                gateway = '',
                secret_ref = kubernetes.client.models.v1/secret_reference.v1.SecretReference(
                    name = '', 
                    namespace = '', ),
                system = '',
        )
        """

    def testV1ScaleIOPersistentVolumeSource(self):
        """Test V1ScaleIOPersistentVolumeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
