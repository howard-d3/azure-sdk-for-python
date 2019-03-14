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

from .proxy_resource import ProxyResource


class RecommendedIndex(ProxyResource):
    """Represents a database recommended index.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar action: The proposed index action. You can create a missing index,
     drop an unused index, or rebuild an existing index to improve its
     performance. Possible values include: 'Create', 'Drop', 'Rebuild'
    :vartype action: str or ~azure.mgmt.sql.models.RecommendedIndexAction
    :ivar state: The current recommendation state. Possible values include:
     'Active', 'Pending', 'Executing', 'Verifying', 'Pending Revert',
     'Reverting', 'Reverted', 'Ignored', 'Expired', 'Blocked', 'Success'
    :vartype state: str or ~azure.mgmt.sql.models.RecommendedIndexState
    :ivar created: The UTC datetime showing when this resource was created
     (ISO8601 format).
    :vartype created: datetime
    :ivar last_modified: The UTC datetime of when was this resource last
     changed (ISO8601 format).
    :vartype last_modified: datetime
    :ivar index_type: The type of index (CLUSTERED, NONCLUSTERED, COLUMNSTORE,
     CLUSTERED COLUMNSTORE). Possible values include: 'CLUSTERED',
     'NONCLUSTERED', 'COLUMNSTORE', 'CLUSTERED COLUMNSTORE'
    :vartype index_type: str or ~azure.mgmt.sql.models.RecommendedIndexType
    :ivar schema: The schema where table to build index over resides
    :vartype schema: str
    :ivar table: The table on which to build index.
    :vartype table: str
    :ivar columns: Columns over which to build index
    :vartype columns: list[str]
    :ivar included_columns: The list of column names to be included in the
     index
    :vartype included_columns: list[str]
    :ivar index_script: The full build index script
    :vartype index_script: str
    :ivar estimated_impact: The estimated impact of doing recommended index
     action.
    :vartype estimated_impact: list[~azure.mgmt.sql.models.OperationImpact]
    :ivar reported_impact: The values reported after index action is complete.
    :vartype reported_impact: list[~azure.mgmt.sql.models.OperationImpact]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'action': {'readonly': True},
        'state': {'readonly': True},
        'created': {'readonly': True},
        'last_modified': {'readonly': True},
        'index_type': {'readonly': True},
        'schema': {'readonly': True},
        'table': {'readonly': True},
        'columns': {'readonly': True},
        'included_columns': {'readonly': True},
        'index_script': {'readonly': True},
        'estimated_impact': {'readonly': True},
        'reported_impact': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'action': {'key': 'properties.action', 'type': 'RecommendedIndexAction'},
        'state': {'key': 'properties.state', 'type': 'RecommendedIndexState'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'last_modified': {'key': 'properties.lastModified', 'type': 'iso-8601'},
        'index_type': {'key': 'properties.indexType', 'type': 'RecommendedIndexType'},
        'schema': {'key': 'properties.schema', 'type': 'str'},
        'table': {'key': 'properties.table', 'type': 'str'},
        'columns': {'key': 'properties.columns', 'type': '[str]'},
        'included_columns': {'key': 'properties.includedColumns', 'type': '[str]'},
        'index_script': {'key': 'properties.indexScript', 'type': 'str'},
        'estimated_impact': {'key': 'properties.estimatedImpact', 'type': '[OperationImpact]'},
        'reported_impact': {'key': 'properties.reportedImpact', 'type': '[OperationImpact]'},
    }

    def __init__(self, **kwargs):
        super(RecommendedIndex, self).__init__(**kwargs)
        self.action = None
        self.state = None
        self.created = None
        self.last_modified = None
        self.index_type = None
        self.schema = None
        self.table = None
        self.columns = None
        self.included_columns = None
        self.index_script = None
        self.estimated_impact = None
        self.reported_impact = None
