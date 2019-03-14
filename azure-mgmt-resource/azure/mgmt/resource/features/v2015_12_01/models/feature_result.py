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


class FeatureResult(Model):
    """Previewed feature information.

    :param name: The name of the feature.
    :type name: str
    :param properties: Properties of the previewed feature.
    :type properties:
     ~azure.mgmt.resource.features.v2015_12_01.models.FeatureProperties
    :param id: The resource ID of the feature.
    :type id: str
    :param type: The resource type of the feature.
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'FeatureProperties'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(FeatureResult, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)
