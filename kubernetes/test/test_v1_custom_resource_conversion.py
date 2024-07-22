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

from kubernetes.client.models.v1_custom_resource_conversion import V1CustomResourceConversion

class TestV1CustomResourceConversion(unittest.TestCase):
    """V1CustomResourceConversion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1CustomResourceConversion:
        """Test V1CustomResourceConversion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1CustomResourceConversion`
        """
        model = V1CustomResourceConversion()
        if include_optional:
            return V1CustomResourceConversion(
                strategy = '',
                webhook = kubernetes.client.models.v1/webhook_conversion.v1.WebhookConversion(
                    kubernetes.client_config = kubernetes.client.models.apiextensions/v1/webhook_client_config.apiextensions.v1.WebhookClientConfig(
                        ca_bundle = 'YQ==', 
                        service = kubernetes.client.models.apiextensions/v1/service_reference.apiextensions.v1.ServiceReference(
                            name = '', 
                            namespace = '', 
                            path = '', 
                            port = 56, ), 
                        url = '', ), 
                    conversion_review_versions = [
                        ''
                        ], )
            )
        else:
            return V1CustomResourceConversion(
                strategy = '',
        )
        """

    def testV1CustomResourceConversion(self):
        """Test V1CustomResourceConversion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
