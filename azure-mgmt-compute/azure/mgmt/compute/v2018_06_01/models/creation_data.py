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


class CreationData(Model):
    """Data used when creating a disk.

    All required parameters must be populated in order to send to Azure.

    :param create_option: Required. This enumerates the possible sources of a
     disk's creation. Possible values include: 'Empty', 'Attach', 'FromImage',
     'Import', 'Copy', 'Restore'
    :type create_option: str or
     ~azure.mgmt.compute.v2018_06_01.models.DiskCreateOption
    :param storage_account_id: If createOption is Import, the Azure Resource
     Manager identifier of the storage account containing the blob to import as
     a disk. Required only if the blob is in a different subscription
    :type storage_account_id: str
    :param image_reference: Disk source information.
    :type image_reference:
     ~azure.mgmt.compute.v2018_06_01.models.ImageDiskReference
    :param source_uri: If createOption is Import, this is the URI of a blob to
     be imported into a managed disk.
    :type source_uri: str
    :param source_resource_id: If createOption is Copy, this is the ARM id of
     the source snapshot or disk.
    :type source_resource_id: str
    """

    _validation = {
        'create_option': {'required': True},
    }

    _attribute_map = {
        'create_option': {'key': 'createOption', 'type': 'str'},
        'storage_account_id': {'key': 'storageAccountId', 'type': 'str'},
        'image_reference': {'key': 'imageReference', 'type': 'ImageDiskReference'},
        'source_uri': {'key': 'sourceUri', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CreationData, self).__init__(**kwargs)
        self.create_option = kwargs.get('create_option', None)
        self.storage_account_id = kwargs.get('storage_account_id', None)
        self.image_reference = kwargs.get('image_reference', None)
        self.source_uri = kwargs.get('source_uri', None)
        self.source_resource_id = kwargs.get('source_resource_id', None)
