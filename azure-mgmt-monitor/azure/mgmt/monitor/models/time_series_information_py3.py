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


class TimeSeriesInformation(Model):
    """The time series info needed for calculating the baseline.

    All required parameters must be populated in order to send to Azure.

    :param sensitivities: Required. the list of sensitivities for calculating
     the baseline.
    :type sensitivities: list[str]
    :param values: Required. The metric values to calculate the baseline.
    :type values: list[float]
    :param timestamps: the array of timestamps of the baselines.
    :type timestamps: list[datetime]
    """

    _validation = {
        'sensitivities': {'required': True},
        'values': {'required': True},
    }

    _attribute_map = {
        'sensitivities': {'key': 'sensitivities', 'type': '[str]'},
        'values': {'key': 'values', 'type': '[float]'},
        'timestamps': {'key': 'timestamps', 'type': '[iso-8601]'},
    }

    def __init__(self, *, sensitivities, values, timestamps=None, **kwargs) -> None:
        super(TimeSeriesInformation, self).__init__(**kwargs)
        self.sensitivities = sensitivities
        self.values = values
        self.timestamps = timestamps
