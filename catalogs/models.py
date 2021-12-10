from django.db import models

# Create your models here.
class Regions(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    iso = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    regions = models.ForeignKey(Regions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Routes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    cities = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PokeTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class States(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
