from django.db import models

# # Create your models here.
class Feature(models.Model):
#     id: int #not use id b/c in databse id is assign byself to every thing

    name = models.CharField(max_length=500)
    detail = models.CharField(max_length=500)

 