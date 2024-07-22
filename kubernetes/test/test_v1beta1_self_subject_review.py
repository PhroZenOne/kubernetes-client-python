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

from kubernetes.client.models.v1beta1_self_subject_review import V1beta1SelfSubjectReview

class TestV1beta1SelfSubjectReview(unittest.TestCase):
    """V1beta1SelfSubjectReview unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1beta1SelfSubjectReview:
        """Test V1beta1SelfSubjectReview
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1beta1SelfSubjectReview`
        """
        model = V1beta1SelfSubjectReview()
        if include_optional:
            return V1beta1SelfSubjectReview(
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
                status = kubernetes.client.models.v1beta1/self_subject_review_status.v1beta1.SelfSubjectReviewStatus(
                    user_info = kubernetes.client.models.v1/user_info.v1.UserInfo(
                        extra = {
                            'key' : [
                                ''
                                ]
                            }, 
                        groups = [
                            ''
                            ], 
                        uid = '', 
                        username = '', ), )
            )
        else:
            return V1beta1SelfSubjectReview(
        )
        """

    def testV1beta1SelfSubjectReview(self):
        """Test V1beta1SelfSubjectReview"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()