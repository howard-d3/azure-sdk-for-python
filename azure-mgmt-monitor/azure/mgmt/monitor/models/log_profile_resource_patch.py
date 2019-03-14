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

from msrest.serialization import Model


class LogProfileResourcePatch(Model):
    """The log profile resource for patch operations.

    All required parameters must be populated in order to send to Azure.

    :param tags: Resource tags
    :type tags: dict[str, str]
    :param storage_account_id: the resource id of the storage account to which
     you would like to send the Activity Log.
    :type storage_account_id: str
    :param service_bus_rule_id: The service bus rule ID of the service bus
     namespace in which you would like to have Event Hubs created for streaming
     the Activity Log. The rule ID is of the format: '{service bus resource
     ID}/authorizationrules/{key name}'.
    :type service_bus_rule_id: str
    :param locations: Required. List of regions for which Activity Log events
     should be stored or streamed. It is a comma separated list of valid ARM
     locations including the 'global' location.
    :type locations: list[str]
    :param categories: Required. the categories of the logs. These categories
     are created as is convenient to the user. Some values are: 'Write',
     'Delete', and/or 'Action.'
    :type categories: list[str]
    :param retention_policy: Required. the retention policy for the events in
     the log.
    :type retention_policy: ~azure.mgmt.monitor.models.RetentionPolicy
    """

    _validation = {
        'locations': {'required': True},
        'categories': {'required': True},
        'retention_policy': {'required': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'locations': {'key': 'properties.locations', 'type': '[str]'},
        'categories': {'key': 'properties.categories', 'type': '[str]'},
        'retention_policy': {'key': 'properties.retentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(self, **kwargs):
        super(LogProfileResourcePatch, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.storage_account_id = kwargs.get('storage_account_id', None)
        self.service_bus_rule_id = kwargs.get('service_bus_rule_id', None)
        self.locations = kwargs.get('locations', None)
        self.categories = kwargs.get('categories', None)
        self.retention_policy = kwargs.get('retention_policy', None)
