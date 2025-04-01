from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from users.serializers import LoginUserSerializer, RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from django.db.models import Q
from .permissions import IsLoggedIn


class RegisterUserViewSet(ModelViewSet):
    serializer_class = RegisterUserSerializer
    http_method_names = ['post']

class LoginUserview(ModelViewSet):
    permission_classes = [IsLoggedIn]
    serializer_class = LoginUserSerializer
    http_method_names = ['post']
    
    def create(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = CustomUser.objects.filter(Q(email=username) | Q(username=username)).first()
        print(user)
        print(user.check_password(password))
        if user and user.check_password(password):
            refresh_token = RefreshToken.for_user(user)
            return Response({
                'refresh_token': str(refresh_token),
                'access_token': str(refresh_token.access_token),
                'user_type': user.user_type
            }, status=status.HTTP_200_OK)
        return Response({"detail": user.email}, status=status.HTTP_401_UNAUTHORIZED)
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LogoutView(request):
    try:
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"detail": "logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)