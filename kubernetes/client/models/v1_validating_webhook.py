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
from kubernetes.client.models.admissionregistration_v1_webhook_client_config import AdmissionregistrationV1WebhookClientConfig
from kubernetes.client.models.v1_label_selector import V1LabelSelector
from kubernetes.client.models.v1_match_condition import V1MatchCondition
from kubernetes.client.models.v1_rule_with_operations import V1RuleWithOperations
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1ValidatingWebhook(BaseModel):
    """
    ValidatingWebhook describes an admission webhook and the resources and operations it applies to.
    """ # noqa: E501
    admission_review_versions: List[StrictStr] = Field(description="AdmissionReviewVersions is an ordered list of preferred `AdmissionReview` versions the Webhook expects. API server will try to use first version in the list which it supports. If none of the versions specified in this list supported by API server, validation will fail for this object. If a persisted webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail and be subject to the failure policy.", alias="admissionReviewVersions")
    client_config: AdmissionregistrationV1WebhookClientConfig = Field(alias="clientConfig")
    failure_policy: Optional[StrictStr] = Field(default=None, description="FailurePolicy defines how unrecognized errors from the admission endpoint are handled - allowed values are Ignore or Fail. Defaults to Fail.", alias="failurePolicy")
    match_conditions: Optional[List[V1MatchCondition]] = Field(default=None, description="MatchConditions is a list of conditions that must be met for a request to be sent to this webhook. Match conditions filter requests that have already been matched by the rules, namespaceSelector, and objectSelector. An empty list of matchConditions matches all requests. There are a maximum of 64 match conditions allowed.  The exact matching logic is (in order):   1. If ANY matchCondition evaluates to FALSE, the webhook is skipped.   2. If ALL matchConditions evaluate to TRUE, the webhook is called.   3. If any matchCondition evaluates to an error (but none are FALSE):      - If failurePolicy=Fail, reject the request      - If failurePolicy=Ignore, the error is ignored and the webhook is skipped", alias="matchConditions")
    match_policy: Optional[StrictStr] = Field(default=None, description="matchPolicy defines how the \"rules\" list is used to match incoming requests. Allowed values are \"Exact\" or \"Equivalent\".  - Exact: match a request only if it exactly matches a specified rule. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, but \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would not be sent to the webhook.  - Equivalent: match a request if modifies a resource listed in rules, even via another API group or version. For example, if deployments can be modified via apps/v1, apps/v1beta1, and extensions/v1beta1, and \"rules\" only included `apiGroups:[\"apps\"], apiVersions:[\"v1\"], resources: [\"deployments\"]`, a request to apps/v1beta1 or extensions/v1beta1 would be converted to apps/v1 and sent to the webhook.  Defaults to \"Equivalent\"", alias="matchPolicy")
    name: StrictStr = Field(description="The name of the admission webhook. Name should be fully qualified, e.g., imagepolicy.kubernetes.io, where \"imagepolicy\" is the name of the webhook, and kubernetes.io is the name of the organization. Required.")
    namespace_selector: Optional[V1LabelSelector] = Field(default=None, alias="namespaceSelector")
    object_selector: Optional[V1LabelSelector] = Field(default=None, alias="objectSelector")
    rules: Optional[List[V1RuleWithOperations]] = Field(default=None, description="Rules describes what operations on what resources/subresources the webhook cares about. The webhook cares about an operation if it matches _any_ Rule. However, in order to prevent ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks from putting the cluster in a state which cannot be recovered from without completely disabling the plugin, ValidatingAdmissionWebhooks and MutatingAdmissionWebhooks are never called on admission requests for ValidatingWebhookConfiguration and MutatingWebhookConfiguration objects.")
    side_effects: StrictStr = Field(description="SideEffects states whether this webhook has side effects. Acceptable values are: None, NoneOnDryRun (webhooks created via v1beta1 may also specify Some or Unknown). Webhooks with side effects MUST implement a reconciliation system, since a request may be rejected by a future step in the admission chain and the side effects therefore need to be undone. Requests with the dryRun attribute will be auto-rejected if they match a webhook with sideEffects == Unknown or Some.", alias="sideEffects")
    timeout_seconds: Optional[StrictInt] = Field(default=None, description="TimeoutSeconds specifies the timeout for this webhook. After the timeout passes, the webhook call will be ignored or the API call will fail based on the failure policy. The timeout value must be between 1 and 30 seconds. Default to 10 seconds.", alias="timeoutSeconds")
    __properties: ClassVar[List[str]] = ["admissionReviewVersions", "clientConfig", "failurePolicy", "matchConditions", "matchPolicy", "name", "namespaceSelector", "objectSelector", "rules", "sideEffects", "timeoutSeconds"]

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
        """Create an instance of V1ValidatingWebhook from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of client_config
        if self.client_config:
            _dict['clientConfig'] = self.client_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in match_conditions (list)
        _items = []
        if self.match_conditions:
            for _item in self.match_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchConditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of namespace_selector
        if self.namespace_selector:
            _dict['namespaceSelector'] = self.namespace_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object_selector
        if self.object_selector:
            _dict['objectSelector'] = self.object_selector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1ValidatingWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "admissionReviewVersions": obj.get("admissionReviewVersions"),
            "clientConfig": AdmissionregistrationV1WebhookClientConfig.from_dict(obj.get("clientConfig")) if obj.get("clientConfig") is not None else None,
            "failurePolicy": obj.get("failurePolicy"),
            "matchConditions": [V1MatchCondition.from_dict(_item) for _item in obj.get("matchConditions")] if obj.get("matchConditions") is not None else None,
            "matchPolicy": obj.get("matchPolicy"),
            "name": obj.get("name"),
            "namespaceSelector": V1LabelSelector.from_dict(obj.get("namespaceSelector")) if obj.get("namespaceSelector") is not None else None,
            "objectSelector": V1LabelSelector.from_dict(obj.get("objectSelector")) if obj.get("objectSelector") is not None else None,
            "rules": [V1RuleWithOperations.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None,
            "sideEffects": obj.get("sideEffects"),
            "timeoutSeconds": obj.get("timeoutSeconds")
        })
        return _obj


