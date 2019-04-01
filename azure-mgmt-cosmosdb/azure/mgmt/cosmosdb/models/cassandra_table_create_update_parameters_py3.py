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


class CassandraTableCreateUpdateParameters(Model):
    """Parameters to create and update Cosmos DB Cassandra table.

    All required parameters must be populated in order to send to Azure.

    :param resource: Required. The standard JSON format of a Cassandra table
    :type resource: ~azure.mgmt.cosmosdb.models.CassandraTableResource
    :param options: Required. A key-value pair of options to be applied for
     the request. This corresponds to the headers sent with the request.
    :type options: dict[str, str]
    """

    _validation = {
        'resource': {'required': True},
        'options': {'required': True},
    }

    _attribute_map = {
        'resource': {'key': 'properties.resource', 'type': 'CassandraTableResource'},
        'options': {'key': 'properties.options', 'type': '{str}'},
    }

    def __init__(self, *, resource, options, **kwargs) -> None:
        super(CassandraTableCreateUpdateParameters, self).__init__(**kwargs)
        self.resource = resource
        self.options = options
