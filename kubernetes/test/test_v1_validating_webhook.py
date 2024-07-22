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

from kubernetes.client.models.v1_validating_webhook import V1ValidatingWebhook

class TestV1ValidatingWebhook(unittest.TestCase):
    """V1ValidatingWebhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ValidatingWebhook:
        """Test V1ValidatingWebhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ValidatingWebhook`
        """
        model = V1ValidatingWebhook()
        if include_optional:
            return V1ValidatingWebhook(
                admission_review_versions = [
                    ''
                    ],
                kubernetes.client_config = kubernetes.client.models.admissionregistration/v1/webhook_client_config.admissionregistration.v1.WebhookClientConfig(
                    ca_bundle = 'YQ==', 
                    service = kubernetes.client.models.admissionregistration/v1/service_reference.admissionregistration.v1.ServiceReference(
                        name = '', 
                        namespace = '', 
                        path = '', 
                        port = 56, ), 
                    url = '', ),
                failure_policy = '',
                match_conditions = [
                    kubernetes.client.models.v1/match_condition.v1.MatchCondition(
                        expression = '', 
                        name = '', )
                    ],
                match_policy = '',
                name = '',
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
                object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                rules = [
                    kubernetes.client.models.v1/rule_with_operations.v1.RuleWithOperations(
                        api_groups = [
                            ''
                            ], 
                        api_versions = [
                            ''
                            ], 
                        operations = [
                            ''
                            ], 
                        resources = [
                            ''
                            ], 
                        scope = '', )
                    ],
                side_effects = '',
                timeout_seconds = 56
            )
        else:
            return V1ValidatingWebhook(
                admission_review_versions = [
                    ''
                    ],
                kubernetes.client_config = kubernetes.client.models.admissionregistration/v1/webhook_client_config.admissionregistration.v1.WebhookClientConfig(
                    ca_bundle = 'YQ==', 
                    service = kubernetes.client.models.admissionregistration/v1/service_reference.admissionregistration.v1.ServiceReference(
                        name = '', 
                        namespace = '', 
                        path = '', 
                        port = 56, ), 
                    url = '', ),
                name = '',
                side_effects = '',
        )
        """

    def testV1ValidatingWebhook(self):
        """Test V1ValidatingWebhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
