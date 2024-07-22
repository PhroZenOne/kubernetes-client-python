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

from kubernetes.client.models.v1_horizontal_pod_autoscaler_spec import V1HorizontalPodAutoscalerSpec

class TestV1HorizontalPodAutoscalerSpec(unittest.TestCase):
    """V1HorizontalPodAutoscalerSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1HorizontalPodAutoscalerSpec:
        """Test V1HorizontalPodAutoscalerSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1HorizontalPodAutoscalerSpec`
        """
        model = V1HorizontalPodAutoscalerSpec()
        if include_optional:
            return V1HorizontalPodAutoscalerSpec(
                max_replicas = 56,
                min_replicas = 56,
                scale_target_ref = kubernetes.client.models.v1/cross_version_object_reference.v1.CrossVersionObjectReference(
                    api_version = '', 
                    kind = '', 
                    name = '', ),
                target_cpu_utilization_percentage = 56
            )
        else:
            return V1HorizontalPodAutoscalerSpec(
                max_replicas = 56,
                scale_target_ref = kubernetes.client.models.v1/cross_version_object_reference.v1.CrossVersionObjectReference(
                    api_version = '', 
                    kind = '', 
                    name = '', ),
        )
        """

    def testV1HorizontalPodAutoscalerSpec(self):
        """Test V1HorizontalPodAutoscalerSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
