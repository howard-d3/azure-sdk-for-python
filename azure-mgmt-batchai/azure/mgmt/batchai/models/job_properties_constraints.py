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


class JobPropertiesConstraints(Model):
    """Constraints associated with the Job.

    :param max_wall_clock_time: Max time the job can run. Default Value = 1
     week. Default value: "7.00:00:00" .
    :type max_wall_clock_time: timedelta
    """

    _attribute_map = {
        'max_wall_clock_time': {'key': 'maxWallClockTime', 'type': 'duration'},
    }

    def __init__(self, **kwargs):
        super(JobPropertiesConstraints, self).__init__(**kwargs)
        self.max_wall_clock_time = kwargs.get('max_wall_clock_time', "7.00:00:00")
