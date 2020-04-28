# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import unittest
from tests import util


class TestAnalyticsCliExtended(unittest.TestCase):
    def setUp(self):
        pass

    def test_analytics_instance_create(self):

        inst_name = 'testinstance1'
        description = 'Test Analytics Instance 1'
        capacity_type = 'OLPU_COUNT'
        capacity_value = '1'
        compartment_id = 'ocid1.tenancy.oc1..aaaaaaaaavy5ubqrzwcupgsapwvzeri4u6pzq4fqecryumqoqvvi2i7xaj7a'
        feature_set = 'ENTERPRISE_ANALYTICS'
        license_type = 'LICENSE_INCLUDED'
        email = 'olivier.louchart-fletcher@oracle.com'
        token_file = 'services/analytics/tests/cassettes/idcs_access_token.txt'

        # Check that --capacity-value is defined and required.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity-type', capacity_type,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token-file', token_file
        ])
        assert 'Missing option(s) --capacity-value.' in result.output

        # Check that --capacity-type is defined and required.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity-value', capacity_value,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token-file', token_file
        ])
        assert 'Missing option(s) --capacity-type.' in result.output

        # Check that --capacity is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity', '{"capacityType": "OLPU_COUNT", "capacityValue": 1}',
            '--capacity-type', capacity_type,
            '--capacity-value', capacity_value,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token-file', token_file
        ])
        assert 'Error: no such option: --capacity ' in result.output

        # Check that --idcs-access-token is not expected on the CLI and triggers an error.
        result = util.invoke_command([
            'analytics', 'analytics-instance', 'create',
            '--name', inst_name,
            '--description', description,
            '--capacity-type', capacity_type,
            '--capacity-value', capacity_value,
            '--compartment-id', compartment_id,
            '--feature-set', feature_set,
            '--license-type', license_type,
            '--email-notification', email,
            '--idcs-access-token', 'eyJraWQiOiJhc3dfb2'
            '--idcs-access-token-file', token_file
        ])
        assert 'Error: no such option: --idcs-access-token ' in result.output
