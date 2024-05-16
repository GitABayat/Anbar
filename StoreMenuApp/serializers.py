from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from StoreMenuApp.models import *


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'password', 'email', 'is_staff', 'is_superuser', 'is_active']


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email', 'is_staff', 'is_superuser', 'is_active']


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['Name', 'Status', 'Desc']


class GoodsAndServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsAndServices
        fields = ['Name', 'Status', 'Desc']


class CustomersGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomersGroup
        fields = ['Name', 'Status', 'Desc']


class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['Name', 'Status', 'Desc', 'Group', 'Family']


class ReceptSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recept
        fields = ['GoAndSer', 'Custom', 'Count', 'Type', 'Desc']

              