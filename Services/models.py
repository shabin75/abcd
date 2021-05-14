from django.db import models


class ServiceData(models.Model):
    head = models.CharField(max_length=50, blank=True, null=True)
    des = models.CharField(max_length=1000, blank=True, null=True)
    img = models.ImageField(upload_to='pic', blank=True, null=True)
    price=models.CharField(max_length=50, blank=True, null=True)
    spec=models.CharField(max_length=50, blank=True, null=True)
    offer=models.CharField(max_length=50, blank=True, null=True)
