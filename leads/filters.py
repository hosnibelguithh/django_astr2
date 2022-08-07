
from dataclasses import field
import django_filters

from accounts.models import User 
from .models import *

class LeadFilter(django_filters.FilterSet):
    Nom = django_filters.CharFilter(
        field_name="Nom",
        lookup_expr='icontains'
    )
    Prénom = django_filters.CharFilter(
        field_name="Prénom",
        lookup_expr='icontains'
    )
    Agent = django_filters.ModelChoiceFilter(
        field_name = 'Agent', 
        queryset = User.objects.filter(is_agent = True)
    )
    class Meta:
        model = Prospect
        fields = {
            'Nom',
            'Prénom',
            'Agent',
            'status',
        }