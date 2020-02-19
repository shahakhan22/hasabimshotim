import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter('title','icontains',label='שם היין')


    CHOICES = (
        ('ascending', 'מהנמוך לגבוה'),
        ('descending', 'מהגבוה לנמוך'),

    )
    ordering_price = django_filters.ChoiceFilter(label="סדר לפי", choices=CHOICES, method='order_by_price')

    class Meta:
        model = Product
        fields = {
            # 'title': ['icontains'],
            # 'price': ['icontains'],
        }

    def order_by_price(self, queryset, name, value):
        expression = 'price' if value == 'ascending' else '-price'
        return queryset.order_by(expression)
