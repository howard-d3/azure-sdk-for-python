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


class RedisCreateParameters(Model):
    """Parameters supplied to the Create Redis operation.

    All required parameters must be populated in order to send to Azure.

    :param redis_configuration: All Redis Settings. Few possible keys:
     rdb-backup-enabled,rdb-storage-connection-string,rdb-backup-frequency,maxmemory-delta,maxmemory-policy,notify-keyspace-events,maxmemory-samples,slowlog-log-slower-than,slowlog-max-len,list-max-ziplist-entries,list-max-ziplist-value,hash-max-ziplist-entries,hash-max-ziplist-value,set-max-intset-entries,zset-max-ziplist-entries,zset-max-ziplist-value
     etc.
    :type redis_configuration: dict[str, str]
    :param enable_non_ssl_port: Specifies whether the non-ssl Redis server
     port (6379) is enabled.
    :type enable_non_ssl_port: bool
    :param tenant_settings: A dictionary of tenant settings
    :type tenant_settings: dict[str, str]
    :param shard_count: The number of shards to be created on a Premium
     Cluster Cache.
    :type shard_count: int
    :param minimum_tls_version: Optional: requires clients to use a specified
     TLS version (or higher) to connect (e,g, '1.0', '1.1', '1.2'). Possible
     values include: '1.0', '1.1', '1.2'
    :type minimum_tls_version: str or ~azure.mgmt.redis.models.TlsVersion
    :param sku: Required. The SKU of the Redis cache to deploy.
    :type sku: ~azure.mgmt.redis.models.Sku
    :param subnet_id: The full resource ID of a subnet in a virtual network to
     deploy the Redis cache in. Example format:
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/Microsoft.{Network|ClassicNetwork}/VirtualNetworks/vnet1/subnets/subnet1
    :type subnet_id: str
    :param static_ip: Static IP address. Required when deploying a Redis cache
     inside an existing Azure Virtual Network.
    :type static_ip: str
    :param zones: A list of availability zones denoting where the resource
     needs to come from.
    :type zones: list[str]
    :param location: Required. The geo-location where the resource lives
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    """

    _validation = {
        'sku': {'required': True},
        'subnet_id': {'pattern': r'^/subscriptions/[^/]*/resourceGroups/[^/]*/providers/Microsoft.(ClassicNetwork|Network)/virtualNetworks/[^/]*/subnets/[^/]*$'},
        'static_ip': {'pattern': r'^\d+\.\d+\.\d+\.\d+$'},
        'location': {'required': True},
    }

    _attribute_map = {
        'redis_configuration': {'key': 'properties.redisConfiguration', 'type': '{str}'},
        'enable_non_ssl_port': {'key': 'properties.enableNonSslPort', 'type': 'bool'},
        'tenant_settings': {'key': 'properties.tenantSettings', 'type': '{str}'},
        'shard_count': {'key': 'properties.shardCount', 'type': 'int'},
        'minimum_tls_version': {'key': 'properties.minimumTlsVersion', 'type': 'str'},
        'sku': {'key': 'properties.sku', 'type': 'Sku'},
        'subnet_id': {'key': 'properties.subnetId', 'type': 'str'},
        'static_ip': {'key': 'properties.staticIP', 'type': 'str'},
        'zones': {'key': 'zones', 'type': '[str]'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(RedisCreateParameters, self).__init__(**kwargs)
        self.redis_configuration = kwargs.get('redis_configuration', None)
        self.enable_non_ssl_port = kwargs.get('enable_non_ssl_port', None)
        self.tenant_settings = kwargs.get('tenant_settings', None)
        self.shard_count = kwargs.get('shard_count', None)
        self.minimum_tls_version = kwargs.get('minimum_tls_version', None)
        self.sku = kwargs.get('sku', None)
        self.subnet_id = kwargs.get('subnet_id', None)
        self.static_ip = kwargs.get('static_ip', None)
        self.zones = kwargs.get('zones', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
