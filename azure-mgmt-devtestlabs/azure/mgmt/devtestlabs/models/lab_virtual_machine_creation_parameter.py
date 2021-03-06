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


class LabVirtualMachineCreationParameter(Model):
    """Properties for creating a virtual machine.

    :param bulk_creation_parameters: The number of virtual machine instances
     to create.
    :type bulk_creation_parameters:
     ~azure.mgmt.devtestlabs.models.BulkCreationParameters
    :param notes: The notes of the virtual machine.
    :type notes: str
    :param owner_object_id: The object identifier of the owner of the virtual
     machine.
    :type owner_object_id: str
    :param owner_user_principal_name: The user principal name of the virtual
     machine owner.
    :type owner_user_principal_name: str
    :param created_by_user_id: The object identifier of the creator of the
     virtual machine.
    :type created_by_user_id: str
    :param created_by_user: The email address of creator of the virtual
     machine.
    :type created_by_user: str
    :param created_date: The creation date of the virtual machine.
    :type created_date: datetime
    :param compute_id: The resource identifier (Microsoft.Compute) of the
     virtual machine.
    :type compute_id: str
    :param custom_image_id: The custom image identifier of the virtual
     machine.
    :type custom_image_id: str
    :param os_type: The OS type of the virtual machine.
    :type os_type: str
    :param size: The size of the virtual machine.
    :type size: str
    :param user_name: The user name of the virtual machine.
    :type user_name: str
    :param password: The password of the virtual machine administrator.
    :type password: str
    :param ssh_key: The SSH key of the virtual machine administrator.
    :type ssh_key: str
    :param is_authentication_with_ssh_key: Indicates whether this virtual
     machine uses an SSH key for authentication.
    :type is_authentication_with_ssh_key: bool
    :param fqdn: The fully-qualified domain name of the virtual machine.
    :type fqdn: str
    :param lab_subnet_name: The lab subnet name of the virtual machine.
    :type lab_subnet_name: str
    :param lab_virtual_network_id: The lab virtual network identifier of the
     virtual machine.
    :type lab_virtual_network_id: str
    :param disallow_public_ip_address: Indicates whether the virtual machine
     is to be created without a public IP address.
    :type disallow_public_ip_address: bool
    :param artifacts: The artifacts to be installed on the virtual machine.
    :type artifacts:
     list[~azure.mgmt.devtestlabs.models.ArtifactInstallProperties]
    :param artifact_deployment_status: The artifact deployment status for the
     virtual machine.
    :type artifact_deployment_status:
     ~azure.mgmt.devtestlabs.models.ArtifactDeploymentStatusProperties
    :param gallery_image_reference: The Microsoft Azure Marketplace image
     reference of the virtual machine.
    :type gallery_image_reference:
     ~azure.mgmt.devtestlabs.models.GalleryImageReference
    :param plan_id: The id of the plan associated with the virtual machine
     image
    :type plan_id: str
    :param network_interface: The network interface properties.
    :type network_interface:
     ~azure.mgmt.devtestlabs.models.NetworkInterfaceProperties
    :param expiration_date: The expiration date for VM.
    :type expiration_date: datetime
    :param allow_claim: Indicates whether another user can take ownership of
     the virtual machine
    :type allow_claim: bool
    :param storage_type: Storage type to use for virtual machine (i.e.
     Standard, Premium).
    :type storage_type: str
    :param virtual_machine_creation_source: Tells source of creation of lab
     virtual machine. Output property only. Possible values include:
     'FromCustomImage', 'FromGalleryImage'
    :type virtual_machine_creation_source: str or
     ~azure.mgmt.devtestlabs.models.VirtualMachineCreationSource
    :param environment_id: The resource ID of the environment that contains
     this virtual machine, if any.
    :type environment_id: str
    :param data_disk_parameters: New or existing data disks to attach to the
     virtual machine after creation
    :type data_disk_parameters:
     list[~azure.mgmt.devtestlabs.models.DataDiskProperties]
    :param schedule_parameters: Virtual Machine schedules to be created
    :type schedule_parameters:
     list[~azure.mgmt.devtestlabs.models.ScheduleCreationParameter]
    :param last_known_power_state: Last known compute power state captured in
     DTL
    :type last_known_power_state: str
    :param name: The name of the virtual machine or environment
    :type name: str
    :param location: The location of the new virtual machine or environment
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'bulk_creation_parameters': {'key': 'properties.bulkCreationParameters', 'type': 'BulkCreationParameters'},
        'notes': {'key': 'properties.notes', 'type': 'str'},
        'owner_object_id': {'key': 'properties.ownerObjectId', 'type': 'str'},
        'owner_user_principal_name': {'key': 'properties.ownerUserPrincipalName', 'type': 'str'},
        'created_by_user_id': {'key': 'properties.createdByUserId', 'type': 'str'},
        'created_by_user': {'key': 'properties.createdByUser', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'compute_id': {'key': 'properties.computeId', 'type': 'str'},
        'custom_image_id': {'key': 'properties.customImageId', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'size': {'key': 'properties.size', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'password': {'key': 'properties.password', 'type': 'str'},
        'ssh_key': {'key': 'properties.sshKey', 'type': 'str'},
        'is_authentication_with_ssh_key': {'key': 'properties.isAuthenticationWithSshKey', 'type': 'bool'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'lab_subnet_name': {'key': 'properties.labSubnetName', 'type': 'str'},
        'lab_virtual_network_id': {'key': 'properties.labVirtualNetworkId', 'type': 'str'},
        'disallow_public_ip_address': {'key': 'properties.disallowPublicIpAddress', 'type': 'bool'},
        'artifacts': {'key': 'properties.artifacts', 'type': '[ArtifactInstallProperties]'},
        'artifact_deployment_status': {'key': 'properties.artifactDeploymentStatus', 'type': 'ArtifactDeploymentStatusProperties'},
        'gallery_image_reference': {'key': 'properties.galleryImageReference', 'type': 'GalleryImageReference'},
        'plan_id': {'key': 'properties.planId', 'type': 'str'},
        'network_interface': {'key': 'properties.networkInterface', 'type': 'NetworkInterfaceProperties'},
        'expiration_date': {'key': 'properties.expirationDate', 'type': 'iso-8601'},
        'allow_claim': {'key': 'properties.allowClaim', 'type': 'bool'},
        'storage_type': {'key': 'properties.storageType', 'type': 'str'},
        'virtual_machine_creation_source': {'key': 'properties.virtualMachineCreationSource', 'type': 'str'},
        'environment_id': {'key': 'properties.environmentId', 'type': 'str'},
        'data_disk_parameters': {'key': 'properties.dataDiskParameters', 'type': '[DataDiskProperties]'},
        'schedule_parameters': {'key': 'properties.scheduleParameters', 'type': '[ScheduleCreationParameter]'},
        'last_known_power_state': {'key': 'properties.lastKnownPowerState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(LabVirtualMachineCreationParameter, self).__init__(**kwargs)
        self.bulk_creation_parameters = kwargs.get('bulk_creation_parameters', None)
        self.notes = kwargs.get('notes', None)
        self.owner_object_id = kwargs.get('owner_object_id', None)
        self.owner_user_principal_name = kwargs.get('owner_user_principal_name', None)
        self.created_by_user_id = kwargs.get('created_by_user_id', None)
        self.created_by_user = kwargs.get('created_by_user', None)
        self.created_date = kwargs.get('created_date', None)
        self.compute_id = kwargs.get('compute_id', None)
        self.custom_image_id = kwargs.get('custom_image_id', None)
        self.os_type = kwargs.get('os_type', None)
        self.size = kwargs.get('size', None)
        self.user_name = kwargs.get('user_name', None)
        self.password = kwargs.get('password', None)
        self.ssh_key = kwargs.get('ssh_key', None)
        self.is_authentication_with_ssh_key = kwargs.get('is_authentication_with_ssh_key', None)
        self.fqdn = kwargs.get('fqdn', None)
        self.lab_subnet_name = kwargs.get('lab_subnet_name', None)
        self.lab_virtual_network_id = kwargs.get('lab_virtual_network_id', None)
        self.disallow_public_ip_address = kwargs.get('disallow_public_ip_address', None)
        self.artifacts = kwargs.get('artifacts', None)
        self.artifact_deployment_status = kwargs.get('artifact_deployment_status', None)
        self.gallery_image_reference = kwargs.get('gallery_image_reference', None)
        self.plan_id = kwargs.get('plan_id', None)
        self.network_interface = kwargs.get('network_interface', None)
        self.expiration_date = kwargs.get('expiration_date', None)
        self.allow_claim = kwargs.get('allow_claim', None)
        self.storage_type = kwargs.get('storage_type', None)
        self.virtual_machine_creation_source = kwargs.get('virtual_machine_creation_source', None)
        self.environment_id = kwargs.get('environment_id', None)
        self.data_disk_parameters = kwargs.get('data_disk_parameters', None)
        self.schedule_parameters = kwargs.get('schedule_parameters', None)
        self.last_known_power_state = kwargs.get('last_known_power_state', None)
        self.name = kwargs.get('name', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
