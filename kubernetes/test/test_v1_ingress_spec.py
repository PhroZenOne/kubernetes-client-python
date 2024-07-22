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

from kubernetes.client.models.v1_ingress_spec import V1IngressSpec

class TestV1IngressSpec(unittest.TestCase):
    """V1IngressSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1IngressSpec:
        """Test V1IngressSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1IngressSpec`
        """
        model = V1IngressSpec()
        if include_optional:
            return V1IngressSpec(
                default_backend = kubernetes.client.models.v1/ingress_backend.v1.IngressBackend(
                    resource = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                        api_group = '', 
                        kind = '', 
                        name = '', ), 
                    service = kubernetes.client.models.v1/ingress_service_backend.v1.IngressServiceBackend(
                        name = '', 
                        port = kubernetes.client.models.v1/service_backend_port.v1.ServiceBackendPort(
                            name = '', 
                            number = 56, ), ), ),
                ingress_class_name = '',
                rules = [
                    kubernetes.client.models.v1/ingress_rule.v1.IngressRule(
                        host = '', 
                        http = kubernetes.client.models.v1/http_ingress_rule_value.v1.HTTPIngressRuleValue(
                            paths = [
                                kubernetes.client.models.v1/http_ingress_path.v1.HTTPIngressPath(
                                    backend = kubernetes.client.models.v1/ingress_backend.v1.IngressBackend(
                                        resource = kubernetes.client.models.v1/typed_local_object_reference.v1.TypedLocalObjectReference(
                                            api_group = '', 
                                            kind = '', 
                                            name = '', ), 
                                        service = kubernetes.client.models.v1/ingress_service_backend.v1.IngressServiceBackend(
                                            name = '', 
                                            port = kubernetes.client.models.v1/service_backend_port.v1.ServiceBackendPort(
                                                name = '', 
                                                number = 56, ), ), ), 
                                    path = '', 
                                    path_type = '', )
                                ], ), )
                    ],
                tls = [
                    kubernetes.client.models.v1/ingress_tls.v1.IngressTLS(
                        hosts = [
                            ''
                            ], 
                        secret_name = '', )
                    ]
            )
        else:
            return V1IngressSpec(
        )
        """

    def testV1IngressSpec(self):
        """Test V1IngressSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()