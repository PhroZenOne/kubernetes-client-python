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
from kubernetes.client.models.v1alpha2_named_resources_attribute import V1alpha2NamedResourcesAttribute
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1alpha2NamedResourcesInstance(BaseModel):
    """
    NamedResourcesInstance represents one individual hardware instance that can be selected based on its attributes.
    """ # noqa: E501
    attributes: Optional[List[V1alpha2NamedResourcesAttribute]] = Field(default=None, description="Attributes defines the attributes of this resource instance. The name of each attribute must be unique.")
    name: StrictStr = Field(description="Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain.")
    __properties: ClassVar[List[str]] = ["attributes", "name"]

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
        """Create an instance of V1alpha2NamedResourcesInstance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1alpha2NamedResourcesInstance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributes": [V1alpha2NamedResourcesAttribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None,
            "name": obj.get("name")
        })
        return _obj

