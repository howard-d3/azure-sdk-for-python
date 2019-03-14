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

from .resource_py3 import Resource


class ApplicationGateway(Resource):
    """Application gateway resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Identifier.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: SKU of the application gateway resource.
    :type sku: ~azure.mgmt.network.v2015_06_15.models.ApplicationGatewaySku
    :ivar operational_state: Operational state of the application gateway
     resource. Possible values are: 'Stopped', 'Started', 'Running', and
     'Stopping'. Possible values include: 'Stopped', 'Starting', 'Running',
     'Stopping'
    :vartype operational_state: str or
     ~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayOperationalState
    :param gateway_ip_configurations: Gets or sets subnets of application
     gateway resource
    :type gateway_ip_configurations:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayIPConfiguration]
    :param ssl_certificates: SSL certificates of the application gateway
     resource.
    :type ssl_certificates:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewaySslCertificate]
    :param frontend_ip_configurations: Frontend IP addresses of the
     application gateway resource.
    :type frontend_ip_configurations:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayFrontendIPConfiguration]
    :param frontend_ports: Frontend ports of the application gateway resource.
    :type frontend_ports:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayFrontendPort]
    :param probes: Probes of the application gateway resource.
    :type probes:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayProbe]
    :param backend_address_pools: Backend address pool of the application
     gateway resource.
    :type backend_address_pools:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayBackendAddressPool]
    :param backend_http_settings_collection: Backend http settings of the
     application gateway resource.
    :type backend_http_settings_collection:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayBackendHttpSettings]
    :param http_listeners: Http listeners of the application gateway resource.
    :type http_listeners:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayHttpListener]
    :param url_path_maps: URL path map of the application gateway resource.
    :type url_path_maps:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayUrlPathMap]
    :param request_routing_rules: Request routing rules of the application
     gateway resource.
    :type request_routing_rules:
     list[~azure.mgmt.network.v2015_06_15.models.ApplicationGatewayRequestRoutingRule]
    :param resource_guid: Resource GUID property of the application gateway
     resource.
    :type resource_guid: str
    :param provisioning_state: Provisioning state of the application gateway
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'operational_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'properties.sku', 'type': 'ApplicationGatewaySku'},
        'operational_state': {'key': 'properties.operationalState', 'type': 'str'},
        'gateway_ip_configurations': {'key': 'properties.gatewayIPConfigurations', 'type': '[ApplicationGatewayIPConfiguration]'},
        'ssl_certificates': {'key': 'properties.sslCertificates', 'type': '[ApplicationGatewaySslCertificate]'},
        'frontend_ip_configurations': {'key': 'properties.frontendIPConfigurations', 'type': '[ApplicationGatewayFrontendIPConfiguration]'},
        'frontend_ports': {'key': 'properties.frontendPorts', 'type': '[ApplicationGatewayFrontendPort]'},
        'probes': {'key': 'properties.probes', 'type': '[ApplicationGatewayProbe]'},
        'backend_address_pools': {'key': 'properties.backendAddressPools', 'type': '[ApplicationGatewayBackendAddressPool]'},
        'backend_http_settings_collection': {'key': 'properties.backendHttpSettingsCollection', 'type': '[ApplicationGatewayBackendHttpSettings]'},
        'http_listeners': {'key': 'properties.httpListeners', 'type': '[ApplicationGatewayHttpListener]'},
        'url_path_maps': {'key': 'properties.urlPathMaps', 'type': '[ApplicationGatewayUrlPathMap]'},
        'request_routing_rules': {'key': 'properties.requestRoutingRules', 'type': '[ApplicationGatewayRequestRoutingRule]'},
        'resource_guid': {'key': 'properties.resourceGuid', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, sku=None, gateway_ip_configurations=None, ssl_certificates=None, frontend_ip_configurations=None, frontend_ports=None, probes=None, backend_address_pools=None, backend_http_settings_collection=None, http_listeners=None, url_path_maps=None, request_routing_rules=None, resource_guid: str=None, provisioning_state: str=None, etag: str=None, **kwargs) -> None:
        super(ApplicationGateway, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.sku = sku
        self.operational_state = None
        self.gateway_ip_configurations = gateway_ip_configurations
        self.ssl_certificates = ssl_certificates
        self.frontend_ip_configurations = frontend_ip_configurations
        self.frontend_ports = frontend_ports
        self.probes = probes
        self.backend_address_pools = backend_address_pools
        self.backend_http_settings_collection = backend_http_settings_collection
        self.http_listeners = http_listeners
        self.url_path_maps = url_path_maps
        self.request_routing_rules = request_routing_rules
        self.resource_guid = resource_guid
        self.provisioning_state = provisioning_state
        self.etag = etag
