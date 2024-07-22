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

from kubernetes.client.models.v1alpha1_ip_address_spec import V1alpha1IPAddressSpec

class TestV1alpha1IPAddressSpec(unittest.TestCase):
    """V1alpha1IPAddressSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha1IPAddressSpec:
        """Test V1alpha1IPAddressSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha1IPAddressSpec`
        """
        model = V1alpha1IPAddressSpec()
        if include_optional:
            return V1alpha1IPAddressSpec(
                parent_ref = kubernetes.client.models.v1alpha1/parent_reference.v1alpha1.ParentReference(
                    group = '', 
                    name = '', 
                    namespace = '', 
                    resource = '', )
            )
        else:
            return V1alpha1IPAddressSpec(
                parent_ref = kubernetes.client.models.v1alpha1/parent_reference.v1alpha1.ParentReference(
                    group = '', 
                    name = '', 
                    namespace = '', 
                    resource = '', ),
        )
        """

    def testV1alpha1IPAddressSpec(self):
        """Test V1alpha1IPAddressSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()