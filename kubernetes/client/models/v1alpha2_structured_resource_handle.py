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
from kubernetes.client.models.v1alpha2_driver_allocation_result import V1alpha2DriverAllocationResult
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1alpha2StructuredResourceHandle(BaseModel):
    """
    StructuredResourceHandle is the in-tree representation of the allocation result.
    """ # noqa: E501
    node_name: Optional[StrictStr] = Field(default=None, description="NodeName is the name of the node providing the necessary resources if the resources are local to a node.", alias="nodeName")
    results: List[V1alpha2DriverAllocationResult] = Field(description="Results lists all allocated driver resources.")
    vendor_claim_parameters: Optional[Dict[str, Any]] = Field(default=None, description="VendorClaimParameters are the per-claim configuration parameters from the resource claim parameters at the time that the claim was allocated.", alias="vendorClaimParameters")
    vendor_class_parameters: Optional[Dict[str, Any]] = Field(default=None, description="VendorClassParameters are the per-claim configuration parameters from the resource class at the time that the claim was allocated.", alias="vendorClassParameters")
    __properties: ClassVar[List[str]] = ["nodeName", "results", "vendorClaimParameters", "vendorClassParameters"]

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
        """Create an instance of V1alpha2StructuredResourceHandle from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1alpha2StructuredResourceHandle from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nodeName": obj.get("nodeName"),
            "results": [V1alpha2DriverAllocationResult.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None,
            "vendorClaimParameters": obj.get("vendorClaimParameters"),
            "vendorClassParameters": obj.get("vendorClassParameters")
        })
        return _obj

