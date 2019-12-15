import django_filters

from sales.models import Profit


class ProfitFilter(django_filters.FilterSet):

    class Meta:
        model = Profit
        fields = {
            'id': ['exact'],
            'product': ['exact'],
            'amount': ['exact', 'lt', 'gt'],
            'sales_date': ['exact', 'date', 'date__lt', 'date__gt']
        }
