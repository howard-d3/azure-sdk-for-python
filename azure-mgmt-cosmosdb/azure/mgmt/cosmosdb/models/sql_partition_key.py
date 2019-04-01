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


class SqlPartitionKey(Model):
    """The configuration of the partition key to be used for partitioning data
    into multiple partitions.

    :param paths: List of paths using which data within the SQL container can
     be partitioned
    :type paths: list[str]
    :param kind: Indicates the kind of algorithm used for partitioning.
     Possible values include: 'Hash', 'Range'. Default value: "Hash" .
    :type kind: str or ~azure.mgmt.cosmosdb.models.PartitionKind
    """

    _attribute_map = {
        'paths': {'key': 'paths', 'type': '[str]'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SqlPartitionKey, self).__init__(**kwargs)
        self.paths = kwargs.get('paths', None)
        self.kind = kwargs.get('kind', "Hash")
