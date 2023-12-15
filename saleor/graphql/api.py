import graphql
from django.urls import reverse
from django.utils.functional import SimpleLazyObject
from graphql import GraphQLScalarType

# @cf::ornament.geo
from saleor.graphql.ornament.geo.schema import GeoQueries

# @cf::ornament.vendors
from saleor.graphql.ornament.vendors.schema import VendorsQueries

# @cf::ornament.checkupcenter
from saleor.graphql.ornament.checkupcenter.schema import (
    CheckUpCenterMutations,
    CheckUpCenterQueries,
)

# @cf::ornament.search
from saleor.graphql.ornament.search.schema import SearchProductsQueries


from ..graphql.notifications.schema import ExternalNotificationMutations
from .account.schema import AccountMutations, AccountQueries
from .app.schema import AppMutations, AppQueries
from .attribute.schema import AttributeMutations, AttributeQueries
from .channel.schema import ChannelMutations, ChannelQueries
from .checkout.schema import CheckoutMutations, CheckoutQueries
from .core.enums import unit_enums
from .core.federation.schema import build_federated_schema
from .core.schema import CoreMutations, CoreQueries
from .csv.schema import CsvMutations, CsvQueries
from .discount.schema import DiscountMutations, DiscountQueries
from .giftcard.schema import GiftCardMutations, GiftCardQueries
from .invoice.schema import InvoiceMutations
from .menu.schema import MenuMutations, MenuQueries
from .meta.schema import MetaMutations
from .order.schema import OrderMutations, OrderQueries
from .page.schema import PageMutations, PageQueries
from .payment.schema import PaymentMutations, PaymentQueries
from .plugins.schema import PluginsMutations, PluginsQueries
from .product.schema import ProductMutations, ProductQueries
from .shipping.schema import ShippingMutations, ShippingQueries
from .shop.schema import ShopMutations, ShopQueries
from .tax.schema import TaxMutations, TaxQueries
from .translations.schema import TranslationQueries
from .warehouse.schema import (
    StockMutations,
    StockQueries,
    WarehouseMutations,
    WarehouseQueries,
)
from .webhook.schema import WebhookMutations, WebhookQueries
from .webhook.subscription_types import WEBHOOK_TYPES_MAP, Subscription

API_PATH = SimpleLazyObject(lambda: reverse("api"))


class Query(
    AccountQueries,
    AppQueries,
    AttributeQueries,
    ChannelQueries,
    CheckoutQueries,
    CoreQueries,
    CsvQueries,
    DiscountQueries,
    PluginsQueries,
    GiftCardQueries,
    MenuQueries,
    OrderQueries,
    PageQueries,
    PaymentQueries,
    ProductQueries,
    ShippingQueries,
    ShopQueries,
    StockQueries,
    TaxQueries,
    TranslationQueries,
    WarehouseQueries,
    WebhookQueries,
    # @cf::ornament.geo
    GeoQueries,
    # @cf::ornament.vendors
    VendorsQueries,
    # @cf::ornament.checkupcenter
    CheckUpCenterQueries,
    # @cf::ornament.search
    SearchProductsQueries,
):
    pass


class Mutation(
    AccountMutations,
    AppMutations,
    AttributeMutations,
    ChannelMutations,
    CheckoutMutations,
    CoreMutations,
    CsvMutations,
    DiscountMutations,
    ExternalNotificationMutations,
    PluginsMutations,
    GiftCardMutations,
    InvoiceMutations,
    MenuMutations,
    MetaMutations,
    OrderMutations,
    PageMutations,
    PaymentMutations,
    ProductMutations,
    ShippingMutations,
    ShopMutations,
    StockMutations,
    TaxMutations,
    WarehouseMutations,
    WebhookMutations,
    # @cf::ornament.checkupcenter
    CheckUpCenterMutations,
):
    pass


GraphQLDocDirective = graphql.GraphQLDirective(
    name="doc",
    description="Groups fields and operations into named groups.",
    args={
        "category": graphql.GraphQLArgument(
            type_=graphql.GraphQLNonNull(graphql.GraphQLString),
            description="Name of the grouping category",
        )
    },
    locations=[
        graphql.DirectiveLocation.ENUM,
        graphql.DirectiveLocation.FIELD,
        graphql.DirectiveLocation.FIELD_DEFINITION,
        graphql.DirectiveLocation.INPUT_OBJECT,
        graphql.DirectiveLocation.OBJECT,
    ],
)


def serialize_webhook_event(value):
    return value


GraphQLWebhookEventAsyncType = GraphQLScalarType(
    name="WebhookEventTypeAsyncEnum",
    description="",
    serialize=serialize_webhook_event,
)

GraphQLWebhookEventSyncType = GraphQLScalarType(
    name="WebhookEventTypeSyncEnum",
    description="",
    serialize=serialize_webhook_event,
)

GraphQLWebhookEventsInfoDirective = graphql.GraphQLDirective(
    name="webhookEventsInfo",
    description="Webhook events triggered by a specific location.",
    args={
        "asyncEvents": graphql.GraphQLArgument(
            type_=graphql.GraphQLNonNull(
                graphql.GraphQLList(
                    graphql.GraphQLNonNull(GraphQLWebhookEventAsyncType)
                )
            ),
            description=(
                "List of asynchronous webhook events triggered by a specific location."
            ),
        ),
        "syncEvents": graphql.GraphQLArgument(
            type_=graphql.GraphQLNonNull(
                graphql.GraphQLList(graphql.GraphQLNonNull(GraphQLWebhookEventSyncType))
            ),
            description=(
                "List of synchronous webhook events triggered by a specific location."
            ),
        ),
    },
    locations=[
        graphql.DirectiveLocation.FIELD,
        graphql.DirectiveLocation.FIELD_DEFINITION,
        graphql.DirectiveLocation.INPUT_OBJECT,
        graphql.DirectiveLocation.OBJECT,
    ],
)
schema = build_federated_schema(
    Query,
    mutation=Mutation,
    types=unit_enums + list(WEBHOOK_TYPES_MAP.values()),
    subscription=Subscription,
    directives=graphql.specified_directives
    + [GraphQLDocDirective, GraphQLWebhookEventsInfoDirective],
)
