from django.db import models

# Create your models here.
class Ingredient(models.Model):
    ingredient = models.CharField(max_length=128)

    def __str__(self):
        return self.ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=128)
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    link_adress = models.URLField(max_length=128)

    def __str__(self):
        return self.name
