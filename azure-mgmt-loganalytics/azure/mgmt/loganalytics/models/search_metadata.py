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


class SearchMetadata(Model):
    """Metadata for search results.

    :param search_id: The request id of the search.
    :type search_id: str
    :param result_type: The search result type.
    :type result_type: str
    :param total: The total number of search results.
    :type total: long
    :param top: The number of top search results.
    :type top: long
    :param id: The id of the search results request.
    :type id: str
    :param core_summaries: The core summaries.
    :type core_summaries: list[~azure.mgmt.loganalytics.models.CoreSummary]
    :param status: The status of the search results.
    :type status: str
    :param start_time: The start time for the search.
    :type start_time: datetime
    :param last_updated: The time of last update.
    :type last_updated: datetime
    :param e_tag: The ETag of the search results.
    :type e_tag: str
    :param sort: How the results are sorted.
    :type sort: list[~azure.mgmt.loganalytics.models.SearchSort]
    :param request_time: The request time.
    :type request_time: long
    :param aggregated_value_field: The aggregated value field.
    :type aggregated_value_field: str
    :param aggregated_grouping_fields: The aggregated grouping fields.
    :type aggregated_grouping_fields: str
    :param sum: The sum of all aggregates returned in the result set.
    :type sum: long
    :param max: The max of all aggregates returned in the result set.
    :type max: long
    :param schema: The schema.
    :type schema: ~azure.mgmt.loganalytics.models.SearchMetadataSchema
    """

    _attribute_map = {
        'search_id': {'key': 'requestId', 'type': 'str'},
        'result_type': {'key': 'resultType', 'type': 'str'},
        'total': {'key': 'total', 'type': 'long'},
        'top': {'key': 'top', 'type': 'long'},
        'id': {'key': 'id', 'type': 'str'},
        'core_summaries': {'key': 'coreSummaries', 'type': '[CoreSummary]'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'sort': {'key': 'sort', 'type': '[SearchSort]'},
        'request_time': {'key': 'requestTime', 'type': 'long'},
        'aggregated_value_field': {'key': 'aggregatedValueField', 'type': 'str'},
        'aggregated_grouping_fields': {'key': 'aggregatedGroupingFields', 'type': 'str'},
        'sum': {'key': 'sum', 'type': 'long'},
        'max': {'key': 'max', 'type': 'long'},
        'schema': {'key': 'schema', 'type': 'SearchMetadataSchema'},
    }

    def __init__(self, **kwargs):
        super(SearchMetadata, self).__init__(**kwargs)
        self.search_id = kwargs.get('search_id', None)
        self.result_type = kwargs.get('result_type', None)
        self.total = kwargs.get('total', None)
        self.top = kwargs.get('top', None)
        self.id = kwargs.get('id', None)
        self.core_summaries = kwargs.get('core_summaries', None)
        self.status = kwargs.get('status', None)
        self.start_time = kwargs.get('start_time', None)
        self.last_updated = kwargs.get('last_updated', None)
        self.e_tag = kwargs.get('e_tag', None)
        self.sort = kwargs.get('sort', None)
        self.request_time = kwargs.get('request_time', None)
        self.aggregated_value_field = kwargs.get('aggregated_value_field', None)
        self.aggregated_grouping_fields = kwargs.get('aggregated_grouping_fields', None)
        self.sum = kwargs.get('sum', None)
        self.max = kwargs.get('max', None)
        self.schema = kwargs.get('schema', None)
