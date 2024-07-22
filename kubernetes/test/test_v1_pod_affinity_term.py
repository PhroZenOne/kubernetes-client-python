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

from kubernetes.client.models.v1_pod_affinity_term import V1PodAffinityTerm

class TestV1PodAffinityTerm(unittest.TestCase):
    """V1PodAffinityTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1PodAffinityTerm:
        """Test V1PodAffinityTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1PodAffinityTerm`
        """
        model = V1PodAffinityTerm()
        if include_optional:
            return V1PodAffinityTerm(
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
                match_label_keys = [
                    ''
                    ],
                mismatch_label_keys = [
                    ''
                    ],
                namespace_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                namespaces = [
                    ''
                    ],
                topology_key = ''
            )
        else:
            return V1PodAffinityTerm(
                topology_key = '',
        )
        """

    def testV1PodAffinityTerm(self):
        """Test V1PodAffinityTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
