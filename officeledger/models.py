from django.db import models
from django.contrib.admin.models import User
from datetime import datetime

class Account(models.Model):
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u'%s' % (self.user,)

    def balance(self, time=None):
        if time is None:
            time = datetime.now()
        return self.entries.filter(datetime__lte=time)\
                .aggregate(models.Sum('amount'))['amount__sum']


ENTRY_CHOICES = {
        'D': 'Deposit (Cash)',
        'F': 'Deposit (Food)',
        'W': 'Withdrawal (Cash)',
        'Z': 'Leveling',
    }


class Entry(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, related_name='entries')
    datetime = models.DateTimeField()
    entry_type = models.CharField(max_length=1, choices=ENTRY_CHOICES.items())

    def __unicode__(self):
        return u'%s: $%.2f - %s - %s' % (self.account, self.amount,
                ENTRY_CHOICES[self.entry_type], self.datetime)

    class Meta:
        ordering = ['datetime']
