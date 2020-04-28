# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from services.work_requests.src.oci_cli_work_request.generated import workrequest_cli
from oci_cli import cli_util

cli_util.rename_command(workrequest_cli, workrequest_cli.work_request_log_entry_group, workrequest_cli.list_work_request_logs, "list")
