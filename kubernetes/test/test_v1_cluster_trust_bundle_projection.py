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

from kubernetes.client.models.v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection

class TestV1ClusterTrustBundleProjection(unittest.TestCase):
    """V1ClusterTrustBundleProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ClusterTrustBundleProjection:
        """Test V1ClusterTrustBundleProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ClusterTrustBundleProjection`
        """
        model = V1ClusterTrustBundleProjection()
        if include_optional:
            return V1ClusterTrustBundleProjection(
                label_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
                    match_expressions = [
                        kubernetes.client.models.v1/label_selector_requirement.v1.LabelSelectorRequirement(
                            key = '', 
                            operator = '', 
                            values = [
                                ''
                                ], )
                        ], 
                    match_labels = {
                        'key' : ''
                        }, ),
                name = '',
                optional = True,
                path = '',
                signer_name = ''
            )
        else:
            return V1ClusterTrustBundleProjection(
                path = '',
        )
        """

    def testV1ClusterTrustBundleProjection(self):
        """Test V1ClusterTrustBundleProjection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()