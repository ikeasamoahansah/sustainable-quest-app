from django.db import models


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField(True)
    joined_date = models.DateField(null=True)
    bit_character = models.CharField(max_length=255, null=True)
    points = models.IntegerField(default=0)
    tasks = models.URLField(null=True)
    rating = models.FloatField(default=0.0)

class Post(models.Model):
    name = models.CharField(default="TASK",max_length=255)
    SDGs = ( 
        ("1", "NO POVERTY"), 
        ("2", "ZERO HUNGER"), 
        ("3", "GOOD HEALTH AND WELL-BEING"), 
        ("4", "QUALITY EDUCATION"), 
        ("5", "GENDER EQUALITY"), 
        ("6", "CLEAN WATER AND SANITATION"), 
        ("7", "AFFORDABLE AND CLEAN ENERGY"), 
        ("8", "DECENT WORK AND ECONOMIC GROWTH"),
        ("9", "INDUSTRY, INNOVATION AND INFRASTRUCTURE"), 
        ("10", "REDUCED INEQUALITIES"),
        ("11", "SUSTAINABLE CITIES AND COMMUNITIES"),
        ("12", "RESPONSIBLE CONSUMPTION AND PRODUCTION"),
        ("13", "CLIMATE ACTION"),
        ("14", "LIFE BELOW WATER"),
        ("15", "LIFE ON LAND"),
        ("16", "PEACE, JUSTICE AND STRONG INSTITUTIONS"),
        ("17", "PARTNERSHIPS FOR THE GOALS"),
    ) 
    
    category = models.CharField( 
        max_length = 20, 
        choices = SDGs, 
        default = '1'
        ) 
    rating = models.FloatField(default=0.0)
    country= models.CharField(max_length=255)
    map = models.URLField()
    description = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    image = models.CharField(default='', max_length=255)


