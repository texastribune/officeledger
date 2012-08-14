from django.db.models import Sum
from django.template.response import TemplateResponse

from .models import Account, Entry
from django.db.models import Sum


def summary(request):
    accounts = Account.objects.exclude(user__username__in=['niran', 'agruen'])
    cash_balance = Entry.objects.filter(entry_type__in=['D',
        'W']).aggregate(Sum('amount'))['amount__sum']
    return TemplateResponse(request, 'summary.html', locals())
