from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20
                                 , choices=(('investor', 'investor'), ('entrepreneur', 'entrepreneur')))
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    nid_number = models.CharField(max_length=20)
    nid_image = models.ImageField(upload_to='nid_image')

    def __str__(self):
        return self.user.username

