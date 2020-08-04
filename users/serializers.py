from rest_framework import serializers
from users.models import User
import datetime


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthday = serializers.DateField()
    registration = serializers.DateField(default=datetime.date.today)
    order = serializers.IntegerField(source='order.id', read_only=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.registration = validated_data.get('registration', instance.registration)
        instance.order = validated_data.get('order', instance.order)
        instance.save()
        return instance
