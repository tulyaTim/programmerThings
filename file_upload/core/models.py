from django.db import models

# Create your models here.

class Option(models.Model):
    value = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    dial_code = models.CharField(max_length=10)

    def __str__(self):
        return self.value
    

