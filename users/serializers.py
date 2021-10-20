from rest_framework import serializers
from users.models import Users

class UsersRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ['id', 'email', 'username', 'password']

  def create(self, validated_data):
    password = validated_data.pop('password', None)
    instance = self.Meta.model(**validated_data)
    if password is not None:
      instance.set_password(password)
    instance.save()
    return instance

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ['id', 'email', 'username', 'first_name', 'last_name', 'is_staff']