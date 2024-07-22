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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1VsphereVirtualDiskVolumeSource(BaseModel):
    """
    Represents a vSphere volume resource.
    """ # noqa: E501
    fs_type: Optional[StrictStr] = Field(default=None, description="fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified.", alias="fsType")
    storage_policy_id: Optional[StrictStr] = Field(default=None, description="storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.", alias="storagePolicyID")
    storage_policy_name: Optional[StrictStr] = Field(default=None, description="storagePolicyName is the storage Policy Based Management (SPBM) profile name.", alias="storagePolicyName")
    volume_path: StrictStr = Field(description="volumePath is the path that identifies vSphere volume vmdk", alias="volumePath")
    __properties: ClassVar[List[str]] = ["fsType", "storagePolicyID", "storagePolicyName", "volumePath"]

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
        """Create an instance of V1VsphereVirtualDiskVolumeSource from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1VsphereVirtualDiskVolumeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fsType": obj.get("fsType"),
            "storagePolicyID": obj.get("storagePolicyID"),
            "storagePolicyName": obj.get("storagePolicyName"),
            "volumePath": obj.get("volumePath")
        })
        return _obj


