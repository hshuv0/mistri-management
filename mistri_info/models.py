from django.db import models

# Create your models here.

class Mistri(models.Model):
    image = models.ImageField(upload_to='mistri_info/', null=True, blank=True)
    name = models.CharField(max_length=100)
    # skill = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
