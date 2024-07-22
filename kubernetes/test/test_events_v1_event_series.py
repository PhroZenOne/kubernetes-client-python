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

from kubernetes.client.models.events_v1_event_series import EventsV1EventSeries

class TestEventsV1EventSeries(unittest.TestCase):
    """EventsV1EventSeries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventsV1EventSeries:
        """Test EventsV1EventSeries
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventsV1EventSeries`
        """
        model = EventsV1EventSeries()
        if include_optional:
            return EventsV1EventSeries(
                count = 56,
                last_observed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return EventsV1EventSeries(
                count = 56,
                last_observed_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testEventsV1EventSeries(self):
        """Test EventsV1EventSeries"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()