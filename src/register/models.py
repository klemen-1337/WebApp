from django.db import models

# Create your models here.

class Register(models.Model):

    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title
# Create your models here.
