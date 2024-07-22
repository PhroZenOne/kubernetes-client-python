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

from kubernetes.client.models.v1_lifecycle_handler import V1LifecycleHandler

class TestV1LifecycleHandler(unittest.TestCase):
    """V1LifecycleHandler unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1LifecycleHandler:
        """Test V1LifecycleHandler
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1LifecycleHandler`
        """
        model = V1LifecycleHandler()
        if include_optional:
            return V1LifecycleHandler(
                var_exec = kubernetes.client.models.v1/exec_action.v1.ExecAction(
                    command = [
                        ''
                        ], ),
                http_get = kubernetes.client.models.v1/http_get_action.v1.HTTPGetAction(
                    host = '', 
                    http_headers = [
                        kubernetes.client.models.v1/http_header.v1.HTTPHeader(
                            name = '', 
                            value = '', )
                        ], 
                    path = '', 
                    port = kubernetes.client.models.port.port(), 
                    scheme = '', ),
                sleep = kubernetes.client.models.v1/sleep_action.v1.SleepAction(
                    seconds = 56, ),
                tcp_socket = kubernetes.client.models.v1/tcp_socket_action.v1.TCPSocketAction(
                    host = '', 
                    port = kubernetes.client.models.port.port(), )
            )
        else:
            return V1LifecycleHandler(
        )
        """

    def testV1LifecycleHandler(self):
        """Test V1LifecycleHandler"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
