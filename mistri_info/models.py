from django.db import models

# Create your models here.

<<<<<<< HEAD
class Mistri(models.Model):
    image = models.ImageField(upload_to='mistri_info/', null=True, blank=True)
    name = models.CharField(max_length=100)
    # skill = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    contact = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
=======
# class Mistri(models.Model):
#     image = models.ImageField(upload_to='mistri_info/', null=True, blank=True)
#     name = models.CharField(max_length=100)
#     # skill = models.CharField(max_length=50)
#     location = models.CharField(max_length=100)
#     contact = models.IntegerField()

#     created_at = models.DateTimeField(auto_now_add = True)

#     def __str__(self):
#         return self.name

class Mistri(models.Model):
    image = models.ImageField(upload_to='mistri_info/', null=True, blank=True)
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=20, null=True)
    contact = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
>>>>>>> 6736dab (second commit)
