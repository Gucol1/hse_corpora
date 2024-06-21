import django_filters
from django_filters import filters
from .models import Main

class WordFilter(django_filters.FilterSet):

    normalized_freq = filters.RangeFilter(label = "Min. normalized frequency:")
    normalized_range = filters.RangeFilter(label = "Min. normalized range:")
    word = filters.CharFilter(lookup_expr="icontains", label="Word:")
    #
    # class Meta:
    #     model = Main
    #     fields = [
    #         # 'genre',
    #         # 'restrictions',
    #         # 'date'
    #     ]