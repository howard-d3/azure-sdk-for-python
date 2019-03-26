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


class ProductDetails(Model):
    """Details of the product to be transferred.

    :param product_type: Type of the prouct to be transferred. Possible values
     include: 'AzureSubscription', 'AzureReservation'
    :type product_type: str or ~azure.mgmt.billing.models.ProductType
    :param product_id: Id of product to be transferred.
    :type product_id: str
    """

    _attribute_map = {
        'product_type': {'key': 'productType', 'type': 'str'},
        'product_id': {'key': 'productId', 'type': 'str'},
    }

    def __init__(self, *, product_type=None, product_id: str=None, **kwargs) -> None:
        super(ProductDetails, self).__init__(**kwargs)
        self.product_type = product_type
        self.product_id = product_id
