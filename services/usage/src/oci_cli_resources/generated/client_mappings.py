# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190111

import oci
from oci_cli.cli_clients import CLIENT_MAP
from oci_cli.cli_clients import MODULE_TO_TYPE_MAPPINGS
from oci.usage import ResourcesClient

MODULE_TO_TYPE_MAPPINGS["usage"] = oci.usage.models.usage_type_mapping
if CLIENT_MAP.get("usage") is None:
    CLIENT_MAP["usage"] = {}
CLIENT_MAP["usage"]["resources"] = ResourcesClient