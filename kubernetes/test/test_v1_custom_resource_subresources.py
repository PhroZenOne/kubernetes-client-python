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

from kubernetes.client.models.v1_custom_resource_subresources import V1CustomResourceSubresources

class TestV1CustomResourceSubresources(unittest.TestCase):
    """V1CustomResourceSubresources unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CustomResourceSubresources:
        """Test V1CustomResourceSubresources
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CustomResourceSubresources`
        """
        model = V1CustomResourceSubresources()
        if include_optional:
            return V1CustomResourceSubresources(
                scale = kubernetes.client.models.v1/custom_resource_subresource_scale.v1.CustomResourceSubresourceScale(
                    label_selector_path = '', 
                    spec_replicas_path = '', 
                    status_replicas_path = '', ),
                status = kubernetes.client.models.status.status()
            )
        else:
            return V1CustomResourceSubresources(
        )
        """

    def testV1CustomResourceSubresources(self):
        """Test V1CustomResourceSubresources"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
