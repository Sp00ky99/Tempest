from django.db import models

class municipios(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
