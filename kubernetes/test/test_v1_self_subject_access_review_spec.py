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

from kubernetes.client.models.v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpec

class TestV1SelfSubjectAccessReviewSpec(unittest.TestCase):
    """V1SelfSubjectAccessReviewSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SelfSubjectAccessReviewSpec:
        """Test V1SelfSubjectAccessReviewSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SelfSubjectAccessReviewSpec`
        """
        model = V1SelfSubjectAccessReviewSpec()
        if include_optional:
            return V1SelfSubjectAccessReviewSpec(
                non_resource_attributes = kubernetes.client.models.v1/non_resource_attributes.v1.NonResourceAttributes(
                    path = '', 
                    verb = '', ),
                resource_attributes = kubernetes.client.models.v1/resource_attributes.v1.ResourceAttributes(
                    group = '', 
                    name = '', 
                    namespace = '', 
                    resource = '', 
                    subresource = '', 
                    verb = '', 
                    version = '', )
            )
        else:
            return V1SelfSubjectAccessReviewSpec(
        )
        """

    def testV1SelfSubjectAccessReviewSpec(self):
        """Test V1SelfSubjectAccessReviewSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
