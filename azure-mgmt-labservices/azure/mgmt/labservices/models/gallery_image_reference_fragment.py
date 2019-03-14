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


class GalleryImageReferenceFragment(Model):
    """The reference information for an Azure Marketplace image.

    :param offer: The offer of the gallery image.
    :type offer: str
    :param publisher: The publisher of the gallery image.
    :type publisher: str
    :param sku: The SKU of the gallery image.
    :type sku: str
    :param os_type: The OS type of the gallery image.
    :type os_type: str
    :param version: The version of the gallery image.
    :type version: str
    """

    _attribute_map = {
        'offer': {'key': 'offer', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'os_type': {'key': 'osType', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GalleryImageReferenceFragment, self).__init__(**kwargs)
        self.offer = kwargs.get('offer', None)
        self.publisher = kwargs.get('publisher', None)
        self.sku = kwargs.get('sku', None)
        self.os_type = kwargs.get('os_type', None)
        self.version = kwargs.get('version', None)
