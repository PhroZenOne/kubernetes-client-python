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

from kubernetes.client.models.v1_replication_controller_status import V1ReplicationControllerStatus

class TestV1ReplicationControllerStatus(unittest.TestCase):
    """V1ReplicationControllerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ReplicationControllerStatus:
        """Test V1ReplicationControllerStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ReplicationControllerStatus`
        """
        model = V1ReplicationControllerStatus()
        if include_optional:
            return V1ReplicationControllerStatus(
                available_replicas = 56,
                conditions = [
                    kubernetes.client.models.v1/replication_controller_condition.v1.ReplicationControllerCondition(
                        last_transition_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        reason = '', 
                        status = '', 
                        type = '', )
                    ],
                fully_labeled_replicas = 56,
                observed_generation = 56,
                ready_replicas = 56,
                replicas = 56
            )
        else:
            return V1ReplicationControllerStatus(
                replicas = 56,
        )
        """

    def testV1ReplicationControllerStatus(self):
        """Test V1ReplicationControllerStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
