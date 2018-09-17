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


class RegisteredServerCreateParameters(Model):
    """The parameters used when creating a storage sync service.

    :param location: Required. Gets or sets the location of the resource. This
     will be one of the supported and registered Azure Geo Regions (e.g. West
     US, East US, Southeast Asia, etc.). The geo region of a resource cannot be
     changed once it is created, but if an identical geo region is specified on
     update, the request will succeed.
    :type location: str
    :param tags: Gets or sets a list of key value pairs that describe the
     resource. These tags can be used for viewing and grouping this resource
     (across resource groups). A maximum of 15 tags can be provided for a
     resource. Each tag must have a key with a length no greater than 128
     characters and a value with a length no greater than 256 characters.
    :type tags: dict[str, str]
    :param server_certificate: Registered Server Certificate
    :type server_certificate: str
    :param agent_version: Registered Server Agent Version
    :type agent_version: str
    :param server_os_version: Registered Server OS Version
    :type server_os_version: str
    :param last_heart_beat: Registered Server last heart beat
    :type last_heart_beat: str
    :param server_role: Registered Server serverRole
    :type server_role: str
    :param cluster_id: Registered Server clusterId
    :type cluster_id: str
    :param cluster_name: Registered Server clusterName
    :type cluster_name: str
    :param server_id: Registered Server serverId
    :type server_id: str
    :param friendly_name: Friendly Name
    :type friendly_name: str
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'server_certificate': {'key': 'properties.serverCertificate', 'type': 'str'},
        'agent_version': {'key': 'properties.agentVersion', 'type': 'str'},
        'server_os_version': {'key': 'properties.serverOSVersion', 'type': 'str'},
        'last_heart_beat': {'key': 'properties.lastHeartBeat', 'type': 'str'},
        'server_role': {'key': 'properties.serverRole', 'type': 'str'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'str'},
        'cluster_name': {'key': 'properties.clusterName', 'type': 'str'},
        'server_id': {'key': 'properties.serverId', 'type': 'str'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegisteredServerCreateParameters, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.server_certificate = kwargs.get('server_certificate', None)
        self.agent_version = kwargs.get('agent_version', None)
        self.server_os_version = kwargs.get('server_os_version', None)
        self.last_heart_beat = kwargs.get('last_heart_beat', None)
        self.server_role = kwargs.get('server_role', None)
        self.cluster_id = kwargs.get('cluster_id', None)
        self.cluster_name = kwargs.get('cluster_name', None)
        self.server_id = kwargs.get('server_id', None)
        self.friendly_name = kwargs.get('friendly_name', None)