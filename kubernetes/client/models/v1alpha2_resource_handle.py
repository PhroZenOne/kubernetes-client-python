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
from kubernetes.client.models.v1alpha2_structured_resource_handle import V1alpha2StructuredResourceHandle
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1alpha2ResourceHandle(BaseModel):
    """
    ResourceHandle holds opaque resource data for processing by a specific kubelet plugin.
    """ # noqa: E501
    data: Optional[StrictStr] = Field(default=None, description="Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced.")
    driver_name: Optional[StrictStr] = Field(default=None, description="DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle's data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in.", alias="driverName")
    structured_data: Optional[V1alpha2StructuredResourceHandle] = Field(default=None, alias="structuredData")
    __properties: ClassVar[List[str]] = ["data", "driverName", "structuredData"]

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
        """Create an instance of V1alpha2ResourceHandle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of structured_data
        if self.structured_data:
            _dict['structuredData'] = self.structured_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1alpha2ResourceHandle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": obj.get("data"),
            "driverName": obj.get("driverName"),
            "structuredData": V1alpha2StructuredResourceHandle.from_dict(obj.get("structuredData")) if obj.get("structuredData") is not None else None
        })
        return _obj


