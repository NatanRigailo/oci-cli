# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias
from services.marketplace_private_offer.src.oci_cli_marketplace_private_offer.generated import marketplace_private_offer_service_cli


@click.command(cli_util.override('offer.offer_root_group.command_name', 'offer'), cls=CommandGroupWithAlias, help=cli_util.override('offer.offer_root_group.help', """Use the Marketplace Publisher API to manage the publishing of applications in Oracle Cloud Infrastructure Marketplace."""), short_help=cli_util.override('offer.offer_root_group.short_help', """MarketplacePrivateOffer API"""))
@cli_util.help_option_group
def offer_root_group():
    pass


@click.command(cli_util.override('offer.offer_group.command_name', 'offer'), cls=CommandGroupWithAlias, help="""Description of Offer.""")
@cli_util.help_option_group
def offer_group():
    pass


@click.command(cli_util.override('offer.offer_collection_group.command_name', 'offer-collection'), cls=CommandGroupWithAlias, help="""Results of a offers search. Contains boh OfferSummary items and other information, such as metadata.""")
@cli_util.help_option_group
def offer_collection_group():
    pass


marketplace_private_offer_service_cli.marketplace_private_offer_service_group.add_command(offer_root_group)
offer_root_group.add_command(offer_group)
offer_root_group.add_command(offer_collection_group)


@offer_group.command(name=cli_util.override('offer.create_offer.command_name', 'create'), help=u"""Creates a new Offer. \n[Command Reference](createOffer)""")
@cli_util.option('--display-name', required=True, help=u"""Offers Identifier""")
@cli_util.option('--seller-compartment-id', required=True, help=u"""Compartment Identifier of the seller""")
@cli_util.option('--buyer-compartment-id', help=u"""Compartment Identifier of the buyer""")
@cli_util.option('--description', help=u"""Description of the Offer""")
@cli_util.option('--internal-notes', help=u"""Internal notes of the Offer""")
@cli_util.option('--time-start-date', type=custom_types.CLI_DATETIME, help=u"""The time the Offer will become active after it has been accepted by the Buyer. An RFC3339 formatted datetime string""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--duration', help=u"""Duration the Offer will be active after its start date. An ISO8601 extended formatted string.""")
@cli_util.option('--time-accept-by', type=custom_types.CLI_DATETIME, help=u"""The time the Offer must be accepted by the Buyer before the Offer becomes invalid. An RFC3339 formatted datetime string""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--pricing', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--buyer-information', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--seller-information', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-bundles', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of Resource Bundles associated with an Offer.

This option is a JSON list with items of type ResourceBundle.  For documentation on ResourceBundle please see our API reference: https://docs.cloud.oracle.com/api/#/en/offer/20220901/datatypes/ResourceBundle.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of key value pairs specified by the seller

This option is a JSON list with items of type CustomField.  For documentation on CustomField please see our API reference: https://docs.cloud.oracle.com/api/#/en/offer/20220901/datatypes/CustomField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'pricing': {'module': 'marketplace_private_offer', 'class': 'Pricing'}, 'buyer-information': {'module': 'marketplace_private_offer', 'class': 'BuyerInformation'}, 'seller-information': {'module': 'marketplace_private_offer', 'class': 'SellerInformation'}, 'resource-bundles': {'module': 'marketplace_private_offer', 'class': 'list[ResourceBundle]'}, 'custom-fields': {'module': 'marketplace_private_offer', 'class': 'list[CustomField]'}, 'freeform-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'pricing': {'module': 'marketplace_private_offer', 'class': 'Pricing'}, 'buyer-information': {'module': 'marketplace_private_offer', 'class': 'BuyerInformation'}, 'seller-information': {'module': 'marketplace_private_offer', 'class': 'SellerInformation'}, 'resource-bundles': {'module': 'marketplace_private_offer', 'class': 'list[ResourceBundle]'}, 'custom-fields': {'module': 'marketplace_private_offer', 'class': 'list[CustomField]'}, 'freeform-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'marketplace_private_offer', 'class': 'Offer'})
@cli_util.wrap_exceptions
def create_offer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, display_name, seller_compartment_id, buyer_compartment_id, description, internal_notes, time_start_date, duration, time_accept_by, pricing, buyer_information, seller_information, resource_bundles, custom_fields, freeform_tags, defined_tags):

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}
    _details['displayName'] = display_name
    _details['sellerCompartmentId'] = seller_compartment_id

    if buyer_compartment_id is not None:
        _details['buyerCompartmentId'] = buyer_compartment_id

    if description is not None:
        _details['description'] = description

    if internal_notes is not None:
        _details['internalNotes'] = internal_notes

    if time_start_date is not None:
        _details['timeStartDate'] = time_start_date

    if duration is not None:
        _details['duration'] = duration

    if time_accept_by is not None:
        _details['timeAcceptBy'] = time_accept_by

    if pricing is not None:
        _details['pricing'] = cli_util.parse_json_parameter("pricing", pricing)

    if buyer_information is not None:
        _details['buyerInformation'] = cli_util.parse_json_parameter("buyer_information", buyer_information)

    if seller_information is not None:
        _details['sellerInformation'] = cli_util.parse_json_parameter("seller_information", seller_information)

    if resource_bundles is not None:
        _details['resourceBundles'] = cli_util.parse_json_parameter("resource_bundles", resource_bundles)

    if custom_fields is not None:
        _details['customFields'] = cli_util.parse_json_parameter("custom_fields", custom_fields)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('marketplace_private_offer', 'offer', ctx)
    result = client.create_offer(
        create_offer_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_offer') and callable(getattr(client, 'get_offer')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_offer(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@offer_group.command(name=cli_util.override('offer.delete_offer.command_name', 'delete'), help=u"""Deletes an Offer resource by identifier \n[Command Reference](deleteOffer)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_offer(ctx, from_json, wait_for_state, max_wait_seconds, wait_interval_seconds, offer_id, if_match):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_private_offer', 'offer', ctx)
    result = client.delete_offer(
        offer_id=offer_id,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_offer') and callable(getattr(client, 'get_offer')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                oci.wait_until(client, client.get_offer(offer_id), 'lifecycle_state', wait_for_state, succeed_on_not_found=True, **wait_period_kwargs)
            except oci.exceptions.ServiceError as e:
                # We make an initial service call so we can pass the result to oci.wait_until(), however if we are waiting on the
                # outcome of a delete operation it is possible that the resource is already gone and so the initial service call
                # will result in an exception that reflects a HTTP 404. In this case, we can exit with success (rather than raising
                # the exception) since this would have been the behaviour in the waiter anyway (as for delete we provide the argument
                # succeed_on_not_found=True to the waiter).
                #
                # Any non-404 should still result in the exception being thrown.
                if e.status == 404:
                    pass
                else:
                    raise
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Please retrieve the resource to find its current state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)


