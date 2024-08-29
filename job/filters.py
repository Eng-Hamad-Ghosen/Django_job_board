from .models import Job
import django_filters

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=Job
        fields='__all__'
        exclude=['like','owner','vacancy','salary','experience','image','slug','published_at']