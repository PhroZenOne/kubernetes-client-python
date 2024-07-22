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

from kubernetes.client.models.v1_param_ref import V1ParamRef

class TestV1ParamRef(unittest.TestCase):
    """V1ParamRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ParamRef:
        """Test V1ParamRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ParamRef`
        """
        model = V1ParamRef()
        if include_optional:
            return V1ParamRef(
                name = '',
                namespace = '',
                parameter_not_found_action = '',
                selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(
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
                        }, )
            )
        else:
            return V1ParamRef(
        )
        """

    def testV1ParamRef(self):
        """Test V1ParamRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
