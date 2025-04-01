from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import CustomUser


class LoginUserSerializer(Serializer):
    username = CharField(max_length=100)
    password = CharField(write_only=True)
        
class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        return user