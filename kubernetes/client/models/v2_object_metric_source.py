# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: release-1.30
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from kubernetes.client.models.v2_cross_version_object_reference import V2CrossVersionObjectReference
from kubernetes.client.models.v2_metric_identifier import V2MetricIdentifier
from kubernetes.client.models.v2_metric_target import V2MetricTarget
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V2ObjectMetricSource(BaseModel):
    """
    ObjectMetricSource indicates how to scale on a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).
    """ # noqa: E501
    described_object: V2CrossVersionObjectReference = Field(alias="describedObject")
    metric: V2MetricIdentifier
    target: V2MetricTarget
    __properties: ClassVar[List[str]] = ["describedObject", "metric", "target"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V2ObjectMetricSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of described_object
        if self.described_object:
            _dict['describedObject'] = self.described_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V2ObjectMetricSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "describedObject": V2CrossVersionObjectReference.from_dict(obj.get("describedObject")) if obj.get("describedObject") is not None else None,
            "metric": V2MetricIdentifier.from_dict(obj.get("metric")) if obj.get("metric") is not None else None,
            "target": V2MetricTarget.from_dict(obj.get("target")) if obj.get("target") is not None else None
        })
        return _obj


