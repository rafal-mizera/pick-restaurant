from django.db import models
from django.conf import settings

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    phone_number = models.CharField(max_length=20)
    notes = models.TextField()

class ExcludedRestaurants(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='excluded')
    date = models.DateField(auto_now_add=True)






