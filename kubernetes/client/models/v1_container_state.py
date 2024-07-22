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
from pydantic import BaseModel
from kubernetes.client.models.v1_container_state_running import V1ContainerStateRunning
from kubernetes.client.models.v1_container_state_terminated import V1ContainerStateTerminated
from kubernetes.client.models.v1_container_state_waiting import V1ContainerStateWaiting
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1ContainerState(BaseModel):
    """
    ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.
    """ # noqa: E501
    running: Optional[V1ContainerStateRunning] = None
    terminated: Optional[V1ContainerStateTerminated] = None
    waiting: Optional[V1ContainerStateWaiting] = None
    __properties: ClassVar[List[str]] = ["running", "terminated", "waiting"]

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
        """Create an instance of V1ContainerState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of running
        if self.running:
            _dict['running'] = self.running.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terminated
        if self.terminated:
            _dict['terminated'] = self.terminated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of waiting
        if self.waiting:
            _dict['waiting'] = self.waiting.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1ContainerState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "running": V1ContainerStateRunning.from_dict(obj.get("running")) if obj.get("running") is not None else None,
            "terminated": V1ContainerStateTerminated.from_dict(obj.get("terminated")) if obj.get("terminated") is not None else None,
            "waiting": V1ContainerStateWaiting.from_dict(obj.get("waiting")) if obj.get("waiting") is not None else None
        })
        return _obj


