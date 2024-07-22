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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from kubernetes.client.models.v1_object_meta import V1ObjectMeta
from kubernetes.client.models.v1alpha2_driver_requests import V1alpha2DriverRequests
from kubernetes.client.models.v1alpha2_resource_claim_parameters_reference import V1alpha2ResourceClaimParametersReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1alpha2ResourceClaimParameters(BaseModel):
    """
    ResourceClaimParameters defines resource requests for a ResourceClaim in an in-tree format understood by Kubernetes.
    """ # noqa: E501
    api_version: Optional[StrictStr] = Field(default=None, description="APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources", alias="apiVersion")
    driver_requests: Optional[List[V1alpha2DriverRequests]] = Field(default=None, description="DriverRequests describes all resources that are needed for the allocated claim. A single claim may use resources coming from different drivers. For each driver, this array has at most one entry which then may have one or more per-driver requests.  May be empty, in which case the claim can always be allocated.", alias="driverRequests")
    generated_from: Optional[V1alpha2ResourceClaimParametersReference] = Field(default=None, alias="generatedFrom")
    kind: Optional[StrictStr] = Field(default=None, description="Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds")
    metadata: Optional[V1ObjectMeta] = None
    shareable: Optional[StrictBool] = Field(default=None, description="Shareable indicates whether the allocated claim is meant to be shareable by multiple consumers at the same time.")
    __properties: ClassVar[List[str]] = ["apiVersion", "driverRequests", "generatedFrom", "kind", "metadata", "shareable"]

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
        """Create an instance of V1alpha2ResourceClaimParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in driver_requests (list)
        _items = []
        if self.driver_requests:
            for _item in self.driver_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['driverRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of generated_from
        if self.generated_from:
            _dict['generatedFrom'] = self.generated_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1alpha2ResourceClaimParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "apiVersion": obj.get("apiVersion"),
            "driverRequests": [V1alpha2DriverRequests.from_dict(_item) for _item in obj.get("driverRequests")] if obj.get("driverRequests") is not None else None,
            "generatedFrom": V1alpha2ResourceClaimParametersReference.from_dict(obj.get("generatedFrom")) if obj.get("generatedFrom") is not None else None,
            "kind": obj.get("kind"),
            "metadata": V1ObjectMeta.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "shareable": obj.get("shareable")
        })
        return _obj


