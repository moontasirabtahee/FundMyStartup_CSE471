from django.db import models

# Create your models here.
class feedback(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'feedback'
