from django.conf import settings
from django.db import models


# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField(null=True)
    email= models.CharField(max_length=255)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    order_key = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        ordering = ('-date_created',)



