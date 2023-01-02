from rest_framework import serializers
from .models import UsersData

class UsersDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersData
        fields = ('pk', 'name', 'mobile', 'email', 'country', 'city', 'dob', 'contract_start_date', 'contract_end_date','active', 'owner')