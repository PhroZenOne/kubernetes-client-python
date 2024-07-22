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
from kubernetes.client.models.v1_audit_annotation import V1AuditAnnotation
from kubernetes.client.models.v1_match_condition import V1MatchCondition
from kubernetes.client.models.v1_match_resources import V1MatchResources
from kubernetes.client.models.v1_param_kind import V1ParamKind
from kubernetes.client.models.v1_validation import V1Validation
from kubernetes.client.models.v1_variable import V1Variable
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1ValidatingAdmissionPolicySpec(BaseModel):
    """
    ValidatingAdmissionPolicySpec is the specification of the desired behavior of the AdmissionPolicy.
    """ # noqa: E501
    audit_annotations: Optional[List[V1AuditAnnotation]] = Field(default=None, description="auditAnnotations contains CEL expressions which are used to produce audit annotations for the audit event of the API request. validations and auditAnnotations may not both be empty; a least one of validations or auditAnnotations is required.", alias="auditAnnotations")
    failure_policy: Optional[StrictStr] = Field(default=None, description="failurePolicy defines how to handle failures for the admission policy. Failures can occur from CEL expression parse errors, type check errors, runtime errors and invalid or mis-configured policy definitions or bindings.  A policy is invalid if spec.paramKind refers to a non-existent Kind. A binding is invalid if spec.paramRef.name refers to a non-existent resource.  failurePolicy does not define how validations that evaluate to false are handled.  When failurePolicy is set to Fail, ValidatingAdmissionPolicyBinding validationActions define how failures are enforced.  Allowed values are Ignore or Fail. Defaults to Fail.", alias="failurePolicy")
    match_conditions: Optional[List[V1MatchCondition]] = Field(default=None, description="MatchConditions is a list of conditions that must be met for a request to be validated. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  If a parameter object is provided, it can be accessed via the `params` handle in the same manner as validation expressions.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the policy is skipped.   2. If ALL matchConditions evaluate to TRUE, the policy is evaluated.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the policy is skipped", alias="matchConditions")
    match_constraints: Optional[V1MatchResources] = Field(default=None, alias="matchConstraints")
    param_kind: Optional[V1ParamKind] = Field(default=None, alias="paramKind")
    validations: Optional[List[V1Validation]] = Field(default=None, description="Validations contain CEL expressions which is used to apply the validation. Validations and AuditAnnotations may not both be empty; a minimum of one Validations or AuditAnnotations is required.")
    variables: Optional[List[V1Variable]] = Field(default=None, description="Variables contain definitions of variables that can be used in composition of other expressions. Each variable is defined as a named CEL expression. The variables defined here will be available under `variables` in other expressions of the policy except MatchConditions because MatchConditions are evaluated before the rest of the policy.  The expression of a variable can refer to other variables defined earlier in the list but not those after. Thus, Variables must be sorted by the order of first appearance and acyclic.")
    __properties: ClassVar[List[str]] = ["auditAnnotations", "failurePolicy", "matchConditions", "matchConstraints", "paramKind", "validations", "variables"]

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
        """Create an instance of V1ValidatingAdmissionPolicySpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in audit_annotations (list)
        _items = []
        if self.audit_annotations:
            for _item in self.audit_annotations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['auditAnnotations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in match_conditions (list)
        _items = []
        if self.match_conditions:
            for _item in self.match_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchConditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of match_constraints
        if self.match_constraints:
            _dict['matchConstraints'] = self.match_constraints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of param_kind
        if self.param_kind:
            _dict['paramKind'] = self.param_kind.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in validations (list)
        _items = []
        if self.validations:
            for _item in self.validations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in variables (list)
        _items = []
        if self.variables:
            for _item in self.variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['variables'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1ValidatingAdmissionPolicySpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auditAnnotations": [V1AuditAnnotation.from_dict(_item) for _item in obj.get("auditAnnotations")] if obj.get("auditAnnotations") is not None else None,
            "failurePolicy": obj.get("failurePolicy"),
            "matchConditions": [V1MatchCondition.from_dict(_item) for _item in obj.get("matchConditions")] if obj.get("matchConditions") is not None else None,
            "matchConstraints": V1MatchResources.from_dict(obj.get("matchConstraints")) if obj.get("matchConstraints") is not None else None,
            "paramKind": V1ParamKind.from_dict(obj.get("paramKind")) if obj.get("paramKind") is not None else None,
            "validations": [V1Validation.from_dict(_item) for _item in obj.get("validations")] if obj.get("validations") is not None else None,
            "variables": [V1Variable.from_dict(_item) for _item in obj.get("variables")] if obj.get("variables") is not None else None
        })
        return _obj

