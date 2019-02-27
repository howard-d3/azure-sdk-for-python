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


class ResourceGroupDefinition(Model):
    """Represents an Azure resource group in a blueprint definition.

    :param name: Name of this resourceGroup. Leave empty if the resource group
     name will be specified during the blueprint assignment.
    :type name: str
    :param location: Location of this resourceGroup. Leave empty if the
     resource group location will be specified during the blueprint assignment.
    :type location: str
    :param display_name: DisplayName of this parameter/resourceGroup.
    :type display_name: str
    :param description: Description of this parameter/resourceGroup.
    :type description: str
    :param strong_type: StrongType for UI to render rich experience during
     blueprint assignment.
    :type strong_type: str
    :param depends_on: Artifacts which need to be deployed before this
     resource group.
    :type depends_on: list[str]
    :param tags: Tags to be assigned to this resource group.
    :type tags: dict[str, str]
    """

    _validation = {
        'name': {'max_length': 90, 'min_length': 1},
        'location': {'max_length': 90},
        'display_name': {'max_length': 256},
        'description': {'max_length': 500},
        'strong_type': {'max_length': 64},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'display_name': {'key': 'metadata.displayName', 'type': 'str'},
        'description': {'key': 'metadata.description', 'type': 'str'},
        'strong_type': {'key': 'metadata.strongType', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[str]'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, name: str=None, location: str=None, display_name: str=None, description: str=None, strong_type: str=None, depends_on=None, tags=None, **kwargs) -> None:
        super(ResourceGroupDefinition, self).__init__(**kwargs)
        self.name = name
        self.location = location
        self.display_name = display_name
        self.description = description
        self.strong_type = strong_type
        self.depends_on = depends_on
        self.tags = tags
