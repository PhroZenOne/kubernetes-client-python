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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from kubernetes.client.models.v1_aggregation_rule import V1AggregationRule
from kubernetes.client.models.v1_object_meta import V1ObjectMeta
from kubernetes.client.models.v1_policy_rule import V1PolicyRule
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1ClusterRole(BaseModel):
    """
    ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding.
    """ # noqa: E501
    aggregation_rule: Optional[V1AggregationRule] = Field(default=None, alias="aggregationRule")
    api_version: Optional[StrictStr] = Field(default=None, description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", alias="apiVersion")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    rules: Optional[List[V1PolicyRule]] = Field(default=None, description="Rules holds all the PolicyRules for this ClusterRole")
    __properties: ClassVar[List[str]] = ["aggregationRule", "apiVersion", "kind", "metadata", "rules"]

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
        """Create an instance of V1ClusterRole from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aggregation_rule
        if self.aggregation_rule:
            _dict['aggregationRule'] = self.aggregation_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1ClusterRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationRule": V1AggregationRule.from_dict(obj.get("aggregationRule")) if obj.get("aggregationRule") is not None else None,
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "rules": [V1PolicyRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None
        })
        return _obj


