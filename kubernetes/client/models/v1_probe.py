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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from kubernetes.client.models.v1_exec_action import V1ExecAction
from kubernetes.client.models.v1_grpc_action import V1GRPCAction
from kubernetes.client.models.v1_http_get_action import V1HTTPGetAction
from kubernetes.client.models.v1_tcp_socket_action import V1TCPSocketAction
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1Probe(BaseModel):
    """
    Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.
    """ # noqa: E501
    var_exec: Optional[V1ExecAction] = Field(default=None, alias="exec")
    failure_threshold: Optional[StrictInt] = Field(default=None, description="Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.", alias="failureThreshold")
    grpc: Optional[V1GRPCAction] = None
    http_get: Optional[V1HTTPGetAction] = Field(default=None, alias="httpGet")
    initial_delay_seconds: Optional[StrictInt] = Field(default=None, description="Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes", alias="initialDelaySeconds")
    period_seconds: Optional[StrictInt] = Field(default=None, description="How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.", alias="periodSeconds")
    success_threshold: Optional[StrictInt] = Field(default=None, description="Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.", alias="successThreshold")
    tcp_socket: Optional[V1TCPSocketAction] = Field(default=None, alias="tcpSocket")
    termination_grace_period_seconds: Optional[StrictInt] = Field(default=None, description="Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.", alias="terminationGracePeriodSeconds")
    timeout_seconds: Optional[StrictInt] = Field(default=None, description="Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes", alias="timeoutSeconds")
    __properties: ClassVar[List[str]] = ["exec", "failureThreshold", "grpc", "httpGet", "initialDelaySeconds", "periodSeconds", "successThreshold", "tcpSocket", "terminationGracePeriodSeconds", "timeoutSeconds"]

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
        """Create an instance of V1Probe from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_exec
        if self.var_exec:
            _dict['exec'] = self.var_exec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grpc
        if self.grpc:
            _dict['grpc'] = self.grpc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of http_get
        if self.http_get:
            _dict['httpGet'] = self.http_get.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tcp_socket
        if self.tcp_socket:
            _dict['tcpSocket'] = self.tcp_socket.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of V1Probe from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exec": V1ExecAction.from_dict(obj.get("exec")) if obj.get("exec") is not None else None,
            "failureThreshold": obj.get("failureThreshold"),
            "grpc": V1GRPCAction.from_dict(obj.get("grpc")) if obj.get("grpc") is not None else None,
            "httpGet": V1HTTPGetAction.from_dict(obj.get("httpGet")) if obj.get("httpGet") is not None else None,
            "initialDelaySeconds": obj.get("initialDelaySeconds"),
            "periodSeconds": obj.get("periodSeconds"),
            "successThreshold": obj.get("successThreshold"),
            "tcpSocket": V1TCPSocketAction.from_dict(obj.get("tcpSocket")) if obj.get("tcpSocket") is not None else None,
            "terminationGracePeriodSeconds": obj.get("terminationGracePeriodSeconds"),
            "timeoutSeconds": obj.get("timeoutSeconds")
        })
        return _obj


