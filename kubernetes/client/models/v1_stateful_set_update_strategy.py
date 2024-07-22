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
from kubernetes.client.models.v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1StatefulSetUpdateStrategy(BaseModel):
    """
    StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.
    """ # noqa: E501
    rolling_update: Optional[V1RollingUpdateStatefulSetStrategy] = Field(default=None, alias="rollingUpdate")
    type: Optional[StrictStr] = Field(default=None, description="Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.")
    __properties: ClassVar[List[str]] = ["rollingUpdate", "type"]

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
        """Create an instance of V1StatefulSetUpdateStrategy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rolling_update
        if self.rolling_update:
            _dict['rollingUpdate'] = self.rolling_update.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1StatefulSetUpdateStrategy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rollingUpdate": V1RollingUpdateStatefulSetStrategy.from_dict(obj.get("rollingUpdate")) if obj.get("rollingUpdate") is not None else None,
            "type": obj.get("type")
        })
        return _obj


