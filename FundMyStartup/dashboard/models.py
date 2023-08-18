from django.db import models
from django.contrib.auth.models import User

class startup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    Equity = models.TextField()
    funding = models.DecimalField(max_digits=10, decimal_places=2)
    Sales =  models.DecimalField(max_digits=10, decimal_places=2)
    owner= models.TextField()
    profit = models.DecimalField(max_digits=10, decimal_places=2)
    debts = models.DecimalField(max_digits=10, decimal_places=2)




    def __str__(self):
        return self.title