@offer_group.command(name=cli_util.override('offer.get_offer.command_name', 'get'), help=u"""Gets an Offer by identifier \n[Command Reference](getOffer)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace_private_offer', 'class': 'Offer'})
@cli_util.wrap_exceptions
def get_offer(ctx, from_json, offer_id):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_private_offer', 'offer', ctx)
    result = client.get_offer(
        offer_id=offer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@offer_group.command(name=cli_util.override('offer.get_offer_internal_detail.command_name', 'get-offer-internal-detail'), help=u"""Gets an Offer internal details by identifier \n[Command Reference](getOfferInternalDetail)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace_private_offer', 'class': 'OfferInternalDetail'})
@cli_util.wrap_exceptions
def get_offer_internal_detail(ctx, from_json, offer_id):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_private_offer', 'offer', ctx)
    result = client.get_offer_internal_detail(
        offer_id=offer_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@offer_collection_group.command(name=cli_util.override('offer.list_offers.command_name', 'list-offers'), help=u"""Returns a list of Offers. Requires either the BuyerCompartmentId or the SellerCompartmentId params. If neither or both are provided, then the API will return a 400. \n[Command Reference](listOffers)""")
@cli_util.option('--buyer-compartment-id', help=u"""The ID of the buyer compartment this offer is associated with.""")
@cli_util.option('--seller-compartment-id', help=u"""The ID of the seller compartment this offer is associated with.""")
@cli_util.option('--lifecycle-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), help=u"""A filter to return only resources their lifecycleState matches the given lifecycleState.""")
@cli_util.option('--display-name', help=u"""A filter to return only resources that match the entire display name given.""")
@cli_util.option('--id', help=u"""unique Offer identifier""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return.""")
@cli_util.option('--page', help=u"""A token representing the position at which to start retrieving results. This must come from the `opc-next-page` header field of a previous response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, either 'ASC' or 'DESC'.""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["timeCreated", "displayName"]), help=u"""The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is ascending.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'marketplace_private_offer', 'class': 'OfferCollection'})
@cli_util.wrap_exceptions
def list_offers(ctx, from_json, all_pages, page_size, buyer_compartment_id, seller_compartment_id, lifecycle_state, display_name, id, limit, page, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    kwargs = {}
    if buyer_compartment_id is not None:
        kwargs['buyer_compartment_id'] = buyer_compartment_id
    if seller_compartment_id is not None:
        kwargs['seller_compartment_id'] = seller_compartment_id
    if lifecycle_state is not None:
        kwargs['lifecycle_state'] = lifecycle_state
    if display_name is not None:
        kwargs['display_name'] = display_name
    if id is not None:
        kwargs['id'] = id
    if limit is not None:
        kwargs['limit'] = limit
    if page is not None:
        kwargs['page'] = page
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('marketplace_private_offer', 'offer', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_offers,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_offers,
            limit,
            page_size,
            **kwargs
        )
    else:
        result = client.list_offers(
            **kwargs
        )
    cli_util.render_response(result, ctx)


@offer_group.command(name=cli_util.override('offer.update_offer.command_name', 'update'), help=u"""Updates the Offer \n[Command Reference](updateOffer)""")
@cli_util.option('--offer-id', required=True, help=u"""unique Offer identifier""")
@cli_util.option('--display-name', help=u"""Offers Identifier""")
@cli_util.option('--buyer-compartment-id', help=u"""OCID of the buyer's tenancy (root compartment).""")
@cli_util.option('--description', help=u"""Description of the Offer""")
@cli_util.option('--internal-notes', help=u"""Internal notes of the Offer""")
@cli_util.option('--time-start-date', type=custom_types.CLI_DATETIME, help=u"""The time the Offer will become active after it has been accepted by the Buyer. An RFC3339 formatted datetime string""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--duration', help=u"""Duration the Offer will be active after its start date. An ISO8601 extended formatted string.""")
@cli_util.option('--time-accept-by', type=custom_types.CLI_DATETIME, help=u"""The time the Offer must be accepted by the Buyer before the Offer becomes invalid. An RFC3339 formatted datetime string""" + custom_types.CLI_DATETIME.VALID_DATETIME_CLI_HELP_MESSAGE)
@cli_util.option('--pricing', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--buyer-information', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--seller-information', type=custom_types.CLI_COMPLEX_TYPE, help=u"""""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--resource-bundles', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of Resource Bundles associated with an Offer.

This option is a JSON list with items of type ResourceBundle.  For documentation on ResourceBundle please see our API reference: https://docs.cloud.oracle.com/api/#/en/offer/20220901/datatypes/ResourceBundle.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--custom-fields', type=custom_types.CLI_COMPLEX_TYPE, help=u"""A list of key value pairs specified by the seller

This option is a JSON list with items of type CustomField.  For documentation on CustomField please see our API reference: https://docs.cloud.oracle.com/api/#/en/offer/20220901/datatypes/CustomField.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--freeform-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only. Example: `{\"bar-key\": \"value\"}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--defined-tags', type=custom_types.CLI_COMPLEX_TYPE, help=u"""Defined tags for this resource. Each key is predefined and scoped to a namespace. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted only if the etag you provide matches the resource's current etag value.""")
@cli_util.option('--force', help="""Perform update without prompting for confirmation.""", is_flag=True)
@cli_util.option('--wait-for-state', type=custom_types.CliCaseInsensitiveChoice(["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]), multiple=True, help="""This operation creates, modifies or deletes a resource that has a defined lifecycle state. Specify this option to perform the action and then wait until the resource reaches a given lifecycle state. Multiple states can be specified, returning on the first state. For example, --wait-for-state SUCCEEDED --wait-for-state FAILED would return on whichever lifecycle state is reached first. If timeout is reached, a return code of 2 is returned. For any other error, a return code of 1 is returned.""")
@cli_util.option('--max-wait-seconds', type=click.INT, help="""The maximum time to wait for the resource to reach the lifecycle state defined by --wait-for-state. Defaults to 1200 seconds.""")
@cli_util.option('--wait-interval-seconds', type=click.INT, help="""Check every --wait-interval-seconds to see whether the resource has reached the lifecycle state defined by --wait-for-state. Defaults to 30 seconds.""")
@json_skeleton_utils.get_cli_json_input_option({'pricing': {'module': 'marketplace_private_offer', 'class': 'Pricing'}, 'buyer-information': {'module': 'marketplace_private_offer', 'class': 'BuyerInformation'}, 'seller-information': {'module': 'marketplace_private_offer', 'class': 'SellerInformation'}, 'resource-bundles': {'module': 'marketplace_private_offer', 'class': 'list[ResourceBundle]'}, 'custom-fields': {'module': 'marketplace_private_offer', 'class': 'list[CustomField]'}, 'freeform-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, dict(str, object))'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'pricing': {'module': 'marketplace_private_offer', 'class': 'Pricing'}, 'buyer-information': {'module': 'marketplace_private_offer', 'class': 'BuyerInformation'}, 'seller-information': {'module': 'marketplace_private_offer', 'class': 'SellerInformation'}, 'resource-bundles': {'module': 'marketplace_private_offer', 'class': 'list[ResourceBundle]'}, 'custom-fields': {'module': 'marketplace_private_offer', 'class': 'list[CustomField]'}, 'freeform-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, string)'}, 'defined-tags': {'module': 'marketplace_private_offer', 'class': 'dict(str, dict(str, object))'}}, output_type={'module': 'marketplace_private_offer', 'class': 'Offer'})
@cli_util.wrap_exceptions
def update_offer(ctx, from_json, force, wait_for_state, max_wait_seconds, wait_interval_seconds, offer_id, display_name, buyer_compartment_id, description, internal_notes, time_start_date, duration, time_accept_by, pricing, buyer_information, seller_information, resource_bundles, custom_fields, freeform_tags, defined_tags, if_match):

    if isinstance(offer_id, six.string_types) and len(offer_id.strip()) == 0:
        raise click.UsageError('Parameter --offer-id cannot be whitespace or empty string')
    if not force:
        if pricing or buyer_information or seller_information or resource_bundles or custom_fields or freeform_tags or defined_tags:
            if not click.confirm("WARNING: Updates to pricing and buyer-information and seller-information and resource-bundles and custom-fields and freeform-tags and defined-tags will replace any existing values. Are you sure you want to continue?"):
                ctx.abort()

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if display_name is not None:
        _details['displayName'] = display_name

    if buyer_compartment_id is not None:
        _details['buyerCompartmentId'] = buyer_compartment_id

    if description is not None:
        _details['description'] = description

    if internal_notes is not None:
        _details['internalNotes'] = internal_notes

    if time_start_date is not None:
        _details['timeStartDate'] = time_start_date

    if duration is not None:
        _details['duration'] = duration

    if time_accept_by is not None:
        _details['timeAcceptBy'] = time_accept_by

    if pricing is not None:
        _details['pricing'] = cli_util.parse_json_parameter("pricing", pricing)

    if buyer_information is not None:
        _details['buyerInformation'] = cli_util.parse_json_parameter("buyer_information", buyer_information)

    if seller_information is not None:
        _details['sellerInformation'] = cli_util.parse_json_parameter("seller_information", seller_information)

    if resource_bundles is not None:
        _details['resourceBundles'] = cli_util.parse_json_parameter("resource_bundles", resource_bundles)

    if custom_fields is not None:
        _details['customFields'] = cli_util.parse_json_parameter("custom_fields", custom_fields)

    if freeform_tags is not None:
        _details['freeformTags'] = cli_util.parse_json_parameter("freeform_tags", freeform_tags)

    if defined_tags is not None:
        _details['definedTags'] = cli_util.parse_json_parameter("defined_tags", defined_tags)

    client = cli_util.build_client('marketplace_private_offer', 'offer', ctx)
    result = client.update_offer(
        offer_id=offer_id,
        update_offer_details=_details,
        **kwargs
    )
    if wait_for_state:

        if hasattr(client, 'get_offer') and callable(getattr(client, 'get_offer')):
            try:
                wait_period_kwargs = {}
                if max_wait_seconds is not None:
                    wait_period_kwargs['max_wait_seconds'] = max_wait_seconds
                if wait_interval_seconds is not None:
                    wait_period_kwargs['max_interval_seconds'] = wait_interval_seconds

                click.echo('Action completed. Waiting until the resource has entered state: {}'.format(wait_for_state), file=sys.stderr)
                result = oci.wait_until(client, client.get_offer(result.data.id), 'lifecycle_state', wait_for_state, **wait_period_kwargs)
            except oci.exceptions.MaximumWaitTimeExceeded as e:
                # If we fail, we should show an error, but we should still provide the information to the customer
                click.echo('Failed to wait until the resource entered the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                sys.exit(2)
            except Exception:
                click.echo('Encountered error while waiting for resource to enter the specified state. Outputting last known resource state', file=sys.stderr)
                cli_util.render_response(result, ctx)
                raise
        else:
            click.echo('Unable to wait for the resource to enter the specified state', file=sys.stderr)
    cli_util.render_response(result, ctx)