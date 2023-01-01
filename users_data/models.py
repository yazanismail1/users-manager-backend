from django.db import models

class UsersData(models.Model):
    name = models.CharField(max_length=56, null=True)
    mobile = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    country = models.CharField(max_length=56, null=True)
    city = models.CharField(max_length=56, null=True)
    dob = models.DateField(null=True)
    contract_start_date = models.DateField(null=True)
    contract_end_date = models.DateField(null=True)

    def __str__(self):
        return self.name
