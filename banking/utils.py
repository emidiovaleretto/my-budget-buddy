from django.db.models import Sum

def calculate_total(queryset, field_name):
    return queryset.aggregate(total=Sum(field_name))['total'] or 0
