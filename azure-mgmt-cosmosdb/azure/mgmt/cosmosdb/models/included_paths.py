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


class IncludedPaths(Model):
    """The paths that are included in indexing.

    :param path: The path for which the indexing behavior applies to. Index
     paths typically start with root and end with wildcard (/path/*)
    :type path: str
    :param indexes: List of indexes for this path
    :type indexes: list[~azure.mgmt.cosmosdb.models.Indexes]
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'indexes': {'key': 'indexes', 'type': '[Indexes]'},
    }

    def __init__(self, **kwargs):
        super(IncludedPaths, self).__init__(**kwargs)
        self.path = kwargs.get('path', None)
        self.indexes = kwargs.get('indexes', None)
