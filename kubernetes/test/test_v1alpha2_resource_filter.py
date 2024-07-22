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

from kubernetes.client.models.v1alpha2_resource_filter import V1alpha2ResourceFilter

class TestV1alpha2ResourceFilter(unittest.TestCase):
    """V1alpha2ResourceFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1alpha2ResourceFilter:
        """Test V1alpha2ResourceFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1alpha2ResourceFilter`
        """
        model = V1alpha2ResourceFilter()
        if include_optional:
            return V1alpha2ResourceFilter(
                driver_name = '',
                named_resources = kubernetes.client.models.v1alpha2/named_resources_filter.v1alpha2.NamedResourcesFilter(
                    selector = '', )
            )
        else:
            return V1alpha2ResourceFilter(
        )
        """

    def testV1alpha2ResourceFilter(self):
        """Test V1alpha2ResourceFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
