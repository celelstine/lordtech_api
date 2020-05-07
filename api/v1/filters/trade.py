import django_filters

from sales.models import Trade


class TradeFilter(django_filters.FilterSet):

    class Meta:
        model = Trade
        fields = {
            'id': ['exact'],
            'sales_rep': ['exact'],
            'card': ['exact'],
            'is_closed': ['exact'],
            'order_id': ['exact'],
            'trade_group': ['exact'],
            'amount': ['exact', 'lt', 'gt'],
            'sales_date': ['exact', 'lt', 'gt'],
            'create_date': ['exact', 'date', 'date__lte', 'date__gte']
        }
