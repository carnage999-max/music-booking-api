from rest_framework.serializers import ModelSerializer, Serializer, EmailField, CharField
from .models import ArtistProfile, CustomUser, OrganizerProfile


class LoginUserSerializer(Serializer):
    username = CharField(max_length=100)
    password = CharField(write_only=True)
        
class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.save()
        return user
    
class ArtistSerializer(ModelSerializer):
    class Meta:
        model = ArtistProfile
        fields = "__all__"
        read_only_fields = ['user']
        
class OrganizerSerializer(ModelSerializer):
    class Meta:
        model = OrganizerProfile
        fields = "__all__"
        read_only_fields = ['user']