import django_filters
from django_filters import filters
from .models import Main

class WordFilter(django_filters.FilterSet):
    normalized_freq = filters.RangeFilter(label = "Min. normalized frequency:")
    normalized_range = filters.RangeFilter(label = "Min. normalized range:")
    word = filters.CharFilter(lookup_expr="icontains", label="Word:")

class NgramFilter(django_filters.FilterSet):
    normalized_freq = filters.RangeFilter(label = "Min. normalized frequency:")
    normalized_range = filters.RangeFilter(label = "Min. normalized range:")
    text = filters.CharFilter(lookup_expr="icontains", label="Word/Words:")


class ConcordanceFilter(django_filters.FilterSet):
    word = django_filters.CharFilter(lookup_expr="icontains", label="Word/Words:")