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


class KEKDetails(Model):
    """KEK is encryption key for BEK.

    :param key_url: Key is KEK.
    :type key_url: str
    :param key_vault_id: Key Vault ID where this Key is stored.
    :type key_vault_id: str
    :param key_backup_data: KEK data.
    :type key_backup_data: str
    """

    _attribute_map = {
        'key_url': {'key': 'keyUrl', 'type': 'str'},
        'key_vault_id': {'key': 'keyVaultId', 'type': 'str'},
        'key_backup_data': {'key': 'keyBackupData', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(KEKDetails, self).__init__(**kwargs)
        self.key_url = kwargs.get('key_url', None)
        self.key_vault_id = kwargs.get('key_vault_id', None)
        self.key_backup_data = kwargs.get('key_backup_data', None)
