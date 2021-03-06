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


class CompositeEntityModel(Model):
    """LUIS Composite Entity.

    All required parameters must be populated in order to send to Azure.

    :param parent_type: Required. Type/name of parent entity.
    :type parent_type: str
    :param value: Required. Value for composite entity extracted by LUIS.
    :type value: str
    :param children: Required. Child entities.
    :type children:
     list[~azure.cognitiveservices.language.luis.runtime.models.CompositeChildModel]
    """

    _validation = {
        'parent_type': {'required': True},
        'value': {'required': True},
        'children': {'required': True},
    }

    _attribute_map = {
        'parent_type': {'key': 'parentType', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'children': {'key': 'children', 'type': '[CompositeChildModel]'},
    }

    def __init__(self, *, parent_type: str, value: str, children, **kwargs) -> None:
        super(CompositeEntityModel, self).__init__(**kwargs)
        self.parent_type = parent_type
        self.value = value
        self.children = children
