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

from kubernetes.client.models.v1_self_subject_access_review import V1SelfSubjectAccessReview

class TestV1SelfSubjectAccessReview(unittest.TestCase):
    """V1SelfSubjectAccessReview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SelfSubjectAccessReview:
        """Test V1SelfSubjectAccessReview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SelfSubjectAccessReview`
        """
        model = V1SelfSubjectAccessReview()
        if include_optional:
            return V1SelfSubjectAccessReview(
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
                spec = kubernetes.client.models.v1/self_subject_access_review_spec.v1.SelfSubjectAccessReviewSpec(
                    non_resource_attributes = kubernetes.client.models.v1/non_resource_attributes.v1.NonResourceAttributes(
                        path = '', 
                        verb = '', ), 
                    resource_attributes = kubernetes.client.models.v1/resource_attributes.v1.ResourceAttributes(
                        group = '', 
                        name = '', 
                        namespace = '', 
                        resource = '', 
                        subresource = '', 
                        verb = '', 
                        version = '', ), ),
                status = kubernetes.client.models.v1/subject_access_review_status.v1.SubjectAccessReviewStatus(
                    allowed = True, 
                    denied = True, 
                    evaluation_error = '', 
                    reason = '', )
            )
        else:
            return V1SelfSubjectAccessReview(
                spec = kubernetes.client.models.v1/self_subject_access_review_spec.v1.SelfSubjectAccessReviewSpec(
                    non_resource_attributes = kubernetes.client.models.v1/non_resource_attributes.v1.NonResourceAttributes(
                        path = '', 
                        verb = '', ), 
                    resource_attributes = kubernetes.client.models.v1/resource_attributes.v1.ResourceAttributes(
                        group = '', 
                        name = '', 
                        namespace = '', 
                        resource = '', 
                        subresource = '', 
                        verb = '', 
                        version = '', ), ),
        )
        """

    def testV1SelfSubjectAccessReview(self):
        """Test V1SelfSubjectAccessReview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
