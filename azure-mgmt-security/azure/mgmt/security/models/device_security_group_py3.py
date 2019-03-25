# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class DeviceSecurityGroup(Resource):
    """The device security group resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param threshold_rules: A list of threshold custom alert rules.
    :type threshold_rules:
     list[~azure.mgmt.security.models.ThresholdCustomAlertRule]
    :param time_window_rules: A list of time window custom alert rules.
    :type time_window_rules:
     list[~azure.mgmt.security.models.TimeWindowCustomAlertRule]
    :param allowlist_rules: A list of allow-list custom alert rules.
    :type allowlist_rules:
     list[~azure.mgmt.security.models.AllowlistCustomAlertRule]
    :param denylist_rules: A list of deny-list custom alert rules.
    :type denylist_rules:
     list[~azure.mgmt.security.models.DenylistCustomAlertRule]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'threshold_rules': {'key': 'properties.thresholdRules', 'type': '[ThresholdCustomAlertRule]'},
        'time_window_rules': {'key': 'properties.timeWindowRules', 'type': '[TimeWindowCustomAlertRule]'},
        'allowlist_rules': {'key': 'properties.allowlistRules', 'type': '[AllowlistCustomAlertRule]'},
        'denylist_rules': {'key': 'properties.denylistRules', 'type': '[DenylistCustomAlertRule]'},
    }

    def __init__(self, *, threshold_rules=None, time_window_rules=None, allowlist_rules=None, denylist_rules=None, **kwargs) -> None:
        super(DeviceSecurityGroup, self).__init__(**kwargs)
        self.threshold_rules = threshold_rules
        self.time_window_rules = time_window_rules
        self.allowlist_rules = allowlist_rules
        self.denylist_rules = denylist_rules
