from django.db import models

#Theme model
class Theme(models.Model):
    name = models.CharField(max_length=120, unique=True)
    id = models.IntegerField(unique=True)


    #Meta controls characteristics of the data. For example: adding indexes or ordering by name
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])],

    #Adding __str__ allows the model to read as a string instead of an object
    def __str__(self):
        return self.name


#Set model
class Set(models.Model):
    set_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=120,unique=True)
    year = models.IntegerField()
    num_parts = models.IntegerField()

    class Meta:
        ordering = ['-year','name']
        indexes = [
            models.Index(fields=['year']),
            models.Index(fields=['name']),
            models.Index(fields=['theme','year']),
        ]
    
    def __str__(self):
        return f"{self.set_number}-{self.name}"



