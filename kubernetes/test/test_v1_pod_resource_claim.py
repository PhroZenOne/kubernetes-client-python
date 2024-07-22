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

from kubernetes.client.models.v1_pod_resource_claim import V1PodResourceClaim

class TestV1PodResourceClaim(unittest.TestCase):
    """V1PodResourceClaim unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PodResourceClaim:
        """Test V1PodResourceClaim
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PodResourceClaim`
        """
        model = V1PodResourceClaim()
        if include_optional:
            return V1PodResourceClaim(
                name = '',
                source = kubernetes.client.models.v1/claim_source.v1.ClaimSource(
                    resource_claim_name = '', 
                    resource_claim_template_name = '', )
            )
        else:
            return V1PodResourceClaim(
                name = '',
        )
        """

    def testV1PodResourceClaim(self):
        """Test V1PodResourceClaim"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()