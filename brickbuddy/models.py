from django.db import models

#Theme model
class Theme(models.Model):
    name = models.CharField(max_length=120, unique=True)
    #id = models.IntegerField(unique=True)


    #Meta controls characteristics of the data. For example: adding indexes or ordering by name
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]

    #Adding __str__ allows the model to read as a string instead of an object
    def __str__(self):
        return self.name


#Set model
class Set(models.Model):
    set_num = models.CharField(unique=True)
    name = models.CharField(max_length=120)
    year = models.IntegerField()
    num_parts = models.IntegerField()
    theme = models.ForeignKey(
        Theme, on_delete=models.PROTECT,related_name="sets"
    )

    class Meta:
        ordering = ['-year','name']
        indexes = [
            models.Index(fields=['year']),
            models.Index(fields=['name']),
            models.Index(fields=['theme','year']),
        ]
    
    def __str__(self):
        return f"{self.set_num}-{self.name}"

#Minifigure Model
class MiniFig(models.Model):
    fig_num = models.CharField(unique=True)
    name = models.CharField(max_length=120)
    num_parts = models.IntegerField()

    class Meta:
        ordering = ['fig_num']
        indexes = [
            models.Index(fields=['fig_num']),
        ]
    
    def __str__(self):
        return f"{self.fig_num}-{self.name}"



