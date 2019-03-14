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


class RuntimeScriptAction(Model):
    """Describes a script action on a running cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the script action.
    :type name: str
    :param uri: Required. The URI to the script.
    :type uri: str
    :param parameters: The parameters for the script
    :type parameters: str
    :param roles: Required. The list of roles where script will be executed.
    :type roles: list[str]
    :ivar application_name: The application name of the script action, if any.
    :vartype application_name: str
    """

    _validation = {
        'name': {'required': True},
        'uri': {'required': True},
        'roles': {'required': True},
        'application_name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'application_name': {'key': 'applicationName', 'type': 'str'},
    }

    def __init__(self, *, name: str, uri: str, roles, parameters: str=None, **kwargs) -> None:
        super(RuntimeScriptAction, self).__init__(**kwargs)
        self.name = name
        self.uri = uri
        self.parameters = parameters
        self.roles = roles
        self.application_name = None
