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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from kubernetes.client.models.v1_stateful_set_condition import V1StatefulSetCondition
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1StatefulSetStatus(BaseModel):
    """
    StatefulSetStatus represents the current state of a StatefulSet.
    """ # noqa: E501
    available_replicas: Optional[StrictInt] = Field(default=None, description="Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset.", alias="availableReplicas")
    collision_count: Optional[StrictInt] = Field(default=None, description="collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.", alias="collisionCount")
    conditions: Optional[List[V1StatefulSetCondition]] = Field(default=None, description="Represents the latest available observations of a statefulset's current state.")
    current_replicas: Optional[StrictInt] = Field(default=None, description="currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.", alias="currentReplicas")
    current_revision: Optional[StrictStr] = Field(default=None, description="currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).", alias="currentRevision")
    observed_generation: Optional[StrictInt] = Field(default=None, description="observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet's generation, which is updated on mutation by the API Server.", alias="observedGeneration")
    ready_replicas: Optional[StrictInt] = Field(default=None, description="readyReplicas is the number of pods created for this StatefulSet with a Ready Condition.", alias="readyReplicas")
    replicas: StrictInt = Field(description="replicas is the number of Pods created by the StatefulSet controller.")
    update_revision: Optional[StrictStr] = Field(default=None, description="updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)", alias="updateRevision")
    updated_replicas: Optional[StrictInt] = Field(default=None, description="updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.", alias="updatedReplicas")
    __properties: ClassVar[List[str]] = ["availableReplicas", "collisionCount", "conditions", "currentReplicas", "currentRevision", "observedGeneration", "readyReplicas", "replicas", "updateRevision", "updatedReplicas"]

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
        """Create an instance of V1StatefulSetStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item in self.conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1StatefulSetStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableReplicas": obj.get("availableReplicas"),
            "collisionCount": obj.get("collisionCount"),
            "conditions": [V1StatefulSetCondition.from_dict(_item) for _item in obj.get("conditions")] if obj.get("conditions") is not None else None,
            "currentReplicas": obj.get("currentReplicas"),
            "currentRevision": obj.get("currentRevision"),
            "observedGeneration": obj.get("observedGeneration"),
            "readyReplicas": obj.get("readyReplicas"),
            "replicas": obj.get("replicas"),
            "updateRevision": obj.get("updateRevision"),
            "updatedReplicas": obj.get("updatedReplicas")
        })
        return _obj


