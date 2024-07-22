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

from kubernetes.client.models.v2_container_resource_metric_status import V2ContainerResourceMetricStatus

class TestV2ContainerResourceMetricStatus(unittest.TestCase):
    """V2ContainerResourceMetricStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2ContainerResourceMetricStatus:
        """Test V2ContainerResourceMetricStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2ContainerResourceMetricStatus`
        """
        model = V2ContainerResourceMetricStatus()
        if include_optional:
            return V2ContainerResourceMetricStatus(
                container = '',
                current = kubernetes.client.models.v2/metric_value_status.v2.MetricValueStatus(
                    average_utilization = 56, 
                    average_value = '', 
                    value = '', ),
                name = ''
            )
        else:
            return V2ContainerResourceMetricStatus(
                container = '',
                current = kubernetes.client.models.v2/metric_value_status.v2.MetricValueStatus(
                    average_utilization = 56, 
                    average_value = '', 
                    value = '', ),
                name = '',
        )
        """

    def testV2ContainerResourceMetricStatus(self):
        """Test V2ContainerResourceMetricStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()