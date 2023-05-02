from rest_framework import serializers
from django.contrib.auth import password_validation as pv

from .models import Category, Product, Order, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, write_only=True)
    password2 = serializers.CharField(max_length=64, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Порольи должны овподать')
        if attrs['username'] == attrs['password']:
            raise serializers.ValidationError('Нельзя username как пароль')

    def validate_password(self, value):
        try:
            pv.validate_password(value)
        except pv.ValidationError as e:
            raise serializers.ValidationError(e)
        else:
            return value

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user







