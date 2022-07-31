from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PRODUCT_CHOICES = (
    ('TV','tv'),
    ('IPAD','Ipad'),
    ('PS','PS5')
)
class Sale(models.Model):
    product = models.CharField(max_length=20,choices=PRODUCT_CHOICES)
    salesmen=models.ForeignKey(User , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id}"

    def save(self,*args, **kwargs):
        price = None
        if self.product == 'TV':
            price = 559.99
        elif self.product == 'IPAD':
            price = 400
        elif self.product == 'PS':
            price = 500
        else :
            pass

        super().save(*args, **kwargs)