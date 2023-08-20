from django.db import models
from django.contrib.auth.models import User
from entrepreneur.models import startup


# Create your models here.
class investedStartup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(startup, on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'investedStartup'
