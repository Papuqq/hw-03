from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post, Category


class PostFilters(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Category',
        empty_label="Любая",
    )

    class Meta:
        model = Post

        fields = {
            'header': ['icontains'],
            'essence': ['exact'],
        }

    added_after = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        label='Date later than',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
