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


class DataDisk(Model):
    """Settings which will be used by the data disks associated to compute nodes
    in the pool.

    All required parameters must be populated in order to send to Azure.

    :param lun: Required. The logical unit number. The lun is used to uniquely
     identify each data disk. If attaching multiple disks, each should have a
     distinct lun.
    :type lun: int
    :param caching: The type of caching to be enabled for the data disks. The
     default value for caching is readwrite. For information about the caching
     options see:
     https://blogs.msdn.microsoft.com/windowsazurestorage/2012/06/27/exploring-windows-azure-drives-disks-and-images/.
     Possible values include: 'none', 'readOnly', 'readWrite'
    :type caching: str or ~azure.batch.models.CachingType
    :param disk_size_gb: Required. The initial disk size in gigabytes.
    :type disk_size_gb: int
    :param storage_account_type: The storage account type to be used for the
     data disk. If omitted, the default is "standard_lrs". Possible values
     include: 'StandardLRS', 'PremiumLRS'
    :type storage_account_type: str or ~azure.batch.models.StorageAccountType
    """

    _validation = {
        'lun': {'required': True},
        'disk_size_gb': {'required': True},
    }

    _attribute_map = {
        'lun': {'key': 'lun', 'type': 'int'},
        'caching': {'key': 'caching', 'type': 'CachingType'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'storage_account_type': {'key': 'storageAccountType', 'type': 'StorageAccountType'},
    }

    def __init__(self, *, lun: int, disk_size_gb: int, caching=None, storage_account_type=None, **kwargs) -> None:
        super(DataDisk, self).__init__(**kwargs)
        self.lun = lun
        self.caching = caching
        self.disk_size_gb = disk_size_gb
        self.storage_account_type = storage_account_type