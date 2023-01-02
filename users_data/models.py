from django.db import models
from django.contrib.auth import get_user_model

class UsersData(models.Model):
    name = models.CharField(max_length=56, null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    country = models.CharField(max_length=56, null=True)
    city = models.CharField(max_length=56, null=True)
    dob = models.DateField(null=True)
    contract_start_date = models.DateField(null=True)
    contract_end_date = models.DateField(null=True)
    active = models.BooleanField(null=True)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.name
