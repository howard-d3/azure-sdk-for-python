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


class UpgradePolicy(Model):
    """Describes an upgrade policy - automatic or manual.

    :param mode: Specifies the mode of an upgrade to virtual machines in the
     scale set.<br /><br /> Possible values are:<br /><br /> **Manual** - You
     control the application of updates to virtual machines in the scale set.
     You do this by using the manualUpgrade action.<br /><br /> **Automatic** -
     All virtual machines in the scale set are  automatically updated at the
     same time. Possible values include: 'Automatic', 'Manual'
    :type mode: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.UpgradeMode
    """

    _attribute_map = {
        'mode': {'key': 'mode', 'type': 'UpgradeMode'},
    }

    def __init__(self, **kwargs):
        super(UpgradePolicy, self).__init__(**kwargs)
        self.mode = kwargs.get('mode', None)
