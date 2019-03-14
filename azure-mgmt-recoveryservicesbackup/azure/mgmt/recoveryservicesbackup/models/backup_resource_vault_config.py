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


class BackupResourceVaultConfig(Model):
    """Backup resource vault config details.

    :param storage_model_type: Storage type. Possible values include:
     'Invalid', 'GeoRedundant', 'LocallyRedundant'
    :type storage_model_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.StorageType
    :param storage_type: Storage type. Possible values include: 'Invalid',
     'GeoRedundant', 'LocallyRedundant'
    :type storage_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.StorageType
    :param storage_type_state: Locked or Unlocked. Once a machine is
     registered against a resource, the storageTypeState is always Locked.
     Possible values include: 'Invalid', 'Locked', 'Unlocked'
    :type storage_type_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.StorageTypeState
    :param enhanced_security_state: Enabled or Disabled. Possible values
     include: 'Invalid', 'Enabled', 'Disabled'
    :type enhanced_security_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.EnhancedSecurityState
    """

    _attribute_map = {
        'storage_model_type': {'key': 'storageModelType', 'type': 'str'},
        'storage_type': {'key': 'storageType', 'type': 'str'},
        'storage_type_state': {'key': 'storageTypeState', 'type': 'str'},
        'enhanced_security_state': {'key': 'enhancedSecurityState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BackupResourceVaultConfig, self).__init__(**kwargs)
        self.storage_model_type = kwargs.get('storage_model_type', None)
        self.storage_type = kwargs.get('storage_type', None)
        self.storage_type_state = kwargs.get('storage_type_state', None)
        self.enhanced_security_state = kwargs.get('enhanced_security_state', None)
