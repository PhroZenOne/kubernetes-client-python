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
from kubernetes.client.models.v1_match_resources import V1MatchResources
from kubernetes.client.models.v1_param_ref import V1ParamRef
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1ValidatingAdmissionPolicyBindingSpec(BaseModel):
    """
    ValidatingAdmissionPolicyBindingSpec is the specification of the ValidatingAdmissionPolicyBinding.
    """ # noqa: E501
    match_resources: Optional[V1MatchResources] = Field(default=None, alias="matchResources")
    param_ref: Optional[V1ParamRef] = Field(default=None, alias="paramRef")
    policy_name: Optional[StrictStr] = Field(default=None, description="PolicyName references a ValidatingAdmissionPolicy name which the ValidatingAdmissionPolicyBinding binds to. If the referenced resource does not exist, this binding is considered invalid and will be ignored Required.", alias="policyName")
    validation_actions: Optional[List[StrictStr]] = Field(default=None, description="validationActions declares how Validations of the referenced ValidatingAdmissionPolicy are enforced. If a validation evaluates to false it is always enforced according to these actions.  Failures defined by the ValidatingAdmissionPolicy's FailurePolicy are enforced according to these actions only if the FailurePolicy is set to Fail, otherwise the failures are ignored. This includes compilation errors, runtime errors and misconfigurations of the policy.  validationActions is declared as a set of action values. Order does not matter. validationActions may not contain duplicates of the same action.  The supported actions values are:  \"Deny\" specifies that a validation failure results in a denied request.  \"Warn\" specifies that a validation failure is reported to the request client in HTTP Warning headers, with a warning code of 299. Warnings can be sent both for allowed or denied admission responses.  \"Audit\" specifies that a validation failure is included in the published audit event for the request. The audit event will contain a `validation.policy.admission.k8s.io/validation_failure` audit annotation with a value containing the details of the validation failures, formatted as a JSON list of objects, each with the following fields: - message: The validation failure message string - policy: The resource name of the ValidatingAdmissionPolicy - binding: The resource name of the ValidatingAdmissionPolicyBinding - expressionIndex: The index of the failed validations in the ValidatingAdmissionPolicy - validationActions: The enforcement actions enacted for the validation failure Example audit annotation: `\"validation.policy.admission.k8s.io/validation_failure\": \"[{\"message\": \"Invalid value\", {\"policy\": \"policy.example.com\", {\"binding\": \"policybinding.example.com\", {\"expressionIndex\": \"1\", {\"validationActions\": [\"Audit\"]}]\"`  Clients should expect to handle additional values by ignoring any values not recognized.  \"Deny\" and \"Warn\" may not be used together since this combination needlessly duplicates the validation failure both in the API response body and the HTTP warning headers.  Required.", alias="validationActions")
    __properties: ClassVar[List[str]] = ["matchResources", "paramRef", "policyName", "validationActions"]

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
        """Create an instance of V1ValidatingAdmissionPolicyBindingSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of match_resources
        if self.match_resources:
            _dict['matchResources'] = self.match_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of param_ref
        if self.param_ref:
            _dict['paramRef'] = self.param_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1ValidatingAdmissionPolicyBindingSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "matchResources": V1MatchResources.from_dict(obj.get("matchResources")) if obj.get("matchResources") is not None else None,
            "paramRef": V1ParamRef.from_dict(obj.get("paramRef")) if obj.get("paramRef") is not None else None,
            "policyName": obj.get("policyName"),
            "validationActions": obj.get("validationActions")
        })
        return _obj


