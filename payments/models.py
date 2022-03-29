
from django.db import models


# Create your models here.


class Payment(models.Model):
    amount = models.PositiveIntegerField(null=True)
    email = models.EmailField(null=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, null=True)
    phonenumber = models.CharField(max_length=255, null=True )
    order_key = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f"Payment: {self.amount}"


