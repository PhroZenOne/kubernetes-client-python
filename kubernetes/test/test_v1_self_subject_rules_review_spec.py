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

from kubernetes.client.models.v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec

class TestV1SelfSubjectRulesReviewSpec(unittest.TestCase):
    """V1SelfSubjectRulesReviewSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SelfSubjectRulesReviewSpec:
        """Test V1SelfSubjectRulesReviewSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SelfSubjectRulesReviewSpec`
        """
        model = V1SelfSubjectRulesReviewSpec()
        if include_optional:
            return V1SelfSubjectRulesReviewSpec(
                namespace = ''
            )
        else:
            return V1SelfSubjectRulesReviewSpec(
        )
        """

    def testV1SelfSubjectRulesReviewSpec(self):
        """Test V1SelfSubjectRulesReviewSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
