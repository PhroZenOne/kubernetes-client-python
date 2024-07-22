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
from kubernetes.client.models.v1_label_selector import V1LabelSelector
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1PodAffinityTerm(BaseModel):
    """
    Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running
    """ # noqa: E501
    label_selector: Optional[V1LabelSelector] = Field(default=None, alias="labelSelector")
    match_label_keys: Optional[List[StrictStr]] = Field(default=None, description="MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate.", alias="matchLabelKeys")
    mismatch_label_keys: Optional[List[StrictStr]] = Field(default=None, description="MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod's pod (anti) affinity. Keys that don't exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn't set. This is an alpha field and requires enabling MatchLabelKeysInPodAffinity feature gate.", alias="mismatchLabelKeys")
    namespace_selector: Optional[V1LabelSelector] = Field(default=None, alias="namespaceSelector")
    namespaces: Optional[List[StrictStr]] = Field(default=None, description="namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means \"this pod's namespace\".")
    topology_key: StrictStr = Field(description="This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.", alias="topologyKey")
    __properties: ClassVar[List[str]] = ["labelSelector", "matchLabelKeys", "mismatchLabelKeys", "namespaceSelector", "namespaces", "topologyKey"]

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
        """Create an instance of V1PodAffinityTerm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of label_selector
        if self.label_selector:
            _dict['labelSelector'] = self.label_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of namespace_selector
        if self.namespace_selector:
            _dict['namespaceSelector'] = self.namespace_selector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1PodAffinityTerm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "labelSelector": V1LabelSelector.from_dict(obj.get("labelSelector")) if obj.get("labelSelector") is not None else None,
            "matchLabelKeys": obj.get("matchLabelKeys"),
            "mismatchLabelKeys": obj.get("mismatchLabelKeys"),
            "namespaceSelector": V1LabelSelector.from_dict(obj.get("namespaceSelector")) if obj.get("namespaceSelector") is not None else None,
            "namespaces": obj.get("namespaces"),
            "topologyKey": obj.get("topologyKey")
        })
        return _obj


