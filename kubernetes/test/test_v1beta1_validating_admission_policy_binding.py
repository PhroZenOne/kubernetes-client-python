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

from kubernetes.client.models.v1beta1_validating_admission_policy_binding import V1beta1ValidatingAdmissionPolicyBinding

class TestV1beta1ValidatingAdmissionPolicyBinding(unittest.TestCase):
    """V1beta1ValidatingAdmissionPolicyBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1ValidatingAdmissionPolicyBinding:
        """Test V1beta1ValidatingAdmissionPolicyBinding
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1ValidatingAdmissionPolicyBinding`
        """
        model = V1beta1ValidatingAdmissionPolicyBinding()
        if include_optional:
            return V1beta1ValidatingAdmissionPolicyBinding(
                api_version = '',
                kind = '',
                metadata = kubernetes.client.models.v1/object_meta.v1.ObjectMeta(
                    annotations = {
                        'key' : ''
                        }, 
                    creation_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    deletion_grace_period_seconds = 56, 
                    deletion_timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    finalizers = [
                        ''
                        ], 
                    generate_name = '', 
                    generation = 56, 
                    labels = {
                        'key' : ''
                        }, 
                    managed_fields = [
                        kubernetes.client.models.v1/managed_fields_entry.v1.ManagedFieldsEntry(
                            api_version = '', 
                            fields_type = '', 
                            fields_v1 = kubernetes.client.models.fields_v1.fieldsV1(), 
                            manager = '', 
                            operation = '', 
                            subresource = '', 
                            time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    name = '', 
                    namespace = '', 
                    owner_references = [
                        kubernetes.client.models.v1/owner_reference.v1.OwnerReference(
                            api_version = '', 
                            block_owner_deletion = True, 
                            controller = True, 
                            kind = '', 
                            name = '', 
                            uid = '', )
                        ], 
                    resource_version = '', 
                    self_link = '', 
                    uid = '', ),
                spec = kubernetes.client.models.v1beta1/validating_admission_policy_binding_spec.v1beta1.ValidatingAdmissionPolicyBindingSpec(
                    match_resources = kubernetes.client.models.v1beta1/match_resources.v1beta1.MatchResources(
                        exclude_resource_rules = [
                            kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
                                api_groups = [
                                    ''
                                    ], 
                                api_versions = [
                                    ''
                                    ], 
                                operations = [
                                    ''
                                    ], 
                                resource_names = [
                                    ''
                                    ], 
                                resources = [
                                    ''
                                    ], 
                                scope = '', )
                            ], 
                        match_policy = '', 
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
                        object_selector = kubernetes.client.models.v1/label_selector.v1.LabelSelector(), 
                        resource_rules = [
                            kubernetes.client.models.v1beta1/named_rule_with_operations.v1beta1.NamedRuleWithOperations(
                                scope = '', )
                            ], ), 
                    param_ref = kubernetes.client.models.v1beta1/param_ref.v1beta1.ParamRef(
                        name = '', 
                        namespace = '', 
                        parameter_not_found_action = '', 
                        selector = , ), 
                    policy_name = '', 
                    validation_actions = [
                        ''
                        ], )
            )
        else:
            return V1beta1ValidatingAdmissionPolicyBinding(
        )
        """

    def testV1beta1ValidatingAdmissionPolicyBinding(self):
        """Test V1beta1ValidatingAdmissionPolicyBinding"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()